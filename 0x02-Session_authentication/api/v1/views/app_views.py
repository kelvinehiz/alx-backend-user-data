#!/usr/bin/env python3
"""Module containing routes for the API."""

from flask import Blueprint, jsonify, abort

app_views = Blueprint('app_views', __name__)


@app_views.route('/api/v1/status/', methods=['GET'])
def status():
    """Returns the status of the API."""
    return jsonify({"status": "OK"})


@app_views.route('/api/v1/stats/', methods=['GET'])
def stats():
    """Returns some statistics (example: number of users)."""
    # Example data; replace with actual logic if needed
    stats_data = {
        "users": 100,  # Example data
        "sessions": 50  # Example data
    }
    return jsonify(stats_data)


@app_views.route('/api/v1/unauthorized/', methods=['GET'])
def unauthorized():
    """Triggers a 401 error for testing purposes."""
    abort(401)


@app_views.route('/api/v1/forbidden/', methods=['GET'])
def forbidden():
    """Triggers a 403 error for testing purposes."""
    abort(403)


@app_views.route('/api/v1/auth_session/login/', methods=['POST'])
def login():
    """Handles the session login.

    Example logic:
    - Validate user credentials.
    - Create a session.
    - Return a session cookie.
    """
    # Implement login logic here
    return jsonify({"message": "Login successful"}), 200
