# First let us import required Functions from FLASK
from flask import Flask, render_template, Response

# From the module "camera" let us import the VideoCamera Class
from fer_camera_Manual_U import VideoCamera

# From the module "fer_Graphical_Visualisation" let us import the Emotion_Analysis Function
from fer_Graphical_Visualisation_Manual_U import Emotion_Analysis

# from flask_sqlalchemy import SQLALCHEMY_

# Import the Random Module 
import random

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

# Defining the route for Graphical Visualization
@app.route("/visual")
def visual():
    # The images for testing
    pics=["test_1_sad.jpg","test_2_angry.jpg","test_3_happy.jpg"]
    result = Emotion_Analysis(random.choice(pics))
    return render_template('visual.html', orig = result[0], pred = result[1], bar=result[2])


if __name__ == '__main__':
    app.run(debug=True)
