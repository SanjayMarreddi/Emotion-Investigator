# First let us import required Functions from FLASK
from flask import Flask, render_template, Response, request, redirect, flash, url_for
from werkzeug.utils import secure_filename

# From the module "camera" let us import the VideoCamera Class
from camera import VideoCamera

# From the module "Graphical_Visualisation" let us import the Emotion_Analysis Function
from Graphical_Visualisation import Emotion_Analysis

# Import the other important Libraries
import os
import cv2
import urllib
import numpy as np
from urllib.request import Request, urlopen


# Let us Instantiate the app
app = Flask(__name__)

# Refreshing the Cache
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

###############################################################################
# Some Utility Functions


def gen(camera):
    # Some Useful function for Video Feed

    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def allowed_file(filename):
    # Useful function for fetching Image form URL

    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

###############################################################################

# We define some global parameters so that its easier for us to tweak when required.


UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


###############################################################################

# Defining the route for Home Page
@app.route('/')
def Start():
    return render_template('Start.html')


# Defining the route for Taking Video Feed
@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


# Defining the route for Capturing an Real Time Image from WebCam Video Stream.
@app.route('/RealTime', methods=['POST'])
def RealTime():
    """Video streaming home page."""
    return render_template('RealTime.html')


# Defining the route for Taking Image from WebCam and saving it
@app.route('/takeimage', methods=['POST'])
def takeimage():
    v = VideoCamera()
    _, frame = v.video.read()
    save_to = "static/"
    cv2.imwrite(save_to + "capture" + ".jpg", frame)
    result = Emotion_Analysis("capture.jpg")
    return render_template('Visual.html', orig=result[0], pred=result[1], bar=result[2])


# Defining the route for Manual Uploading of Images
@app.route('/ManualUpload', methods=['POST'])
def ManualUpload():
    """Video streaming home page."""
    return render_template('ManualUpload.html')


# Defining the route for Manual Uploading of Images via UPLOAD from system
@app.route('/uploadimage', methods=['POST'])
def uploadimage():
    if request.method == 'POST':

        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']

        # If user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        # If user uploads the correct Image File
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # Start the Facial Expression Recognition
            result = Emotion_Analysis(filename)
            return render_template('visual.html', orig=result[0], pred=result[1], bar=result[2])


# Defining the route for Manual Uploading of Images via providing URL of Image
@app.route('/imageurl', methods=['POST'])
def imageurl():

    # Fetch the Image from the Provided URL
    url = request.form['url']
    req = Request(url,
                  headers={'User-Agent': 'Mozilla/5.0'})

    # Encoding and Saving it to the static Folder
    webpage = urlopen(req).read()
    arr = np.asarray(bytearray(webpage), dtype=np.uint8)
    img = cv2.imdecode(arr, -1)
    save_to = "static/"
    cv2.imwrite(save_to + "url.jpg", img)

    # Start the Facial Expression Recognition
    result = Emotion_Analysis("url.jpg")
    return render_template('Visual.html', orig=result[0], pred=result[1], bar=result[2])


if __name__ == '__main__':
    app.run(debug=True)
