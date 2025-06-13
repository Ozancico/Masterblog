# Masterblog

A simple blog created with Flask.

## Features

- Display blog posts
- Create new posts
- Edit existing posts
- Delete posts
- Like feature for posts

## Installation

1. Install Python 3.x
2. Clone repository
3. Create and activate virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # For Unix/macOS
# OR
.venv\Scripts\activate     # For Windows
```
4. Install dependencies:
```bash
pip install flask
```

## Running

1. Start Flask application:
```bash
python app.py
```
2. Open in browser: http://localhost:5000

## Project Structure

```
masterblog/
│
├── app.py              # Flask main application
├── data.json          # JSON data store for blog posts
├── style.css          # CSS styling
│
└── templates/         # HTML templates
    ├── index.html    # Main page with post list
    ├── add.html      # Form for new posts
    └── update.html   # Form for editing
```
