import os
import json

__PATH = os.path.join(os.path.dirname(__file__), "console.config.json")

with open(__PATH, "r") as config:
  CONFIG = json.loads(config.read())