# First let us import required Functions from FLASK
from flask import Flask, render_template, Response

# From the module "camera" let us import the VideoCamera Class
from fer_camera import VideoCamera

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


if __name__ == '__main__':
    app.run(debug=True)
