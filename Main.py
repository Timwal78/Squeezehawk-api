
from flask import Flask, jsonify
from flask_cors import CORS
import requests
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({
        "message": "Squeezehawk API is running!",
        "timestamp": datetime.now().isoformat(),
        "status": "active"
    })

@app.route('/api/hawks/price')
def get_hawks_price():
    try:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=seahawks&vs_currencies=usd", timeout=10)
        data = response.json()
        return jsonify({
            "price": data.get("seahawks", {}).get("usd", 0),
            "timestamp": datetime.now().isoformat(),
            "source": "coingecko"
        })
    except:
        return jsonify({"error": "Unable to fetch price", "price": 0})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
      
