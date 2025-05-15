import json

def load_config(path="config.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "ui_port": 7860,
            "model_name": "facebook/blenderbot-400M-distill",
            "tie_break_strategy": "alfabeto"
        }
