# GRUPPE 21
import cv2 as cv
import numpy as np
from models.gamestate import GameState
from .cardfinder import CardFinder

class CVEngine:
    def __init__(self):
        self.card_finder = CardFinder()


    def get_card(self, img):
        '''returns card object from image'''
        return self.card_finder.find(img)


    def gamestate_from_board(self, db, board_image):
        '''returns gamestate object from image of board'''
        imgs = self.__split_board(board_image)
        cards = [self.card_finder.find(img)
                for img
                in imgs]
        return GameState(db, cards)


    def __split_board(self, img):
        '''divides the board image into single card images'''
        def is_card_pos(i,j): return i!=1 or j!=1 and j!=2
        try:
            h,w,_ = img.shape
            w, h, = w//7, h//2
            return [img[i*h:i*h+h,j*w:j*w+w]
                    for i in range(2)
                    for j in range(7)
                    if is_card_pos(i,j)]
        except Exception as e:
            print(e)
            return None
