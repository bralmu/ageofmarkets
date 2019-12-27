#!/user/bin/env python3 -tt
"""
Module documentation.
"""


import sys, json
import world
from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS, cross_origin


GAME_WORLD = None


class Game(Resource):

    def get(self):
        global GAME_WORLD
        return GAME_WORLD.get_serializable(), 200

    def post(self, parameter1):
        pass

    def put(self, parameter1):
        pass

    def delete(self, parameter1):
        pass


def main():

    global GAME_WORLD
    args = sys.argv[1:]

    if args:
        print('no args needed so far, aborting')
        sys.exit(1)

    GAME_WORLD = world.World()

    app = Flask(__name__)
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    api = Api(app)
    api.add_resource(Game, "/")
    app.run(debug=True, use_reloader=False)


if __name__ == '__main__':
    main()
