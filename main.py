from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Squeezehawk API is running!"

@app.route('/api/hawks/price')
def get_price():
    return jsonify({"price": 0.0001})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
      
