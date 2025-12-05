import redis
import json
from flask import jsonify, make_response
from .user_create import create_user
from .user_login import login_user
from .user_delete import delete_user
from .user_read import read_user
from .user_update import update_user

class user_model:
    def __init__(self):
        try:
            self.redis = redis.Redis (
                host='redis-17870.c82.us-east-1-2.ec2.cloud.redislabs.com',     
                port=17870,            
                password="Pa5s6iMXlg1V2pZ7agrTskI3atjbBH95",        
                decode_responses=True 
            )
            print("Redis Connection Established")

        except Exception as e:
            print(f"Redis Connection Error: {e}")

# Fahad's Side of the work Includes -> (Create and Delete)

    def create_c(self, data):
        return create_user(self.redis, data)

    def delete_d(self, id):
        return delete_user(self.redis, id)
    
# Extra Login Feature
    def login_l(self, data):  
        return login_user(self.redis, data)

# Nameera's Side of the work Includes -> (Update and Read)
    def getall(self):
        return read_user(self.redis)

    def update(self, id, data):
        return update_user(self.redis, id, data)    

