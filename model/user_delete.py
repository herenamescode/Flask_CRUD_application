from flask import make_response

def delete_user(redis, user_id):
    try:
        key = f"user:{user_id}"
        # Check whether user exists
        if not redis.exists(key):
            return make_response({"message": "Nothing to Delete"}, 200)

        # Delete from Redis
        redis.delete(key)

        return make_response({"message": "User Deleted Successfully"}, 200)

    except Exception as e:
        return make_response({"message": f"Query Failed: {e}"}, 400)
