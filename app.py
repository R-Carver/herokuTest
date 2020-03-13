from flask import Flask, jsonify

from models import setup_db, Player, db

def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    db.create_all()

    @app.route('/')
    def test_app():
        return jsonify({
            "greeting": "hallo mops"
        })

    return app

app = create_app()