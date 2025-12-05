from flask import make_response
# import sqlite3
    
def update_user(redis, user_id, data):
    try:
        key = f"user:{user_id}"

        if not redis.exists(key):  # Check if user exists
            return make_response({"message": "NOTHING_TO_UPDATE"}, 204)

        update_data = {}

        if "name" in data:
            update_data["name"] = data["name"]

        if "email" in data:
            update_data["email"] = data["email"]

        if "roll_batch" in data:
            update_data["roll_batch"] = data["roll_batch"]

        if "branch" in data:
            update_data["branch"] = data["branch"]

        if not update_data:
            return make_response({"message": "NOTHING_TO_UPDATE"}, 204)
        redis.hset(key, mapping=update_data)         # Update Redis Hash

        return make_response({"message": "UPDATED_SUCCESSFULLY"}, 201)

    except Exception as e:
        return make_response(
            {"message": "UPDATE_FAILED", "error": str(e)}, 
            500
        )