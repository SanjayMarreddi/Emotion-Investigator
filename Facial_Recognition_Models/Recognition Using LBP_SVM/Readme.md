## Overview
    Face detection and recognition using LBP features and Support Vector Machine.
    This model first creates the rectangle and crop the facial area from image then extracts LBP features from image and pass it through SVM.

## Dependencies
    pip install numpy
    pip install opencv-python
    pip install sklearn
    pip install skimage
    
    
## Quick Start
    1] git clone https://github.com/SanjayMarreddi/Facial-Expression-Recognition-Classifier-Model.git
    2] cd Facial-Expression-Recognition-Classifier-Model
       cd Facial_Recognition_Models
       cd 'Recognition Using LBP_SVM'
    
    -->To collect live data run below command
    3] python create_dataset.py
      (First it will ask your name and then after it will take your 100 snapshots. You can press 'Esc' to exit)
    
    -->After data collection, run below command to train model and recognising images using webcam.
    4] python model.py
    
   
## Snapshots 

![prediction_1](https://user-images.githubusercontent.com/43903254/107783286-1883fd00-6d70-11eb-85f1-dbd71829822e.png)
![prediction_2](https://user-images.githubusercontent.com/43903254/107783306-1e79de00-6d70-11eb-9146-2f93b5eb3977.png)
    
   
