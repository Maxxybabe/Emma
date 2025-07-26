import os
from typing import List

API_ID = os.environ.get("23616884", "")
API_HASH = os.environ.get("a9383cb4eb58b76d1dbc6cb82461f6de", "")
BOT_TOKEN = os.environ.get("7529400895:AAGkMZJK90Q1KkoljOoAls8Ylqj4xxSbbuA", "")
ADMIN = int(os.environ.get("8185479084", ""))
PICS = (os.environ.get("PICS", "")).split()

LOG_CHANNEL = int(os.environ.get("-1002704956540", ""))
NEW_REQ_MODE = os.environ.get("NEW_REQ_MODE", "False").lower() == "true"  # Set "True" For accept new requests

DB_URI = os.environ.get("mongodb+srv://maxen:maxen@cluster0.3bz6vzu.mongodb.net/?retryWrites=true&w=majority", "")
DB_NAME = os.environ.get("DB_NAME", "")

IS_FSUB = os.environ.get("IS_FSUB", "False").lower() == "true"  # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "-100******** -100*********").split())) # Add Multiple channel ids
