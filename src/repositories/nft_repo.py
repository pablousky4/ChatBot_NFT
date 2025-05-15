import json
import uuid
from datetime import datetime
from pathlib import Path

class NFTRepository:
    def __init__(self, file_path="data/nfts.json"):
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.file_path.exists():
            self._save_data([])

    def _load_data(self):
        with open(self.file_path, "r") as f:
            return json.load(f)

    def _save_data(self, data):
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4, default=str)

    def add_token(self, token):
        tokens = self._load_data()
        tokens.append(token)
        self._save_data(tokens)

    def get_tokens_by_owner(self, username):
        return [t for t in self._load_data() if t["owner"] == username]

    def transfer_token(self, token_id, new_owner):
        tokens = self._load_data()
        found = False
        for t in tokens:
            if t["token_id"] == token_id:
                t["owner"] = new_owner
                found = True
                break
        if not found:
            raise ValueError("Token no encontrado")
        self._save_data(tokens)

    def get_all_tokens(self):
        return self._load_data()
