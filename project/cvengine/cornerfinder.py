# GRUPPE 21
import cv2 as cv
import numpy as np

class CornerFinder:
    '''
    CornerFinder is a private class only used by the CardFinder class to find
    the number and the symbol on the card.
    '''
    def __init__(self):
        pass


    def find(self, card):
        '''finds the number and the symbol of a card'''
        corner  = card[0:80,0:30]
        num     = self.__strip_margin(corner[:45])
        sym     = self.__strip_margin(corner[40:])
        return num, sym


    def __strip_margin(self, img):
        '''returns the final 10x10 image of object without margin'''
        gray        = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        blur        = cv.GaussianBlur(gray,(5,5),0)
        thresh      = cv.adaptiveThreshold(blur,255,1,1,11,2)
        contours,_  = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
        dimensions  = self.__get_dimensions(contours)
        self.__draw_contours_on_image(img, dimensions)
        objects     = self.__get_objects(gray, dimensions)
        return self.__get_final_object(objects)


    def __get_final_object(self, objects):
        '''checks and handles if more than one number is found eg. 10'''
        if len(objects) == 2:
            a,b = objects
            return cv.resize(np.hstack((b,a)),(10,10))
        return objects[0]


    def __get_dimensions(self, contours):
        '''returns a list of dimensions for contours larger than 50'''
        return [cv.boundingRect(cnt)
            for cnt
            in contours
            if cv.contourArea(cnt) > 50]


    def __get_objects(self, img, dimensions):
        '''returns a list objects higher than 20'''
        return [self.__get_object(img, (x,y,w,h))
            for [x,y,w,h]
            in dimensions
            if h>20]


    def __draw_contours_on_image(self, img, dimensions):
        '''used to draw the lines around the objects on the original image'''
        for [x,y,w,h] in dimensions:
            if h>20: cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)


    def __get_object(self, img, dim):
        '''returns a black/white 10x10 image of the object'''
        [x, y, w, h] = dim
        out = cv.resize(img[y:y+h,x:x+w],(10,10))
        _, out = cv.threshold(out, 0, 255, cv.THRESH_OTSU | cv.THRESH_BINARY_INV)
        return out
