from app.storage.memory import users, get_next_id
from app.errors.handlers import AppError

def create_user(data: dict):
    if "name" not in data or "email" not in data:
        raise AppError("name and email are required", 400)

    user_id = get_next_id()
    user = {
        "id": user_id,
        "name": data["name"],
        "email": data["email"],
    }

    users[user_id] = user
    return user, 201

def get_all_users():
    return list(users.values()), 200

def get_user_by_id(user_id: int):
    user = users.get(user_id)
    if not user:
        raise AppError("User not found", 404)

    return user, 200

def update_user(user_id: int, data: dict):
    user = users.get(user_id)
    if not user:
        raise AppError("User not found", 404)

    user["name"] = data.get("name", user["name"])
    user["email"] = data.get("email", user["email"])

    return user, 200

def delete_user(user_id: int):
    if user_id not in users:
        raise AppError("User not found", 404)

    del users[user_id]
    return "", 204