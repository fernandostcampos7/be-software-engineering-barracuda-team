from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity
from app.utils.auth_utils import supabase_jwt_required  # adjust if path is different

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
	return jsonify({"message": "User registered successfully!"})

@auth_bp.route("/profile", methods=["GET"])
@supabase_jwt_required
def get_profile():
	user = get_jwt_identity()
	return jsonify(user), 200
