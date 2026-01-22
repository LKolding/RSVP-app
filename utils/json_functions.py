import json

# from main.py
def get_settings() -> dict:
    with open('settings.json', 'r') as f:
        return json.load(f)
   