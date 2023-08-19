from flask import Flask, request, jsonify, Blueprint
import pandas as pd
from datasets import Dataset
from transformers import AutoTokenizer, DistilBertForSequenceClassification, Trainer
import numpy as np
import requests
import io

predict_csv_bp = Blueprint('predict', __name__)

# Load your tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("model/tokenizer")
model = DistilBertForSequenceClassification.from_pretrained("model/saved_model")
#model.eval()

trainer = Trainer(
    model,
    tokenizer=tokenizer
)

task_to_keys = {
    "rte": ("rule", "entry")
}
rule, entry = task_to_keys['rte']

def preprocess_function(param):
    return tokenizer(param[rule], param[entry], truncation=True)

@predict_csv_bp.route('/predict_csv', methods=['POST'])
def predict_csv():
    if 'file' not in request.files or 'rules' not in request.form:
        return jsonify({'error': 'Missing data'})

    file = request.files['file']
    rules = request.form['rules']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        # Convert the file to prompted data using the convert_csv endpoint
        url_convert = "http://localhost:4000/api/v1/convert_csv"  # Update the URL accordingly
        files = {'file': file}
        data = {'rules': rules}
        response_convert = requests.post(url_convert, files=files, data=data)
        
        if response_convert.status_code == 200:
            csv_data = response_convert.content

            # Process the CSV data and make predictions
            df = pd.read_csv(io.BytesIO(csv_data))
            dataset = Dataset.from_pandas(df)
            encoded_dataset = dataset.map(preprocess_function, batched=True)

            predictions = trainer.predict(encoded_dataset, metric_key_prefix="predict")
            predicted_labels = np.argmax(predictions.predictions, axis=1)
            y_pred = np.argmax(predictions.predictions, axis=1)
            df['predicted'] = y_pred

            new = pd.DataFrame()
            new['Entry'] = df['entry']
            new['Compliant'] = df['predicted']

            filtered_rows = df[df['predicted'] == 0].to_dict(orient='records')
            count = len(filtered_rows)

            return jsonify({'filtered_rows': new.to_dict(orient='records'), "count": count})

        else:
            return jsonify({'error': 'Error generating prompted data'})