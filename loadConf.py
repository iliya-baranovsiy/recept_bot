import json

with open("config.json", mode="r", encoding="utf-8") as f:
    data = json.loads(f.read())

TOKEN = data.get("TOKEN")
