from flask import jsonify
# import sqlite3

def read_user(redis):
    try:
        # Get all user keys
        keys = redis.keys("user:*")
        users = []

        for key in keys:
            user = redis.hgetall(key)
            users.append(user)

        if users:
            return jsonify({"database": users})
        else:
            return jsonify({"message": "No data found"}), 404

    except Exception as e:
        return jsonify({"message": f"Query Failed: {e}"}), 400
 