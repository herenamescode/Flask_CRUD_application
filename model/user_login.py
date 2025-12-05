from flask import make_response
from werkzeug.security import check_password_hash

def login_user(redis, data):
    try:
        email = data['email']
        password = data['pass']
        keys = redis.keys("user:*")

        for key in keys:
            user = redis.hgetall(key)

            # Match email
            if user.get("email") == email:

                # Check hashed password
                if check_password_hash(user.get("pass"), password):

                    user_data = {
                        "id": user["id"],
                        "name": user["name"],
                        "roll_batch": user["roll_batch"],
                        "branch": user["branch"],
                        "email": user["email"]
                    }

                    return make_response(
                        {"message": "Login Successful", "user": user_data},
                        200
                    )

                else:
                    return make_response({"message": "Invalid Credentials"}, 400)

        # No email found
        return make_response({"message": "Invalid Credentials"}, 400)

    except Exception as e:
        return make_response({"message": f"Error: {e}"}, 500)