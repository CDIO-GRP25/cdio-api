from cvengine.edge import CVEngine
from cvengine import serializer as im
from database.mongo import MongoDB
import os

uri = os.environ['CDIO_MONGO_PASS']

db = MongoDB(uri)

cv = CVEngine()

x = [x for x in os.listdir('resources/newimgs')][0]

card = im.get(f'resources/newimgs/{x}')

card = cv.get_card(card)

card.find_values(db.get_numbers(), db.get_symbols())

print(card)
