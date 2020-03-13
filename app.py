from flask import Flask, jsonify

def create_app(test_config=None):
    app = Flask(__name__)

    @app.route('/')
    def test_app():
        return jsonify({
            "greeting": "hallo mops"
        })

    return app

app = create_app()