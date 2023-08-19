from flask import Flask, request, jsonify
import pandas as pd
from datasets import Dataset
from transformers import AutoTokenizer, DistilBertForSequenceClassification, Trainer
import torch
import numpy as np

app = Flask(__name__)

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

@app.route('/predict_csv', methods=['POST'])
def predict_csv():
    if 'fisier' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['fisier']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        df = pd.read_csv(file)
        dataset = Dataset.from_pandas(df)
        encoded_dataset = dataset.map(preprocess_function, batched=True)

        predictions = trainer.predict(encoded_dataset, metric_key_prefix="predict")
        predicted_labels = np.argmax(predictions.predictions, axis=1)
        y_pred = np.argmax(predictions.predictions, axis=1)
        df['predicted'] = y_pred

        filtered_rows = df[df['predicted'] == 0].to_dict(orient='records')
        count = len(filtered_rows)

        return jsonify({'filtered_rows': filtered_rows,"count":count})

if __name__ == '__main__':
    app.run(host='localhost', port=4000, debug=True)

