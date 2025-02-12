from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Flask app Initialization
app = Flask(__name__)

#Ensuring the DATABASE_URL is properly loaded
database_url = os.getenv("DATABASE_URL")
print("✅ Debugging: Loaded DATABASE_URL:", database_url)  # Debugging line
if not database_url:
	raise RuntimeError("❌ DATABASE_URL is not set! Check your .env file.")

# Loading .env variables
load_dotenv()
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initializing Extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
CORS(app)

@app.route("/")
def home():
	return {"message": "Welcome to Komodo Hub API!"}

# Importing routes
from app.routes.auth_routes import auth_bp
app.register_blueprint(auth_bp, url_prefix="/api/auth")

if __name__ == "__main__":
	app.run(debug=True)