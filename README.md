# :sunglasses: Facial Expression Recognition Classifier Model 

A Facial Expression Recognition Classifier Model that takes
**Real-time Video input** and predicts the **Emotion of users** present in front of
Webcam. It also gives **Graphical Visualization** of Expressions when we feed in an
Image via Web Cam or manually !

![images](https://user-images.githubusercontent.com/57671048/98015631-031f3e80-1e23-11eb-9adc-70fd489cc004.png)


## :computer: Coding Structure:

- Import the required Packages and Libraries.
- Data analysis and Creating Training and Validation Batches.
- Create a CNN using 4 Convolutional Layers including *Batch Normalization*,
*Activation*, *Max Pooling*, *Dropout* Layers followed by *Flatten* Layer, 2 Fully
*Connected dense* Layers and finally Dense Layer with *SoftMax* Activation
Function.
- Compile the model using `Adam` Optimizer and categorical cross entropy
loss function.
- Training the model for 15 epochs and then Evaluating the model as well as
saving the model Weights in `.h5` Values
- Saving the model as `JSON` string.
- Creating a Class in a separate file to reload the model and its weights to
make predictions and return the probabilities of each emotion.
- Creating one more class in a Separate file which takes in the `Real-time
Video input` and returns frames of Images with a Circle detecting the face
and putting text of its emotion on it.
- A python script is also created which upon running yields the `Graphical`
`Visualization` of Emotions present in the Image provided.
- Finally creating a file which inherits form all the Classes defined by us and
deploys our application using *Flask*.


## :loop: Tech Stack used 
- Deep Learning Techniques : Convolutional Nueral Networks (CNN)
- Python
- Flask



## :golf: Predictions done by Model 

![Sad](https://github.com/SanjayMarreddi/Facial-Expression-Recognition-Classifier-Model/blob/master/Final%20Project/Predictions/sad.png)

![Angry](https://github.com/SanjayMarreddi/Facial-Expression-Recognition-Classifier-Model/blob/master/Final%20Project/Predictions/angry.png)

![Happy](https://github.com/SanjayMarreddi/Facial-Expression-Recognition-Classifier-Model/blob/master/Final%20Project/Predictions/happy.png)

## :boom: Steps to run the Project in your local device !!
- Fork this repository.
- Clone the repository to your System using `git clone`
- Example : `git clone https://github.com<your-github-username>/Facial-Expression-Recognition-Classifier-Model`
- Open any **Python** IDE and run the `fer_main.py` file !

## :innocent: We can further improve the Validation Accuracy of the model by tuning the hyperparameters like:
- Learning Rate
- Epochs
- Batch Size
- Number of Layers in CNN
- Number of filters
- Size of filters
- Value in Dropout Layers
- Optimizers

## Any Suggestions, Pull Requests, Issues are welcomed ! :tada:
