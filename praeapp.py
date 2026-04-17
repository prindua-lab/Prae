
from flask import Flask
import random

app = Flask(__name__)

phrases = [
    "รักมากนะะะ พิมพ์อะไรมาก็รักหมดดด",
    "เมื่อไรจะกลับมาาาา",
    "ง้ออออออ",
    "รักแพรรรรรรรรร"
]

@app.route('/')
def home():
    return random.choice(phrases)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
