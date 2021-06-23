# GRUPPE 21
import cv2 as cv
import database.database as db
from . import core, dao

def testShowDB():
    #Wrong cards in database
    for card in db.get_all():
        cv.imshow('hej',card['image'])
        done()


def test():
    img = cv.imread(f'c.jpg')
    showCard(img)
    done()
    #img = cv.resize(img, (0, 0), fx=0.2, fy=0.2)
    card = findCard(img)
    return extractCornor(card)


def testUploads():
    corners = []
    for path in os.listdir('uploads'):
        corners.append(testSave(f'{path}'))
    for corner in corners:
        print('-'*40)
        compareImg(corner)


if __name__ == '__main__':
    test()

