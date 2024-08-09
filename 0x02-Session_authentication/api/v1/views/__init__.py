#!/usr/bin/env python3
"""Initialize the views module."""
from api.v1.views.app_views import app_views
from api.v1.views.session_auth import session_auth

# Register the Blueprints
# Register session_auth with a URL prefix to ensure it's correctly scoped
app_views.register_blueprint(session_auth, url_prefix='/api/v1')
