# GRUPPE 21
from itertools import chain
from cv2 import bitwise_xor, imshow, waitKey
class CornerObject:
    def __init__(self, img, val=None):
        self.img = img
        self.val = val

    def __str__(self):
        return self.val

    def find_value(self, others):
        self.val = min(others, key=self.difference)

    def difference(self, other):
        return len([x for sub
            in bitwise_xor(self.img, other.img)
            for x in sub
            if x == 1]))
