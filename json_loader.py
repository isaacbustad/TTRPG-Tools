# data_loader.py
import json
import os
from flask import current_app

def load_json(filename):
    """Safely loads a JSON file from the project root."""
    # This assumes your json files are in a folder named 'data'
    file_path = os.path.join(current_app.root_path, 'data', filename)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)