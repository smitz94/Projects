#!/usr/bin/env python
# coding: utf-8

# ## Basic Structure of the Code
# 
# * EDA on normal data
# * LSTM on normal data
# * LSTM on feature engineered data (moving average)
# * LSTM on normal data with SMOTE
# * LSTM on feature engineered data with SMOTE
# 

# In[1]:


# reading data from source

import pandas as pd
data=pd.read_csv('Documents\ec2_cpu_utilization_24ae8d.csv')


# In[2]:


df=pd.DataFrame(data)


# ### EDA on normal data

# In[3]:


import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (20,10)


# In[4]:


#Following is the plot of both the labels 0 and 1 seperately showing their corresponding pattern

df.groupby('label').plot.line(x='timestamp', y= 'value')


# In[5]:


#following is the plot showing anomalous data showing seperately in green color 

fig, ax = plt.subplots(figsize=(15,7))
y1 = df[(df['timestamp'] >= '25-02-2014  00:00:00')& (df['timestamp'] <= '28-02-2014 14:25:00')]
y1.groupby('label').plot(ax=ax)


# In[6]:


# normal plot of values to see the trigger of anomalous behaviour

plt.plot(df['value'])


# #### Applying Z-score to the data and try to remove outliers from the data

# In[7]:


from scipy import stats
import numpy as np
from sklearn.metrics import confusion_matrix,f1_score
from sklearn.metrics import classification_report

X_in=data['value']
Y_in=data['label']

X_in=X_in.values
Y_in=Y_in.values



z_score=stats.zscore(X_in)


std_dev=np.std(X_in)

ypred=[]
for i in z_score:
    if(i>=1.96 or i<=-1.96):
        ypred.append(1)
    else:
        ypred.append(0)
ypred=np.array(ypred)


print(classification_report(Y_in, ypred))
print("F1 Score=",f1_score(Y_in,ypred))


# #### Calculating Z-score for moving avg Data

# In[8]:


MX=data['value'].rolling(window=10).mean()
MX=pd.DataFrame(MX)

MX.columns=['avg']
MX.loc[MX['avg'].isnull(),'avg'] = .132

MX=MX.values

Mz_score=stats.zscore(MX)
Mstd_dev=np.std(MX)

Mypred=[]
for i in z_score:
    if(i>=1.96 or i<=-1.96):
        Mypred.append(1)
    else:
        Mypred.append(0)
Mypred=np.array(Mypred)

print(classification_report(Y_in, Mypred))
print("F1 Score=",f1_score(Y_in,Mypred))


# #### As we can see basic EDA and Outlier removal using Z-score wont help much and we need better algorithm to detect anomaly and have stable and consistent results in real time too.
# 
# #### 1. Applying LSTM to normal data extracted from the .csv file

# In[9]:


import numpy as np
import matplotlib.pyplot as plt
import pandas
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.metrics import confusion_matrix,f1_score
from sklearn.metrics import classification_report


X_in=df['value']
Y_in=df['label']
X_in=X_in.values


trainX=X_in.reshape((X_in.shape[0],1,1))

model = Sequential()
model.add(LSTM(4, input_shape=(trainX.shape[1], trainX.shape[2])))
model.add(Dense(1,activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['binary_accuracy'])
print(model.summary())
model.fit(trainX,Y_in, epochs=100, batch_size=10, verbose=2)


# In[10]:


ypred = model.predict(trainX)

avg =np.mean(ypred)

ypred1=[]
for i in ypred:
    if(i>=avg):
        ypred1.append(1)
    else:
        ypred1.append(0)

ypred1=np.array(ypred1)


print(classification_report(Y_in, ypred1))
print(confusion_matrix(Y_in,ypred1))
print("F1 Score=",f1_score(Y_in,ypred1))


# #### This yet can be improved by taking feature engineering into account therefor applying 
# #### 2. LSTM on feature engineered data (moving average)

# In[11]:


trainmx=MX.reshape((MX.shape[0],1,1))

model = Sequential()
model.add(LSTM(4, input_shape=(trainmx.shape[1], trainmx.shape[2])))
model.add(Dense(1,activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['binary_accuracy'])
print(model.summary())
model.fit(trainmx,Y_in, epochs=200, batch_size=10, verbose=2)



# In[12]:


mypred = model.predict(trainmx)

avg =np.mean(mypred)

mypred1=[]
for i in mypred:
    if(i>=avg):
        mypred1.append(1)
    else:
        mypred1.append(0)

mypred1=np.array(mypred1)


print(classification_report(Y_in, mypred1))
print(confusion_matrix(Y_in,mypred1))
print("F1 Score=",f1_score(Y_in,mypred1))


# as the data is imbalanced we can try to make it balanced using SMOTE on both normal and average data

# In[13]:


get_ipython().system('pip install imblearn')


# #### 3. LSTM on normal data with SMOTE

# In[14]:


from imblearn.over_sampling import SMOTE

X_sm=np.array(X_in)
Y_sm=np.array(Y_in)

X_sm=X_sm.reshape(-1,1)
Y_sm=Y_sm.reshape(-1,1)

X_sm,Y_sm=SMOTE(random_state=2).fit_resample(X_sm,Y_sm.ravel())

trainX_sm=X_sm.reshape(X_sm.shape[0],1,1)
trainY_sm=Y_sm.reshape(Y_sm.shape[0],1,1)

model = Sequential()
model.add(LSTM(4, input_shape=(trainX_sm.shape[1], trainX_sm.shape[2])))
model.add(Dense(1,activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['binary_accuracy'])
print(model.summary())
model.fit(trainX_sm,Y_sm, epochs=200, batch_size=10, verbose=2)


# In[15]:


ypred_sm = model.predict(trainX)

avg =np.mean(ypred_sm)

ypred1_sm=[]
for i in ypred_sm:
    if(i>=avg):
        ypred1_sm.append(1)
    else:
        ypred1_sm.append(0)

ypred1_sm=np.array(ypred1_sm)


print(classification_report(Y_in, ypred1_sm))
print(confusion_matrix(Y_in,ypred1_sm))
print("F1 Score=",f1_score(Y_in,ypred1_sm))


# #### 4. LSTM on feature engineered data with SMOTE

# In[16]:


MX_sm=np.array(MX)
Y_sm=np.array(Y_in)

MX_sm=MX_sm.reshape(-1,1)
Y_sm=Y_sm.reshape(-1,1)

MX_sm,Y_sm=SMOTE(random_state=2).fit_resample(MX_sm,Y_sm.ravel())

trainMX_sm=MX_sm.reshape(X_sm.shape[0],1,1)
trainY_sm=Y_sm.reshape(Y_sm.shape[0],1,1)

model = Sequential()
model.add(LSTM(4, input_shape=(trainMX_sm.shape[1], trainMX_sm.shape[2])))
model.add(Dense(1,activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['binary_accuracy'])
print(model.summary())
model.fit(trainMX_sm,Y_sm, epochs=200, batch_size=20, verbose=2)


# In[17]:


Mypred_sm = model.predict(trainmx)

avg =np.mean(Mypred_sm)

Mypred1_sm=[]
for i in Mypred_sm:
    if(i>=avg):
        Mypred1_sm.append(1)
    else:
        Mypred1_sm.append(0)

Mypred1_sm=np.array(Mypred1_sm)


print(classification_report(Y_in, Mypred1_sm))
print(confusion_matrix(Y_in,Mypred1_sm))
print("F1 Score=",f1_score(Y_in,Mypred1_sm))


# ## Conclusion
# #### As seen from the output of several combinations the most stable appraoch is LSTM on feature engineered data where we calculated moving average for a window of 10 and applied LSTM on it.
# #### SMOTE is not giving good results because the anomaly is collective in nature and data generation on random fashion to equalise minority and majority wont help.
# #### Therefore, the most reliable approach is to maitaing moving average over a window and train the model accordingly for better results.

# In[ ]:




