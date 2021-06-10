import cv2 as cv
from imutils.convenience import rotate
import numpy as np
import imutils as util
from numpy.lib.type_check import imag
import skimage.exposure
from imgstf import edge

#TODO make this object oriented

def extractCard(aprox,img):
    pts1 = aprox.reshape(4, 2)
    rect = np.zeros((4, 2), dtype="float32") 
    s = pts1.sum(axis=1)
    rect[0] = pts1[np.argmin(s)]
    rect[3] = pts1[np.argmax(s)]

    diff = np.diff(pts1, axis=1)
    rect[1] = pts1[np.argmin(diff)] 
    rect[2] = pts1[np.argmax(diff)]

    pts2 = np.float32([[0, 0], [200, 0], [0, 300], [200, 300]])
    matrix = cv.getPerspectiveTransform(rect, pts2)
    result = cv.warpPerspective(img, matrix, (200, 300))
    return result
    

def extractCornor(card):
    cornor = card[0:80,0:30]
    top = cornor[:40]
    bot = cornor[40:]
    cornor = cv.cvtColor(cornor,cv.COLOR_RGB2GRAY)
    _, cornor = cv.threshold(cornor, 0, 255, cv.THRESH_OTSU | cv.THRESH_BINARY_INV)

    top = cornor[:40]
    bottom = cornor[40:]

    return top, bottom


def find_card(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = cv.subtract(255,gray)
    ret,thresh = cv.threshold(gray,150,255,cv.THRESH_TOZERO)
    kernel1 = cv.getStructuringElement(cv.MORPH_ELLIPSE,(3,3))
    kernel2 = np.ones((3,3),np.uint8)
    erosion = cv.erode(thresh,kernel2,iterations = 1)
    dilation = cv.dilate(erosion,kernel1,iterations = 1)
    see = cv.findContours(dilation.copy(),cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
    see = util.grab_contours(see)
    see = sorted(see,key=cv.contourArea,reverse=True)[:3]
    for s in see:
        lnked = cv.arcLength(s,True)
        aprox = cv.approxPolyDP(s,0.02*lnked,True)
        if len(aprox) == 4:
            print('found card')
            return extractCard(aprox,img)


def splitstuff(img):
    w = 560
    h = 800
    b = 15
    cards = [img[b+i*h:b+i*h+h,b+j*w:b+j*w+w] 
            for i in range(2) 
            for j in range(7)]

    cards = [find_card(x) 
            for x in cards[:8] + cards[10:]]

    return [extractCornor(x) 
            for x in cards]

def rotate_images(image):
    image = np.rot90(image)
    return image

def test_func():
    image = cv.imread('/home/thomas/Skrivebord/Mapper/OpenCV/cdio-api/images/20210609_161353.jpg')

    image = edge.resize(image)

    image = rotate_images(image)

    cv.imshow('hej',image)
    cv.waitKey(0)

    image = find_card(image)