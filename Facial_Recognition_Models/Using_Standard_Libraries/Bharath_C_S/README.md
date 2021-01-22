## FACE RECOGNITION AND CLASSIFICATION

> This is a simple facial recognition and classification project where use facerecognition model to predict the face and label the image.The model looks through the faces folder and encodes all the faces and 
return: dict of (name, image encoded). Then the input image is passed through the classify method where will find all of the faces in a given image and label them if it knows what they are and else name it as unknown. Face locations are encoded with the facencoding and compared with both the train and test image. If both are equal it classify the image along with the label else it labels it as unknown

##
## Demo of the Project is [here](https://drive.google.com/drive/folders/1zOBI7Bc-UlUY1HoM-CdxgGB-KlFZt0Hb?usp=sharing)

## The image used for training

![](./faces/Bharath%20C%20S.jpg)


## The image given input for classification
![](./test1.PNG)


## The output image with label
![](./output_face_rec.PNG)