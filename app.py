from flask import Flask, jsonify, abort, request
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
    @requires_auth('get:players')
    def get_players(payload):
    #def get_players():
        players = Player.query.all()

        outplayers = [player.format() for player in players]

        return jsonify({
            'success': True,
            'players': outplayers
        })

    @app.route('/players', methods=['POST'])
    @requires_auth('post:players')
    def create_player(payload):
    #def create_player():
        try:
            body = request.get_json()

            new_name = body.get('name', None)
            new_skill = body.get('skill', None)

            player = Player(name=new_name, skill=new_skill)
            player.insert()

            return jsonify({
                'success':True,
                'player':player.format()
            })
        except:
            abort(422)

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success":False,
            "error":422,
            "message":"unprocessable"
        })

    return app

app = create_app()