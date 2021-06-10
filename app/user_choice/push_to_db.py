import numpy as np
import cv2 as cv
import os 
import database.database as db
from imgstf import core
from imgstf import edge

TOP = True 
BOTTOM = False

def get_images():
    images = os.listdir('/home/thomas/Skrivebord/Mapper/OpenCV/cdio-api/images')

    return [cv.imread(f'/home/thomas/Skrivebord/Mapper/OpenCV/cdio-api/images/{x}') for x in images]

def rotate_images(images):
    images = [np.rot90(x) for x in images]
    return images

def user_validate_image(image, cornor_part):
    image = core.find_card(image)

    image = edge.resize(image)

    cv.imshow('test',image)
    cv.waitKey(0)

    cornor = core.extractCornor(image)

    part = cornor[0] if cornor_part else cornor[1]

    if input('Press Y if ok else N').lower() != 'y':
            return None

    return part

def identify_image(cornor_part):
    value = input('Write the input value')

    choices = ['A','2','3','4','5','6','7','8','9','10','J','Q','K'] if cornor_part else ['S','K','D','H']

    if value not in choices:
        return None

    return value

def database():
    images = get_images()
    images = rotate_images(images)

    cornor_part = TOP

    for image in images:

        cv.imshow('test',image)
        cv.waitKey(0)
        
        part = user_validate_image(image,cornor_part) 

        print(part)

        if not part:
            continue

        value = identify_image(cornor_part)

        if not value:
            continue

        if cornor_part == TOP:
            db.save_number(part,value)
        else:
            db.save_symbol(part,value)