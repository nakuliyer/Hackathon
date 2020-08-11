from dotenv import load_dotenv, find_dotenv

# load .env into os.getenv function
loaded = load_dotenv(find_dotenv())

if not loaded:
    raise Exception(".env error")

# now start flask
from flask import Flask
app = Flask(__name__)

import clientbot.routes
import os

# port = int(os.environ.get("PORT", 9874))

# app.run(port=port, debug=True)
app.run()
