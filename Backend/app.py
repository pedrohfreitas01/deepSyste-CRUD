from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from dataclasses import dataclass
import datetime
from bson import ObjectId

app = Flask(__name__)
CORS(app, supports_credentials=True)

client = MongoClient("mongodb://localhost:27017")
db = client["user_database"]
users_collection = db["users"]

@dataclass
class UserPreferences:
    timezone: str

@dataclass
class User:
    username: str
    password: str
    roles: list
    preferences: UserPreferences
    active: bool = True
    created_ts: float = datetime.datetime.utcnow().timestamp()

@app.route('/api/users', methods=['GET'])
def get_users():
    users = list(users_collection.find())
    for user in users:
        user["_id"] = str(user["_id"])
    return jsonify(users)


    

@app.route('/api/users/<string:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = users_collection.find_one({"_id": ObjectId(user_id)})
        if user:
            user["_id"] = str(user["_id"])
            return jsonify(user)
        return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400



@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(
        username=data["username"],
        password=data["password"],
        roles=data["roles"],
        preferences=UserPreferences(timezone=data["user_timezone"]),
        active=data["is_user_active"],
        created_ts=datetime.datetime.utcnow().timestamp()
    )
    users_collection.insert_one(user.__dict__)
    return jsonify({"message": "User created successfully"}), 201

@app.route('/api/users/<string:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    updated_user = {
        "username": data["username"],
        "password": data["password"],
        "roles": data["roles"],
        "preferences": {"timezone": data["user_timezone"]},
        "active": data["is_user_active"],
        "created_ts": datetime.datetime.utcnow().timestamp()
    }
    result = users_collection.update_one({"_id": ObjectId(user_id)}, {"$set": updated_user})
    if result.modified_count > 0:
        return jsonify({"message": "User updated successfully"}), 200
    return jsonify({"error": "User not found"}), 404

@app.route('/api/users/<string:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if not user_id:
        return jsonify({"error": "Invalid user ID"}), 400

    result = users_collection.delete_one({"_id": ObjectId(user_id)})

    if result.deleted_count > 0:
        return jsonify({"message": "User deleted successfully"}), 200

    return jsonify({"error": "User not found"}), 404


