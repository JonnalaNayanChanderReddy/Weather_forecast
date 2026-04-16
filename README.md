# 🌦️ Weather App (Flask + OpenWeather API)

A simple and responsive weather application built using **Flask (Python)** and **OpenWeather API**.
Users can enter a city name and get real-time weather details like temperature, humidity, and conditions.

---

## 🚀 Features

* 🌍 Search weather by city name
* 🌡️ Displays temperature (°C)
* 🤗 Shows "feels like" temperature
* 💧 Humidity information
* ☁️ Weather condition description
* ❌ Error handling for invalid cities
* 🎨 Simple and clean UI

---

## 🛠️ Tech Stack

* **Backend:** Python (Flask)
* **Frontend:** HTML, CSS (Jinja2 Templates)
* **API:** OpenWeather API

---

## 📁 Project Structure

```
weather_app/
│
├── app.py
└── templates/
    └── index.html
```

---

## 🔑 Setup Instructions

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/weather-app.git
cd weather-app
```

---

### 2️⃣ Install dependencies

```
pip install flask requests
```

---

### 3️⃣ Get API Key

* Go to: https://openweathermap.org/api
* Sign up and generate an API key

---

### 4️⃣ Add API Key

Open `app.py` and replace:

```
API_KEY = "your_api_key_here"
```

with your actual API key.

---

### 5️⃣ Run the application

```
python app.py
```

---

### 6️⃣ Open in browser

```
http://127.0.0.1:5000/
```

---

## ⚠️ Common Issues

### ❌ "City not found"

* Check spelling of city
* Ensure API key is active (may take 5–10 minutes)

### ❌ "Invalid API key"

* Verify key is correct
* Regenerate key if needed


## 🌟 Future Enhancements

* 📍 Auto-detect location
* 📊 5-day weather forecast
* 🌙 Dark mode
* ⚡ AJAX (no page reload)
* 📱 Mobile responsive UI

---

## 🤝 Contributing

Feel free to fork this repo and improve the project!

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 🙌 Acknowledgements

* OpenWeather API for providing weather data
* Flask for lightweight backend framework

---

## 💡 Author

**Nayan Chander Reddy**

---
