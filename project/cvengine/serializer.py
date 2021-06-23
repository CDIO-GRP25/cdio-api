# GRUPPE 21
import io
import cv2 as cv
import numpy as np

def show(img):
    '''shows image'''
    cv.imshow('hej', img)
    return cv.waitKey(0)

def get(path):
    '''loads image from path'''
    return cv.cvtColor(cv.imread(path),cv.COLOR_BGR2RGB)

def load(file):
    '''Loads image from byearray'''
    img = np.asarray(bytearray(file.read()), dtype="uint8")
    return cv.imdecode(img, cv.IMREAD_COLOR)

def save(img):
    '''returns image as byte array'''
    is_success, buffer = cv.imencode(".jpg", img)
    return io.BytesIO(buffer)
