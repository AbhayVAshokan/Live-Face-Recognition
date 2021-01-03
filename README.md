# Live-Face-Recognition

> Live training and recognition of faces using convolutional neural network.

`tkinter` library is used for creating the user interface for the project. 

During image generation, the head region of the new user is cropped using Haarcascade classifier. A Gaussian blur filter is applied and it is resized to 64x64. Finally the image is normalized bu dividing it with 255.

A custom CNN model is created with 2 convolution, 2 max-pooling and 3 dense layers due to limitations from the computational point of view for the training process. This model is used for face recognition during test.

#### Setup
```
pip install -r requirements.txt
```
