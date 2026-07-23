# rodos

A Django web application.

## Local Setup

**Requirements:** Python 3.9+

```bash
# Clone the repo and enter the directory
git clone <repo-url>
cd rodos

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the development server
python manage.py runserver
```

Visit http://127.0.0.1:8000 — you should see "Hello, World!".

## Project Structure

```
rodos/
├── core/           # Main app (views, URLs)
├── rodos/          # Django project config (settings, root URLs)
├── manage.py
└── requirements.txt
```
