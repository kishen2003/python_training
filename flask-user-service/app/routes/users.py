from flask import Blueprint, request

from app.services.user_service import (
    create_user,
    get_all_users,
    get_user_by_id,
    update_user,
    delete_user,
)
from app.errors.handlers import AppError

users_bp = Blueprint("users", __name__, url_prefix="/users")

@users_bp.route("", methods=["POST"])
def create_user_api():
    data = request.get_json()
    if not data:
        raise AppError("Invalid request body", 400)

    return create_user(data)

@users_bp.route("", methods=["GET"])
def get_users_api():
    return get_all_users()

@users_bp.route("/<int:user_id>", methods=["GET"])
def get_user_api(user_id: int):
    return get_user_by_id(user_id)

@users_bp.route("/<int:user_id>", methods=["PUT"])
def update_user_api(user_id: int):
    data = request.get_json()
    if not data:
        raise AppError("Invalid request body", 400)

    return update_user(user_id, data)

@users_bp.route("/<int:user_id>", methods=["DELETE"])
def delete_user_api(user_id: int):
    return delete_user(user_id)