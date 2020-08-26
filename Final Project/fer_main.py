# First let us import required Functions from FLASK
from flask import Flask, render_template, Response

# From the module "camera" let us import the VideoCamera Class
from fer_camera import VideoCamera

# From the module "fer_Graphical_Visualisation" let us import the Emotion_Analysis Function
from fer_Graphical_Visualisation import Emotion_Analysis

# from flask_sqlalchemy import SQLALCHEMY_

# Import the Random Module 
import random

# Let us Instantiate the app 
app = Flask(__name__)


# ENV ="prod"

# if ENV =="prod":
#     app.debug =False
#     app.config['SQLALCHEMY_DATABASE_URI'] =" postgres://hlzcifuyqjilsm:8efa9454fccd85c6d2e12cde062f59e9531505c7bce7aa0e81619828aaf88506@ec2-54-235-192-146.compute-1.amazonaws.com:5432/dfsna6ggbpq3rt"

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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
