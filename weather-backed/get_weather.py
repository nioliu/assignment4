from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)
API_KEY = '5acbac2a26b67b9b119b2a85ea0242f3'


@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('q')
    zipcode = request.args.get('zip')
    unit = request.args.get('units', 'metric')
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        'q': city,
        'zip': zipcode,
        'appid': API_KEY,
        'units': unit
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return jsonify({'error': 'Could not retrieve weather data'}), response.status_code


if __name__ == '__main__':
    app.run(debug=True)
