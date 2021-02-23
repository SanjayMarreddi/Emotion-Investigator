# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 15:12:17 2021

"""

#Importing Packages
import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import tensorflow as tf
global graph
graph = tf.get_default_graph()
from flask import Flask , request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

#Loading the dataset
app = Flask(__name__)
model = load_model("celeb.h5")

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/predict',methods = ['GET','POST'])
def upload():
    if request.method == 'POST':
        f = request.files['image']
        print("current path")
        basepath = os.path.dirname(__file__)
        print("current path", basepath)
        filepath = os.path.join(basepath,'uploads',f.filename)
        print("upload folder is ", filepath)
        f.save(filepath)
        
        img = image.load_img(filepath,target_size = (64,64))
        x = image.img_to_array(img)
        x = np.expand_dims(x,axis =0)
        
        with graph.as_default():
            preds = model.predict_classes(x)
            4
            
            print("prediction",preds)
         #Model Prediction labels
        index = ['ben_afflek','etlon_john','jerry_seinfeld','madonna','mindy_kaling']
        
        text = "the predicted celebrity is : " + str(index[preds[0]])
        
    return text
if __name__ == '__main__':
    app.run(debug = True)
        
        
        
    
    
    