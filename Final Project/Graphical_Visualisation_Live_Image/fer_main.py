# First let us import required Functions from FLASK
from flask import Flask, render_template, Response,request

# From the module "camera" let us import the VideoCamera Class
from fer_camera import VideoCamera

# From the module "fer_Graphical_Visualisation" let us import the Emotion_Analysis Function
from fer_Graphical_Visualisation import Emotion_Analysis

# Import the Random Module 
import random

# Import the OpenCV
import cv2

# Let us Instantiate the app 
app = Flask(__name__)

# Defining the route for Home Page
@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


# Defining the route for Taking Video Feed
@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


# Defining thr route fot Capturing an Image from WebCam
@app.route('/capture')
def index1():
    """Video streaming home page."""
    return render_template('index1.html')


# Takes Image from WebCam and saves it
@app.route('/takeimage', methods = ['POST'])
def takeimage():
    name = request.form['name']
    print(name)
    v = VideoCamera()
    _, frame = v.video.read()
    save_to ="C:/Users/Swetha/Desktop/Sanjay/Technocolabs/Project/static/"
    cv2.imwrite(save_to + str(name) + ".jpg" , frame) 
    return Response(status=200)



# Defining the route for Graphical Visualization
@app.route("/visual",methods = ['POST',"GET"])
def visual():
    result = Emotion_Analysis("predict.jpg" )
    return render_template('visual.html', orig = result[0], pred = result[1], bar=result[2])



if __name__ == '__main__':
    app.run(debug=True)
