import requests
from flask import Flask, render_template, requests
from bs4 import BeautifulSoup

MONGODB_URI = os.environ.get('MONGODB_URI')
DB_NAME = os.environ.get("DB_NAME")

client = MongoClient(MONGODB_URI)
db = client(DB_NAME)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port = 5000, debug = True)