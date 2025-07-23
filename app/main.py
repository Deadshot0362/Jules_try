from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

from flask import request, jsonify
from scripts.content_extractor import extract_text_from_url
from scripts.chatbot_generator import generate_chatbot_from_text

@app.route('/generate', methods=['POST'])
def generate():
    url = request.form['url']
    text = extract_text_from_url(url)
    if text:
        chatbot = generate_chatbot_from_text(text)
        return jsonify(chatbot)
    else:
        return "Error extracting text."

if __name__ == '__main__':
    app.run(debug=True)
