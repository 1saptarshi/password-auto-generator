from flask import Flask, render_template, request, jsonify
import string
import random

app = Flask(__name__)

def generate_password(length, strength):
    characters = string.ascii_letters  # Option 1: Only letters
    if strength == '2':  # Option 2: Letters and numbers
        characters += string.digits
    elif strength == '3':  # Option 3: Letters, numbers, and symbols
        characters += string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    length = int(data.get('length', 12))
    strength = data.get('strength', '1')
    password = generate_password(length, strength)
    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(debug=True)