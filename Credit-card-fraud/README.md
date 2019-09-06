# CREDIT-CARD FRAUD DETECTION (MACHINE LEARNING)


### PROBLEM STATEMENT : 
Analyze and compare different Machine Learning Models for Credit-card Fraud detection.

_Language used_ : **Python**

_Library used_ : **[pandas](https://pandas.pydata.org/)**,**[numpy](https://numpy.org/),**[sklearn](https://scikit-learn.org/)**,
**[matplotlib](https://matplotlib.org/)** and **[imblearn](https://imbalanced-learn.readthedocs.io/en/stable/api.html)**

_Models used_ : **[Linear Regression](https://towardsdatascience.com/linear-regression-detailed-view-ea73175f6e86)**, 
**[K Nearest Neighbours](https://towardsdatascience.com/machine-learning-basics-with-the-k-nearest-neighbors-algorithm-6a6e71d01761)** and
**[Random Forest](https://towardsdatascience.com/understanding-random-forest-58381e0602d2)**


### CODE EXPLATION [CREDIT_CARD_FRAUD_DETECTION.PY](https://github.com/smitz94/Projects/blob/master/Credit-card-fraud/credit_card_fraud_detection.py)
* Open the desired image for analysis.

* Threshold the Input image to [HSV space](https://en.wikipedia.org/wiki/HSL_and_HSV), as it has the desirable property 
that allows us to identify a particular color using a single value, the **hue**, instead of three values. 

* Combine the two threshold images i.e low range and high range images.

* Apply Hough Transform to detect circles in the image and patch the red color and circles together.

### RESULTS

> Input: [Input 1](https://github.com/smitz94/Projects/blob/master/Detect%20only%20Red%20circles%20in%20a%20given%20Image/Images/all_circles.png)

![](https://github.com/smitz94/Projects/blob/master/Detect%20only%20Red%20circles%20in%20a%20given%20Image/Images/result1.png)

> Input: [Input 2](https://github.com/smitz94/Projects/blob/master/Detect%20only%20Red%20circles%20in%20a%20given%20Image/Images/all_red.png)

![](https://github.com/smitz94/Projects/blob/master/Detect%20only%20Red%20circles%20in%20a%20given%20Image/Images/result2.png)

> Input: [Input 3](https://github.com/smitz94/Projects/blob/master/Detect%20only%20Red%20circles%20in%20a%20given%20Image/Images/diff_shapes.png)

![](https://github.com/smitz94/Projects/blob/master/Detect%20only%20Red%20circles%20in%20a%20given%20Image/Images/result3.png)
