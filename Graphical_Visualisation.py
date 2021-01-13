# Let us import the Libraries required.
import cv2
import numpy as np
import matplotlib.pyplot as plt

from model import FacialExpressionModel

# Creating an instance of the class with the parameters as model and its weights.
test_model = FacialExpressionModel("model.json", "model_weights.h5")

# Loading the classifier from the file.
facec = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


def Emotion_Analysis(img):
    """ It does prediction of Emotions found in the Image provided, does the 
    Graphical visualisation, saves as Images and returns them """

    # Read the Image through OpenCv's imread()
    path = "static/" + str(img)
    image = cv2.imread(path)

    # Convert the Image into Gray Scale
    gray_frame = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Image size is reduced by 30% at each image scale.
    scaleFactor = 1.3

    # 5 neighbors should be present for each rectangle to be retained.
    minNeighbors = 5

    # Detect the Faces in the given Image and store it in faces.
    faces = facec.detectMultiScale(gray_frame, scaleFactor, minNeighbors)

    # When Classifier could not detect any Face.
    if len(faces) == 0:
        return [img]

    for (x, y, w, h) in faces:

        # Taking the Face part in the Image as Region of Interest.
        roi = gray_frame[y:y+h, x:x+w]

        # Let us resize the Image accordingly to use pretrained model.
        roi = cv2.resize(roi, (48, 48))

        # Let us make the Prediction of Emotion present in the Image
        prediction = test_model.predict_emotion(
            roi[np.newaxis, :, :, np.newaxis])

        # Custom Symbols to print with text of emotion.
        Symbols = {"Happy": ":)", "Sad": ":}", "Surprise": "!!",
                   "Angry": "?", "Disgust": "#", "Neutral": ".", "Fear": "~"}
    

        ## based on the prediction recommend music


        # Defining the Parameters for putting Text on Image
        Text = str(prediction) + Symbols[str(prediction)]
        Text_Color = (180, 105, 255)

        Thickness = 2
        Font_Scale = 1
        Font_Type = cv2.FONT_HERSHEY_SIMPLEX

        # Inserting the Text on Image
        cv2.putText(image, Text, (x, y), Font_Type,
                    Font_Scale, Text_Color, Thickness)

        # Finding the Coordinates and Radius of Circle
        xc = int((x + x+w)/2)
        yc = int((y + y+h)/2)
        radius = int(w/2)

        # Drawing the Circle on the Image
        cv2.circle(image, (xc, yc), radius, (0, 255, 0), Thickness)

        # Saving the Predicted Image
        path = "static/" + "pred" + str(img)
        cv2.imwrite(path, image)

        # List of Emotions
        EMOTIONS = ["Angry", "Disgust",
                    "Fear", "Happy",
                    "Neutral", "Sad",
                    "Surprise"]

        # Finding the Probability of each Emotion
        preds = test_model.return_probabs(roi[np.newaxis, :, :, np.newaxis])

        # Converting the array into list
        data = preds.tolist()[0]

        # Initializing the Figure for Bar Graph
        fig = plt.figure(figsize=(8, 5))

        # Creating the bar plot
        plt.bar(EMOTIONS, data, color='green',
                width=0.4)

        # Labelling the axes and title
        plt.xlabel("Types of Emotions")
        plt.ylabel("Probability")
        plt.title("Facial Emotion Recognition")

        # Saving the Bar Plot
        path = "static/" + "bar_plot" + str(img)
        plt.savefig(path)
       
    # Returns a list containing the names of Original, Predicted, Bar Plot Images
    return ([img, "pred" + img, "bar_plot" + img, prediction])
