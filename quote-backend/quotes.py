from flask import Flask, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
API_KEY = '5acbac2a26b67b9b119b2a85ea0242f3'


@app.route('/quote', methods=['GET'])
def get_weather():
    base_url = "https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json"

    response = requests.get(base_url)

    if response.status_code == 200:
        return response.json()
    else:
        return jsonify({'error': 'Could not retrieve weather data'}), response.status_code


if __name__ == '__main__':
    app.run(debug=True)
