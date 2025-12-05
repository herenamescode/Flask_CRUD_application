from flask import make_response
from werkzeug.security import generate_password_hash
import uuid

def create_user(redis, data):
    try:
        user_id = str(uuid.uuid4())
        hashed_password = generate_password_hash(data['pass']) #hashing

        user_data = {
            "id": user_id,
            "name": data["name"],
            "email": data["email"],
            "pass": hashed_password,
            "roll_batch": data["roll_batch"],
            "branch": data["branch"]
        }

        redis.hset(f"user:{user_id}", mapping=user_data)      # Save user as Redis Hash

        return make_response(
            {"message": f"{data['name']} added successfully", "id": user_id}, 
            200
        )

    except Exception as e:
        return make_response({"message": f"Query Failed: {e}"}, 400)
