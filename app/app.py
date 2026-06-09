from flask import Flask

def create_app():
    app = Flask(__name__)

    employees = []

    @app.route("/")
    def home():
        return {
            "status": "running",
            "employees": len(employees)
        }

    return app