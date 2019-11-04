# ANOMALY DETECTION USING LSTM(RNN)


### PROBLEM STATEMENT : 
Detect **Collective Anomalies** in the real time data of AWS EC2 using LSTM.

_Language used_ : **Python**

_Library used_ : **[numpy](https://numpy.org/)**,**[matplotlib](https://matplotlib.org/)**,**[pandas](https://pandas.pydata.org/)**,
**[sklearn](https://scikit-learn.org/)**,**[imblearn](https://imbalanced-learn.readthedocs.io/en/stable/api.html)**
and **[tensorflow-keras](https://www.tensorflow.org/guide/keras)**

_Models used_ : Long Short Term Memory(LSTM)- Recurrent Neural Network


### CODE EXPLATION [LSTM.IPYNB](https://github.com/smitz94/Projects/blob/master/Anomaly%20Detection%20using%20LSTM(RNN)/LSTM.ipynb)
* The observation by EDA is also that there is no seasonality in the data. Therefore, dropping
the time-stamps from the data won’t harm us. It’s not a feature of interest for calculating
the anomaly.

* Feature Engineering – Applied several combinations on the LSTM and conclusion is that
“moving average” on the data makes it more clear for understanding the data by the model.

* Train the neural network to generate probalistic output and then apply threshold to classify the points.

* As, the data have collective anomaly splitting the data in general test-train split will destroy
the pattern which implies that splitting the data and validation process is not useful on the
data given.

### RESULTS

> **SAMPLE RESULT**

![](https://github.com/smitz94/Projects/blob/master/Anomaly%20Detection%20using%20LSTM(RNN)/sample_result.png)

### CONCLUSION

* If we get more data to train the model – “LSTM on moving average” and run the model for
larger epochs we can improve the F1-score by large amount and we can keep the accuracy
of the model stable.

* I wanted to try out synthetic data generation to achieve to repeat the pattern on random fashion
using for loop or randomised generation of pattern using pattern in the data. But, dint got
opportunity to do so. Else increasing the data and reproducing the pattern again and again using a
function would help to tune the model more and train it more effectively as LSTM requires good
amount of data for stability.
