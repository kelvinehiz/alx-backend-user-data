#!/usr/bin/env python3
"""Session authentication route module."""

from flask import Blueprint, jsonify, request
from models.user import User
from api.v1.app import auth
import os

# Define the Blueprint for session authentication
session_auth = Blueprint('session_auth', __name__)


@session_auth.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """Handles session authentication login."""
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    user = User.search({'email': email})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404

    user = user[0]  # Assume email is unique so we take the first match

    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(user.id)
    response = jsonify(user.to_json())

    session_name = os.getenv('SESSION_NAME', 'session_id')
    response.set_cookie(session_name, session_id)

    return response
