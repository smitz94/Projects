# DENOISING THE IMAGE USING AUTOENCODER(CNN) (DEEP LEARNING)


### PROBLEM STATEMENT : 
Take an image that has noise in it and train an autoencoder neural network to produce clean image removing the noise.

_Language used_ : **Python**

_Library used_ : **[numpy](https://numpy.org/)**,**[matplotlib](https://matplotlib.org/)** 
and **[tensorflow-keras](https://www.tensorflow.org/guide/keras)**

_Models used_ : Convolutional Neural Network


### CODE EXPLATION [AUTOENCODER(CNN).IPYNB](https://github.com/smitz94/Projects/blob/master/Denoising%20the%20image%20using%20Autoencoder(CNN)/autoencoder(CNN).ipynb)
* Create clean images of circles at different positions and different radius in a 64*64 size of space.

* Add noise to these images and save them in a seperate sample.

* Train the neural network with Input(Predictor):noisy image and Output(Response): Corresponding clean image.

* Test and Predict on the noisy image and let neural network produce the output.

### RESULTS

> **SAMPLE IMAGE OF CIRCLE**

![](https://github.com/smitz94/Projects/blob/master/Denoising%20the%20image%20using%20Autoencoder(CNN)/sample_circle.png)

> **SAMPLE NOISY IMAGE**

![](https://github.com/smitz94/Projects/blob/master/Denoising%20the%20image%20using%20Autoencoder(CNN)/sample_noise.png)

> **OUTPUT IMAGES**

![](https://github.com/smitz94/Projects/blob/master/Denoising%20the%20image%20using%20Autoencoder(CNN)/output.png)

### CONCLUSION

* Output from the network is not the cleanest image but the network learnt the important feature even fromt the noisy inputs.

* It learnt features like where is the circle located, its radius and its colour contrast. 

* With more training and changing the hyperparameters clean output image can be obtained.
