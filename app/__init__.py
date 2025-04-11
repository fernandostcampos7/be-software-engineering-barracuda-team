import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
from app.routes.auth_routes import auth_bp  # ✅ Corrected import

# ✅ Load environment variables
load_dotenv()

# ✅ Initialise Flask app
app = Flask(__name__)

# ✅ Setup CORS to allow frontend to access backend
CORS(app, supports_credentials=True, origins=[
    "https://fe-software-engineering-barracuda-team.vercel.app"
])

# ✅ Set up database configuration
database_url = os.getenv("DATABASE_URL")
if not database_url:
    raise RuntimeError("❌ DATABASE_URL is not set! Check your .env file.")

app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

print("✅ Loaded DATABASE_URL:", database_url)

# ✅ Initialise SQLAlchemy
db = SQLAlchemy(app)

# ✅ Register blueprints
app.register_blueprint(auth_bp, url_prefix="/api/auth")

# ✅ Main entrypoint
if __name__ == "__main__":
    app.run(debug=True)
