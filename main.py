from flask import Flask, request, jsonify, render_template
import requests
from datetime import datetime

app = Flask(__name__)
API_KEY = MY_API_KEY  # Replace with your OpenWeatherMap API key

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_local_weather")
def get_local_weather():
    lat = request.args.get("lat")
    lon = request.args.get("lon")
    date = request.args.get("date")

    # Fetch current weather (OpenWeatherMap's /weather endpoint doesn't support historical data)
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    response = requests.get(weather_url)
    return jsonify(response.json())

@app.route("/get_forecast")
def get_forecast():
    city = request.args.get("city")
    date = request.args.get("date")

    # Fetch 5-day forecast (OpenWeatherMap's /forecast endpoint)
    forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(forecast_url)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True)