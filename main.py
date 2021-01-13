# Let us import the Libraries required.
import os
import cv2
import urllib
import numpy as np
from werkzeug.utils import secure_filename
from urllib.request import Request, urlopen
from flask import Flask, render_template, Response, request, redirect, flash, url_for

# Importing the required Classes/Functions from Modules defined.
from camera import VideoCamera
from Graphical_Visualisation import Emotion_Analysis

# Let us Instantiate the app
app = Flask(__name__)

###################################################################################
# We define some global parameters so that its easier for us to tweak when required.

# When serving files, we set the cache control max age to zero number of seconds
# for refreshing the Cache
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

###################################################################################
# Some Utility Functions

# Flask provides native support for streaming responses through the use of generator
# functions. A generator is a special function that can be interrupted and resumed.


def gen(camera):
    "" "Helps in Passing frames from Web Camera to server"""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def allowed_file(filename):
    """ Checks the file format when file is uploaded"""
    return ('.' in filename and
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS)


###################################################################################

def mood(result):
    if result=="Happy":
        return 'Since you are happy, lets keep up the good mood with some amazing music!'
    elif result=="Sad":
        return 'It seems that you are having a bad day, lets cheer you up with some amazing music!'
    elif result=="Disgust":
        return 'It seems something has got you feeling disgusted. Lets improve your mood with some great music!'
    elif result=="Neutral":
         return 'It seems like a normal day. Lets turn it into a great one with some amazing music!'
    elif result=="Fear":
        return 'You seem very scared. We are sure that some music will help!'
    elif result=="Angry":
        return 'You seem angry. Listening to some music will surely help you calm down!'
    elif result=="Surprise":
        return 'You seem surprised! Hopefully its some good news. Lets celebrate it with some great music!'

@app.route('/')
def Start():
    """ Renders the Home Page """

    return render_template('Start.html')


@app.route('/video_feed')
def video_feed():
    """ A route that returns a streamed response needs to return a Response object
    that is initialized with the generator function."""

    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/RealTime', methods=['POST'])
def RealTime():
    """ Video streaming (Real Time Image from WebCam Video) home page."""

    return render_template('RealTime.html')


@app.route('/takeimage', methods=['POST'])
def takeimage():
    """ Captures Images from WebCam, saves them, does Emotion Analysis & renders. """

    v = VideoCamera()
    _, frame = v.video.read()
    save_to = "static/"
    cv2.imwrite(save_to + "capture" + ".jpg", frame)

    result = Emotion_Analysis("capture.jpg")

    # When Classifier could not detect any Face.
    if len(result) == 1:
        return render_template('NoDetection.html', orig=result[0])

    sentence=mood(result[3])
    return render_template('Visual.html', orig=result[0], pred=result[1], bar=result[2],music=result[3],sentence=sentence)


@app.route('/ManualUpload', methods=['POST'])
def ManualUpload():
    """ Manual Uploading of Images via URL or Upload """

    return render_template('ManualUpload.html')


@app.route('/uploadimage', methods=['POST'])
def uploadimage():
    """ Loads Image from System, does Emotion Analysis & renders."""

    if request.method == 'POST':

        # Check if the post request has the file part
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

            # Pass it a filename and it will return a secure version of it.
            # The filename returned is an ASCII only string for maximum portability.
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            result = Emotion_Analysis(filename)

            # When Classifier could not detect any Face.
            if len(result) == 1:

                return render_template('NoDetection.html', orig=result[0])

            sentence=mood(result[3])
            return render_template('Visual.html', orig=result[0], pred=result[1], bar=result[2],music=result[3],sentence=sentence)


@app.route('/imageurl', methods=['POST'])
def imageurl():
    """ Fetches Image from URL Provided, does Emotion Analysis & renders."""

    # Fetch the Image from the Provided URL
    url = request.form['url']
    req = Request(url,
                  headers={'User-Agent': 'Mozilla/5.0'})

    # Reading, Encoding and Saving it to the static Folder
    webpage = urlopen(req).read()
    arr = np.asarray(bytearray(webpage), dtype=np.uint8)
    img = cv2.imdecode(arr, -1)
    save_to = "static/"
    cv2.imwrite(save_to + "url.jpg", img)

    result = Emotion_Analysis("url.jpg")

    # When Classifier could not detect any Face.
    if len(result) == 1:
        return render_template('NoDetection.html', orig=result[0])

    sentence=mood(result[3])

    return render_template('Visual.html', orig=result[0], pred=result[1], bar=result[2],music=result[3],sentence=sentence)


if __name__ == '__main__':
    app.run(debug=True)
