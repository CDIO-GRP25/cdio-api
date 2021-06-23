# GRUPPE 21
import requests
import cv2 as cv

#Upload image
url = 'http://localhost:8000/upload'
files= {'file': ('image.jpg',open('ace.jpg', 'rb'),'image/jpg',)}
r = requests.post(url, files=files)
print(r.text)
