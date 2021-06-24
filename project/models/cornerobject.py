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
        lowest = 100
        out = ''
        for obj in others:
            r = self.check_similarity(obj)
            if r < lowest:
                lowest = r
                out = obj.val
        self.val = out

    def check_similarity(self, other):
        xor = bitwise_xor(self.img, other.img)
        return len([x for sub in xor for x in sub if x == 1])
