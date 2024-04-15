from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def get_weather():
    latitude = request.args.get('lat')
    longitude = request.args.get('lon')
    
    if not latitude or not longitude:
        return jsonify({'error': 'Latitude and longitude parameters are required'}), 400

    api_key = os.getenv('API_KEY')

    url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric'

    response = requests.get(url)
    
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Failed to fetch weather data'}), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)