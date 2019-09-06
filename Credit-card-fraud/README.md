# CREDIT-CARD FRAUD DETECTION (MACHINE LEARNING)


### PROBLEM STATEMENT : 
Analyze and compare different Machine Learning Models for Credit-card Fraud detection.

_Language used_ : **Python**

_Library used_ : **[pandas](https://pandas.pydata.org/)**,**[numpy](https://numpy.org/)**,**[sklearn](https://scikit-learn.org/)**,
**[matplotlib](https://matplotlib.org/)** and **[imblearn](https://imbalanced-learn.readthedocs.io/en/stable/api.html)**

_Models used_ : **[Linear Regression](https://towardsdatascience.com/linear-regression-detailed-view-ea73175f6e86)**, 
**[K Nearest Neighbours](https://towardsdatascience.com/machine-learning-basics-with-the-k-nearest-neighbors-algorithm-6a6e71d01761)** and
**[Random Forest](https://towardsdatascience.com/understanding-random-forest-58381e0602d2)**


### CODE EXPLATION [CREDIT_CARD_FRAUD_DETECTION.PY](https://github.com/smitz94/Projects/blob/master/Credit-card-fraud/credit_card_fraud_detection.py)
* Seperate Target and Training data in the ratio 75:25.

* Apply SMOTE to oversample the data to equalize the minority and majority classes.

* Call the described models to train the data and predict the output.

* Compute confusion matrix, accuracy, precision, recall, ROC and AUC for each described Model and plot them to analyze.

### RESULTS

> **LINEAR REGRESSION**

![](https://github.com/smitz94/Projects/blob/master/Credit-card-fraud/Figure_1.png)

> **K NEAREST NEIGHBOURS**

![](https://github.com/smitz94/Projects/blob/master/Credit-card-fraud/Figure_2.png)

> **RANDOM FOREST**

![](https://github.com/smitz94/Projects/blob/master/Credit-card-fraud/Figure_3.png)

### CONCLUSION

Closer the AUC to 1 better the model's performance over the dataset. Hence, we can see Linear Regression and Random Forest model have close AUC. Therefore we can choose either of them. Here we can choose Random Forest.
