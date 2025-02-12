import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

database_url = os.getenv("DATABASE_URL")
if not database_url:
	raise RuntimeError("❌ DATABASE_URL is not set! Check your .env file.")

print("✅ Loaded DATABASE_URL:", database_url)

