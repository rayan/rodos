# AGENTS.md

Guidelines for AI agents working on this codebase.

## Environment Setup

Before doing anything else, set up the Python environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running the App

```bash
python manage.py runserver
```

## Running Checks

```bash
python manage.py check        # Django system check
python manage.py test         # Run tests (once tests are added)
```

## Project Conventions

- Django apps live at the top level (e.g. `core/`).
- Each app has its own `urls.py`; root URL conf is `rodos/urls.py`.
- Keep `requirements.txt` up to date when adding dependencies (`pip freeze > requirements.txt`).
- Do not commit `venv/`, `__pycache__/`, or `db.sqlite3`.

## Key Files

| File | Purpose |
|------|---------|
| `rodos/settings.py` | Django settings |
| `rodos/urls.py` | Root URL configuration |
| `core/views.py` | Application views |
| `core/urls.py` | App-level URL patterns |
| `requirements.txt` | Python dependencies |
