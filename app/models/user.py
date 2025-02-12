from app import db
from datetime import datetime, timezone

class User(db.Model):
	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key=True)
	email =db.Column(db.String(120), unique=True, nullable=False)
	role = db.Column(db.Enum("super_admin", "school_admin", "teacher", "student", "community_member", "public", name="user_roles"), nullable=False)
	first_name = db.Column(db.String(50), nullable=False)
	last_name = db.Column(db.String(50), nullable=False)
	school_id = db.Column(db.Interger, nullable=True)
	community_id = db.Column(db.Interger, nullable=True)
	created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
	updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

	def __repr__(self):
		return f"<User {self.email} - {self.role}>"


