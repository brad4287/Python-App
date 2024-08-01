from app import app
import os

@app.route("/")
def index():
# Purpose of this file is to create-view 
    app_name = os.getenv("APP_NAME")

    if app_name:
        return f"Hello from {app_name} running in a Docker container behind Nginx!"

    return "Hello from Flask"