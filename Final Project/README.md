# Facial Expression Recognition Classifier Model

A Facial Expression Recognition Classifier Model that takes
Real-time Video input and predicts the Emotion of users present in front of
Webcam. It also gives Graphical Visualization of Expressions when we feed in an
Image.

## Coding Structure:

➢ Import the required Packages and Libraries.
➢ Data analysis and Creating Training and Validation Batches.
➢ Create a CNN using 4 Convolutional Layers including Batch Normalization,
Activation, Max Pooling, Dropout Layers followed by Flatten Layer ,2 Fully
Connected dense Layers and finally Dense Layer with SoftMax Activation
Function.
➢ Compile the model using Adam Optimizer and categorical cross entropy
loss function.
➢ Training the model for 15 epochs and then Evaluating the model as well as
saving the model Weights in .h5 Values
➢ Saving the model as JSON string.
➢ Creating a Class in a separate file to reload the model and its weights to
make predictions and return the probabilities of each emotion.
➢ Creating one more class in a Separate file which takes in the Real-time
Video input and returns frames of Images with a Circle detecting the face
and putting text of its emotion on it.
➢ A python script is also created which upon running yields the Graphical
Visualization of Emotions present in the Image provided.
➢ Finally creating a file which inherits form all the Classes defined by us and
deploys our application using Flask.
