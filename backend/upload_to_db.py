from flask import Flask, request, jsonify, Blueprint
import sqlite3

upload_to_db_bp = Blueprint('db_upload', __name__)

# Initialize SQLite database
db_path = 'uploaded_files.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create table to store CSV data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS csv_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT,
        data BLOB
    )
''')
conn.commit()

# Route to store CSV data into SQLite
@upload_to_db_bp.route('db_upload', methods=['POST'])
def upload_csv():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    csv_data = file.read()
    cursor.execute('INSERT INTO csv_data (filename, data) VALUES (?, ?)', (file.filename, csv_data))
    conn.commit()

    return jsonify({'message': 'CSV file uploaded successfully'})