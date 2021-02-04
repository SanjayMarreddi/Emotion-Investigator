import face_recognition as fr
import cv2 as cv
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os

Tk().withdraw
loadimg = askopenfilename()

targetimg = fr.load_image_file(loadimg)
targetencode = fr.face_encodings(targetimg)

##Training the model by providing the images
def encodeface(images):
    list_people = []

    for files in os.listdir(images):
        knownimg = fr.load_image_file(f'{images}{files}')
        knownencode = fr.face_encodings(knownimg)[0]

        list_people.append((knownencode, files))

    return list_people

##This function takes the image provided by the user and compares with the trained models
def find_target():
    face_location = fr.face_locations(targetimg)

    for people in encodeface("./data_img"):
        encodedface = people[0]
        files = people[1]


        is_target = fr.compare_faces(encodedface, targetencode, tolerance = 0.55)

        print(f'{is_target} {files}')

        if face_location:
            faceid = 0
            for location in face_location:
                if is_target(faceid):
                   label = files
                   create_frame(location, label)

                faceid += 1



## Here the rectangles around the faces is created
def create_frame(location, label):
    top, right, bottom, left = location
    cv.rectangle(targetimg, (left,top), (right,bottom), (255, 0, 0), 2)
    cv.rectangle(targetimg, (left,bottom + 20), (right,bottom), (255, 0, 0), cv.FILLED)
    cv.putText(targetimg, label, (left + 3, bottom + 14), cv.FONT_HERSHEY_COMPLEX, 0.4, (255, 255, 255), 1)

## It shows the recognized image with label
def renderimg():
    rgb_img = cv.cvtColor(targetimg, cv.COLOR_BGR2RGB)
    cv.imshow('Face Recognition', rgb_img)
    cv.waitKey(0)

find_target()
renderimg()
            