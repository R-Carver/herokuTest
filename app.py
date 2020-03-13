from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

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

    @app.route('/players', methods=['GET'])
    #@requires_auth('get:players')
    #def get_players(payload):
    def get_players():
        players = Player.query.all()

        outplayers = [player.format() for player in players]

        return jsonify({
            'success': True,
            'players': outplayers
        })

    return app

app = create_app()