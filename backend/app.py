from flask import Flask
from convert_csv import generate_csv_bp
from predict import predict_csv_bp

app = Flask(__name__)

app.register_blueprint(generate_csv_bp, url_prefix='/api/v1')
app.register_blueprint(predict_csv_bp, url_prefix='/api/v1')

if __name__ == '__main__':
    app.run(host='localhost', port=4000, debug=True)
