import io
from flask import Flask, Response, request, send_file,Blueprint
import pandas as pd
from helpers import convert_to_prompt

generate_csv_bp = Blueprint('convert', __name__)
@generate_csv_bp.route('/convert_csv', methods=['POST'])
def generate_csv():
    if 'file' not in request.files or 'rules' not in request.form:
        return "Error: Missing data"

    file = request.files['file']
    rules_list = request.form['rules'].split('\n')

    if file.filename == '':
        return "Error: No selected file"

    df = pd.read_csv(file)
    prompted_df = convert_to_prompt(rules_list, df)

    csv_data = io.StringIO()
    prompted_df.to_csv(csv_data, index=False)
    csv_data.seek(0)

    return Response(csv_data.getvalue(), headers={
        "Content-Disposition": "attachment; filename=prompted.csv",
        "Content-Type": "text/csv"
    })