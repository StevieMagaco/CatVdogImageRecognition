# CatVdogImageRecognition

This program was to enter the kaggle competition at: https://www.kaggle.com/c/dogs-vs-cats-redux-kernels-edition

The machine currently does what I intended it to do, which is to be able to somewhat identify if an image represents a dog or a cat.
There are a few things that can be fixed to make it better.
Currently this machine is using a breath first traversal to run through the data, which make it slow, very slow.
Switching to a greedy-best-first traversal would speed things up considerably and also provide more accurate results.
Also, switching from a .txt file to a .csv would alos improve it's performance.

This project was made by me, Stevie Magaco.

I used this as my research source: https://pythonprogramming.net/image-recognition-python/

###

The training samples and the numArEx.txt were removed becaused of their size.
The link for the training samples can be found on the Data section here:
https://www.kaggle.com/c/dogs-vs-cats-redux-kernels-edition

To generate numArEx.tx run CATvDogcreateExamples() function
