#  Facial Emotion Investigator :

<img src=https://www.apa.org/images/PSA-2011-05-matsumoto-fig1_tcm7-115934_w1024_n.jpg height="200">

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
![GitHub contributors](https://img.shields.io/github/contributors-anon/SanjayMarreddi/Facial-Expression-Recognition-Classifier-Model?style=social)
![GitHub forks](https://img.shields.io/github/forks/SanjayMarreddi/Facial-Expression-Recognition-Classifier-Model?style=social)
![GitHub Repo stars](https://img.shields.io/github/stars/SanjayMarreddi/Facial-Expression-Recognition-Classifier-Model?style=social)
![GitHub Repo Issues](https://img.shields.io/github/issues/SanjayMarreddi/Facial-Expression-Recognition-Classifier-Model?style=social)
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

## :sunglasses:  About The Project: :point_down:

# Facial Expression Recognition Classifier Model :

Facial expression for emotion detection has always been an easy task for humans, but achieving the same task with a computer algorithm is quite challenging. With the recent advancement in computer vision and machine learning, it is possible to detect emotions from images.In this project,we propose a novel technique called facial emotion recognition using convolutional neural networks,python and flask. Facial expressions are the vital identifiers for human feelings, because it corresponds to the emotions. Most of the times (roughly in 55% cases), the facial expression is a nonverbal way of emotional expression, and it can be considered as concrete evidence to uncover whether an individual is speaking the truth or not.

Our Facial Expression Recognition Classifier Model takes **Real-time Video input** and predicts the **Emotion of users** present in front of Webcam. It also gives **Graphical Visualization** of Expressions when we feed in an
Image via WebCam or manually! like mentioned in the photo below:

<img src="https://miro.medium.com/max/1864/1*oURfHMP1--ttXnDx0heusg.png">


## :loop: Tech Stack used :point_down:
- Python
- Flask
- HTML, CSS
- Deep Learning (CNN)

## :golf: Predictions done by Model :point_down:
<img width="896" alt="sad" src="https://user-images.githubusercontent.com/57671048/98131077-f103d580-1ee0-11eb-9dc3-905f3884ee1b.png">
<img width="897" alt="angry" src="https://user-images.githubusercontent.com/57671048/98131265-1e508380-1ee1-11eb-92b5-12c7677c08c0.png">
<img width="884" alt="happy" src="https://user-images.githubusercontent.com/57671048/98131204-10026780-1ee1-11eb-999b-0182a68ce529.png">
Predictions On Live Image :point_down:
<img width="891" alt="nuetral" src="https://user-images.githubusercontent.com/57671048/98197451-c8192a00-1f4c-11eb-8b9f-e752acce1127.png">




## :boom: Getting Started: Steps to run the Project in your local device !!
- Fork this repository.
- Clone the repository to your System using `git clone`
- Example : `git clone https://github.com<your-github-username>/Facial-Expression-Recognition-Classifier-Model`
- Open any **Python** IDE and run the `main.py` file. 

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

## Steps to Contribute to this Project ! :point_down:
**Go through the link If you are new to Open Source Contribution [here](https://github.com/firstcontributions/first-contributions) on making your First Contribution !!**
- Fork this repository
- Clone the repository to your System using `git clone https://github.com<your-github-username>/Facial-Expression-Recognition-Classifier-Model`
- Create a branch :-
   - Change to the repository directory on your computer `cd Facial-Expression-Recognition-Classifier-Model`
   - Now create a branch using the git checkout command: `git checkout -b your-new-branch-name`
- Make changes as per your requirement to solve the Issues mentioned in the `Future scope of the Project` and commit those changes.
- If you go to the project directory and execute the command git status, you'll see there are changes. Add those changes to the branch you just created using the `git add`
- Now commit those changes using the git commit command: `git commit -m "Added the feature of Suggesting Music"`
- Push your changes to GitHub using the command `git push origin <add-your-branch-name>`
- If you go to your repository on GitHub, you'll see a Compare & pull request button. Click on that button.
- Now describe the changes you made and submit the `pull request`.
- Wait for the Maintainers to review :)

### Excited to contribute to the Project ? Head over Open Issues [here](https://github.com/SanjayMarreddi/Facial-Expression-Recognition-Classifier-Model/issues)

## Project Admin :point_down:

<!-- If you click on the image it would take to your GitHub profile -->

[![](https://github.com/SanjayMarreddi.png?size=100)](https://github.com/SanjayMarreddi)

:fire: SanjayMarreddi

## Contributors :point_down:

<!-- If you click on the image it would take to your GitHub profile -->

[![](https://github.com/SanjayMarreddi.png?size=100)](https://github.com/SanjayMarreddi)
|:--:| 
| *SanjayMarreddi* |
[![](https://github.com/muthuannamalai12.png?size=100)](https://github.com/muthuannamalai12)
| *Muthu Annamalai* |

## Open Source Programs
This Project is part of the following programs :


**[DevScript Winter of Code](https://devscript.tech/woc/)**

<img src="https://user-images.githubusercontent.com/57671048/103410240-809bcc80-4b90-11eb-894c-6d3980d1c5d8.png" width="150" height="150">

## Code of Conduct

You can find our Code of Conduct [here](/CODE_OF_CONDUCT.md).

## License

This project follows the [MIT License](/LICENSE).


### Any type of Contributions via Pull Requests, Issues, Documentation, Code Review are always welcomed ! :tada:
