import cv2 as cv

def showCard(img):
    card = findCard(img)
    cv.imshow(f'{uuid.uuid4()} card', card)
    cornor = extractCornor(card)
    cv.imshow(f'{uuid.uuid4()} corner', cornor)


def done():
    cv.waitKey()
    cv.destroyAllWindows()


def testShowDB():
    #Wrong cards in database
    for card in db.get_all():
        cv.imshow('hej',card['image'])
        done()


def testCompare():
    for path in os.listdir('resources'):
        img = cv.imread(f'resources/{path}')
        card = findCard(img)
        if card is not None:
            corner = extractCornor(card)
            compareImg(corner)
            done()


def test():
    img = cv.imread(f'../ace.jpg')
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

