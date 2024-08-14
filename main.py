from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_cat')
def get_cat():
    cat_response = requests.get('https://api.thecatapi.com/v1/images/search')
    cat_image_url = cat_response.json()[0]['url']
    return jsonify(url=cat_image_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)