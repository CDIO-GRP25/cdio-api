# GRUPPE 21
import unittest
import cv2 as cv
from app.imgstf import core
import uuid

class TestOpenCVCore(unittest.TestCase):
    def test_find_card(self):
        img = cv.imread(f'res/ace.jpg')
        card = core.findCard(img)
        cv.imshow(f'{uuid.uuid4()} card', card)
        cornor = core.extractCornor(card)
        cv.imshow(f'{uuid.uuid4()} corner', cornor)
        cv.waitKey()
        cv.destroyAllWindows()


#class TestCompareTwoCards(unittest.TestCase):
#    def testCompare():
#        for path in os.listdir('resources'):
#            img = cv.imread(f'resources/{path}')
#            card = findCard(img)
#            if card is not None:
#                corner = extractCornor(card)
#                compareImg(corner)
#                done()
#

