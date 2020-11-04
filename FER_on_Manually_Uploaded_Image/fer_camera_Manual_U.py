# Let us import the Libraries required.
import cv2
import numpy as np


# From Module named "model", Let us import the FacialExpressionModel class.
from fer_model_Manual_U import FacialExpressionModel

# Creating an instance of the class with the parameters as model and its weights.
model = FacialExpressionModel("fer_model.json", "fer_model_weights.h5")
facec = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Let us define a Class for taking the Real time Video and Predicting the Emotion using our model

class VideoCamera(object):
    
    # Whenever we create an instance of class, video variable is created and its starts taking the Video
    # using System's Default Web Cam
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    # Let us define a function that returns camera frames along with bounding boxes and predictions
    def get_frame(self):

        # Reading the Video and grasping the Frames
        _, fr = self.video.read()

        # Converting the Color image to Gray Scale 
        gray_fr = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)

        # Detect the Faces in the given Image and store it in faces.
        faces = facec.detectMultiScale(gray_fr, 1.3, 5)
        
        # Iterating through all the faces detected
        for (x, y, w, h) in faces:
            
            # Taking the Face part in the Image
            fc = gray_fr[y:y+h, x:x+w]
            
            # Let us resize the Image and store it as Region of Interest(roi) 
            roi = cv2.resize(fc, (48, 48))

            # Let us make the Prediction of Emotion present in the Image
            pred = model.predict_emotion(roi[np.newaxis, :, :, np.newaxis])

            # Let us define text and its Font style that is to be written on Image
            sym={"Happy":":)","Sad":":}","Surprise":"!!","Angry":"?","Disgust":"#","Neutral":".","Fear":"~"}
            text=  str(pred) +  sym[str(pred)] 
            font = cv2.FONT_HERSHEY_SIMPLEX
            
            # Inserting the Text on Image
            cv2.putText(fr,text, (x, y), font, 1, (180,105,255), 2)
            
            # Finding the Coordinates and Radius of Circle
            xc = (x + x+w)/2
            yc = (y + y+h)/2
            radius = w/2 # or h/2

            # Drawing the Circle on the Image
            cv2.circle(fr, (int(xc),int(yc)), int(radius), (0,255,0), 2)
           
        # Encoding the Image into a memory buffer
        _, jpeg = cv2.imencode('.jpg', fr)

        # Returning the Image
        return jpeg.tobytes()


