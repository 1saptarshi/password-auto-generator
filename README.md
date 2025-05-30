# Password Auto Generator

A simple web app to generate secure passwords with selectable length and strength, built with Flask and Tailwind CSS.

## Features

- Choose password length (4–20 characters)
- Select password strength:
  - Only letters (a-z, A-Z)
  - Letters and numbers (a-z, A-Z, 0-9)
  - Letters, numbers, and symbols (a-z, A-Z, 0-9, !@#$...)
- Copy generated password to clipboard
- Light/Dark mode toggle

## Requirements

- Python 3.6+
- Flask

## Installation

1. **Clone or download this repository.**
2. **Install Flask:**
   ```sh
   pip install flask
   ```
3. **Ensure your folder structure:**
   ```
   password auto generator/
   ├── password.py
   └── templates/
       └── index.html
   ```

## Usage

1. **Run the Flask app:**
   ```sh
   python password.py
   ```
2. **Open your browser and go to:**
   ```
   http://127.0.0.1:5000/
   ```

## File Overview

- `password.py` — Flask backend for password generation
- `templates/index.html` — Frontend UI (uses Tailwind CSS and Font Awesome via CDN)

## License

MIT License
