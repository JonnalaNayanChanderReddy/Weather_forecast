from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "417b470f431af7c701cfebd4f72498f2"  # 🔑 Replace this
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")

        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        try:
            response = requests.get(BASE_URL, params=params)
            data = response.json()

            if data["cod"] == 200:
                weather = {
                    "city": city,
                    "temp": data["main"]["temp"],
                    "feels": data["main"]["feels_like"],
                    "humidity": data["main"]["humidity"],
                    "condition": data["weather"][0]["description"]
                }
            else:
                error = "City not found!"
        except:
            error = "Something went wrong!"

    return render_template("index.html", weather=weather, error=error)

if __name__ == "__main__":
    app.run(debug=True)