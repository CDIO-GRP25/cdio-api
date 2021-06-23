# GRUPPE 21
import cv2 as cv
import numpy as np
import imutils as util
from .cornerfinder import CornerFinder
from models.cardobject import Card, EmptyCard

class CardFinder:
    def __init__(self):
        self.corner_finder = CornerFinder()


    def find(self, img):
        '''finds a single card on an image with a single card'''
        gray        = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        _, thresh   = cv.threshold(gray, 140, 255, cv.THRESH_BINARY)

        contours    = cv.findContours(
                image=thresh.copy(),
                mode=cv.RETR_TREE,
                method=cv.CHAIN_APPROX_NONE)
        contours    = util.grab_contours(contours)
        contours    = sorted(contours,key=cv.contourArea,reverse=True)[:5]

        card        = self.__get_card(contours, img)
        return self.__create_card_object(card)


    def __create_card_object(self, card):
        '''returns the card object'''
        if card is None:
            return EmptyCard()
        try:
            num, sym = self.corner_finder.find(card)
            return Card(card, num, sym)
        except Exception as e:
            print(e)
            return EmptyCard()


    def __get_card(self, contours, img):
        '''looks for and possible cards in the found contours'''
        def is_card(aprox): return len(aprox) == 4
        for cnt in contours:
            aprox = self.__get_aprox(cnt)
            if is_card(aprox):
                return self.__extract_card(aprox, img)
        return None


    def __get_aprox(self, cnt):
        '''gets the square from the contour'''
        lnked = cv.arcLength(cnt,True)
        return cv.approxPolyDP(cnt,0.02*lnked,True)


    def __extract_card(self, aprox,img):
        '''warps the found card into perspective'''
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

