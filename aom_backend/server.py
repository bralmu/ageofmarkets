#!/user/bin/env python3 -tt
"""
Module documentation.
"""


import sys, json
import worldmap, worldplayers
from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS, cross_origin


WORLD_MAP = None
WORLD_PLAYERS = None


class WorldMapAPIResource(Resource):

    def get(self):
        global WORLD_MAP
        return WORLD_MAP.get_serializable(), 200

    def post(self, parameter1):
        pass

    def put(self, parameter1):
        pass

    def delete(self, parameter1):
        pass


class WorldPlayersAPIResource(Resource):

    def get(self):
        global WORLD_PLAYERS
        return WORLD_PLAYERS.get_serializable(), 200

    def post(self, parameter1):
        pass

    def put(self, parameter1):
        pass

    def delete(self, parameter1):
        pass


def build_world():
    
    global WORLD_MAP, WORLD_PLAYERS

    WORLD_MAP = worldmap.WorldMap()
    WORLD_PLAYERS = worldplayers.WorldPlayers()


def build_and_run_api():

    app = Flask(__name__)
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    api = Api(app)
    api.add_resource(WorldMapAPIResource, "/worldmap/")
    api.add_resource(WorldPlayersAPIResource, "/worldplayers/")
    app.run(debug=True, use_reloader=False)
    

def main():

    args = sys.argv[1:]
    if args:
        print('no args needed so far, aborting')
        sys.exit(1)

    build_world()
    build_and_run_api()


if __name__ == '__main__':
    main()
