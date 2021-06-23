# GRUPPE 21
import unittest
import json
from cvengine import edge as im
from os import environ as env, listdir
from database.mongo import MongoDB
from models.gamestate import GameState

class TestOneGame(unittest.TestCase):
    def test_one_game(self):
        uri     = env['CDIO_MONGO_PASS']
        db      = MongoDB(uri)
        images  = [im.get(f'resources/onegame/{x}') for x in sorted(listdir('resources/onegame'))]
        for img in images:
            #im.show(img)
            gamestate = im.gamestate_from_board(db, img)
            jsonn = gamestate.json()
            print(json.dumps(jsonn, indent=2))
