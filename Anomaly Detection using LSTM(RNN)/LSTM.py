#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.metrics import confusion_matrix,f1_score
from sklearn.metrics import classification_report
from sklearn.preprocessing import MinMaxScaler

# fixing the randomness to reproduce the data for debugging
np.random.seed(7)

# read all 4 input files
data=pd.read_csv('Documents\ec2_cpu_utilization_24ae8d.csv')

df=pd.DataFrame(data)
df1=pd.read_csv('Documents\ec2_cpu_utilization_5f5533.csv')
df2=pd.read_csv('Documents\ec2_cpu_utilization_53ea38.csv')
df3=pd.read_csv('Documents\ec2_cpu_utilization_77c1ca.csv')

#Normalizing data to scale it for the training
df3_trans=df3.drop('timestamp', 1)
scaler = MinMaxScaler(feature_range=(0, 1))
df3_trans = scaler.fit_transform(df3_trans)

df3_trans=pd.DataFrame(df3_trans)
df3_trans.columns=['value','label']


df2_trans=df2.drop('timestamp', 1)
scaler = MinMaxScaler(feature_range=(0, 1))
df2_trans = scaler.fit_transform(df2_trans)

df2_trans=pd.DataFrame(df2_trans)
df2_trans.columns=['value','label']

df1_trans=df1.drop('timestamp', 1)
scaler = MinMaxScaler(feature_range=(0, 1))
df1_trans = scaler.fit_transform(df1_trans)

df1_trans=pd.DataFrame(df1_trans)
df1_trans.columns=['value','label']

# merge all the data for training
frames=[df,df1_trans,df2_trans,df3_trans]
df_final = pd.concat(frames,sort=False)


# feature engineering (applying moving average over a window size of 10 elements)
X_in=df_final['value']
Y_in=df_final['label']
X_in=X_in.values

MX=df_final['value'].rolling(window=10).mean()
MX=pd.DataFrame(MX)

MX.columns=['avg']
MX.loc[MX['avg'].isnull(),'avg'] = .132

MX=MX.values

#reshaping data for training
trainX=X_in.reshape((X_in.shape[0],1,1))

trainmx=MX.reshape((MX.shape[0],1,1))

# training the model and predicting the output the same data to preserve the pattern in the data
model = Sequential()
model.add(LSTM(4, input_shape=(trainmx.shape[1], trainmx.shape[2])))
model.add(Dense(1,activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['binary_accuracy'])
print(model.summary())
model.fit(trainmx,Y_in, epochs=150, batch_size=10, verbose=2)

#predicting data and grouping the alert
mypred = model.predict(trainmx)

avg =np.mean(mypred)
#grouping the alert based on mean and distributing them according to it
mypred1=[]
for i in mypred:
    if(i>=avg):
        mypred1.append(1)
    else:
        mypred1.append(0)

mypred1=np.array(mypred1)

# Evaluating model
print(classification_report(Y_in, mypred1))
print(confusion_matrix(Y_in,mypred1))
print("F1 Score=",f1_score(Y_in,mypred1))


# ### Calculating predictions on the Merged file 1 by 1 and see the results

# #### 1. For the data "ec2_cpu_utilization_5f5533.csv"

# In[2]:


X1_in=df1_trans['value'].values
Y1_in=df1_trans['label'].values


MX1=df1_trans['value'].rolling(window=10).mean()
MX1=pd.DataFrame(MX1)

MX1.columns=['avg']
MX1.loc[MX1['avg'].isnull(),'avg'] = X1_in[0]

MX1=MX1.values

trainmx1=MX1.reshape((MX1.shape[0],1,1))

mypred = model.predict(trainmx1)

avg =np.mean(mypred)

mypred1=[]
for i in mypred:
    if(i>=avg):
        mypred1.append(1)
    else:
        mypred1.append(0)

mypred1=np.array(mypred1)


print(classification_report(Y1_in, mypred1))
print(confusion_matrix(Y1_in,mypred1))
print("F1 Score=",f1_score(Y1_in,mypred1))


# #### 2. For the data "ec2_cpu_utilization_53ea38.csv"

# In[3]:


X2_in=df2_trans['value'].values
Y2_in=df2_trans['label'].values

MX2=df2_trans['value'].rolling(window=10).mean()
MX2=pd.DataFrame(MX2)

MX2.columns=['avg']
MX2.loc[MX2['avg'].isnull(),'avg'] = X2_in[0]

MX2=MX2.values

trainmx2=MX2.reshape((MX2.shape[0],1,1))

mypred = model.predict(trainmx2)
avg =np.mean(mypred)

mypred1=[]
for i in mypred:
    if(i>=avg):
        mypred1.append(1)
    else:
        mypred1.append(0)

mypred1=np.array(mypred1)


print(classification_report(Y2_in, mypred1))
print(confusion_matrix(Y2_in,mypred1))
print("F1 Score=",f1_score(Y2_in,mypred1))


# #### 3. For the data "ec2_cpu_utilization_77c1ca.csv"

# In[4]:


X3_in=df3_trans['value'].values
Y3_in=df3_trans['label'].values

MX3=df3_trans['value'].rolling(window=10).mean()
MX3=pd.DataFrame(MX3)

MX3.columns=['avg']
MX3.loc[MX3['avg'].isnull(),'avg'] = X3_in[0]

MX3=MX3.values

trainmx3=MX3.reshape((MX3.shape[0],1,1))

mypred = model.predict(trainmx3)
avg =np.mean(mypred)

mypred1=[]
for i in mypred:
    if(i>=avg):
        mypred1.append(1)
    else:
        mypred1.append(0)

mypred1=np.array(mypred1)


print(classification_report(Y3_in, mypred1))
print(confusion_matrix(Y3_in,mypred1))
print("F1 Score=",f1_score(Y3_in,mypred1))


# #### 4. For the data "ec2_cpu_utilization_24ae8d.csv"

# In[5]:


X4_in=df['value'].values
Y4_in=df['label'].values

MX4=df['value'].rolling(window=10).mean()
MX4=pd.DataFrame(MX4)

MX4.columns=['avg']
MX4.loc[MX4['avg'].isnull(),'avg'] = X4_in[0]

MX4=MX4.values

trainmx4=MX4.reshape((MX4.shape[0],1,1))

mypred = model.predict(trainmx4)
avg =np.mean(mypred)

mypred1=[]
for i in mypred:
    if(i>=avg):
        mypred1.append(1)
    else:
        mypred1.append(0)

mypred1=np.array(mypred1)


print(classification_report(Y4_in, mypred1))
print(confusion_matrix(Y4_in,mypred1))
print("F1 Score=",f1_score(Y4_in,mypred1))


# ### 1. Output of ec2_cpu_utilization_24ae8d.csv

# In[15]:


data1=pd.read_csv('Documents\ec2_cpu_utilization_24ae8d_1.csv')

df1=pd.DataFrame(data1)

X_in1=df1['value']

X_in1=X_in1.values

MX1=data1['value'].rolling(window=10).mean()
MX1=pd.DataFrame(MX1)

MX1.columns=['avg']
MX1.loc[MX1['avg'].isnull(),'avg'] = X_in1[0]

MX1=MX1.values


trainX1=X_in1.reshape((X_in1.shape[0],1,1))

trainmx1=MX1.reshape((MX1.shape[0],1,1))

mypred = model.predict(trainmx1)

avg =np.mean(mypred)

mypred1=[]
for i in mypred:
    if(i>=avg):
        mypred1.append(1)
    else:
        mypred1.append(0)

mypred1=np.array(mypred1)
print(mypred1)

print("After OverSampling, counts of label '1': {}".format(sum(mypred1 == 1))) 
print("After OverSampling, counts of label '0': {}".format(sum(mypred1 == 0))) 

df1['label']=mypred1
df1.to_csv('Output_ec2_cpu_utilization_24ae8d.csv') 


# ### 2. Output of the Evaluation file "ec2_cpu_utilization_5f5533.csv"

# In[13]:


# reading data
data2=pd.read_csv('Documents\Evaluation Dataset\ec2_cpu_utilization_5f5533.csv')


#Normalizing data for prediction
df2=data2['value'].values.reshape(-1,1)
scaler = MinMaxScaler(feature_range=(0, 1))
df2 = scaler.fit_transform(df2)

df2=pd.DataFrame(df2)
df2.columns=['value']

X_in2=df2['value']
X_in2=X_in2.values

# Implementing moving average over window of 10
MX2=df2['value'].rolling(window=10).mean()
MX2=pd.DataFrame(MX2)

MX2.columns=['avg']
MX2.loc[MX2['avg'].isnull(),'avg'] = X_in2[0]

MX2=MX2.values

trainmx2=MX2.reshape((MX2.shape[0],1,1))

# Predicting the output
mypred = model.predict(trainmx2)

avg =np.mean(mypred)

mypred1=[]
for i in mypred:
    if(i>=avg):
        mypred1.append(1)
    else:
        mypred1.append(0)

mypred1=np.array(mypred1)
print(mypred1)

print("After OverSampling, counts of label '1': {}".format(sum(mypred1 == 1))) 
print("After OverSampling, counts of label '0': {}".format(sum(mypred1 == 0))) 

# Saving the output in .csv file
data2['label']=mypred1
data2.to_csv('Output_ec2_cpu_utilization_5f5533.csv') 


# ### 3. Output of the Evaluation file "ec2_cpu_utilization_53ea38.csv"

# In[16]:


# reading data
data3=pd.read_csv('Documents\Evaluation Dataset\ec2_cpu_utilization_53ea38.csv')


#Normalizing data for prediction
df3=data3['value'].values.reshape(-1,1)
scaler = MinMaxScaler(feature_range=(0, 1))
df3 = scaler.fit_transform(df3)

df3=pd.DataFrame(df3)
df3.columns=['value']

X_in3=df3['value']
X_in3=X_in3.values

# Implementing moving average over window of 10
MX3=df3['value'].rolling(window=10).mean()
MX3=pd.DataFrame(MX3)

MX3.columns=['avg']
MX3.loc[MX3['avg'].isnull(),'avg'] = X_in3[0]

MX3=MX3.values

trainmx3=MX3.reshape((MX3.shape[0],1,1))

# Predicting the output
mypred = model.predict(trainmx3)

avg =np.mean(mypred)

mypred1=[]
for i in mypred:
    if(i>=avg):
        mypred1.append(1)
    else:
        mypred1.append(0)

mypred1=np.array(mypred1)
print(mypred1)

print("After OverSampling, counts of label '1': {}".format(sum(mypred1 == 1))) 
print("After OverSampling, counts of label '0': {}".format(sum(mypred1 == 0))) 

# Saving the output in .csv file
data3['label']=mypred1
data3.to_csv('Output_ec2_cpu_utilization_53ea38.csv') 


# ### 4. Output of the Evaluation file "ec2_cpu_utilization_77c1ca.csv"

# In[18]:


# reading data
data4=pd.read_csv('Documents\Evaluation Dataset\ec2_cpu_utilization_77c1ca.csv')


#Normalizing data for prediction
df4=data4['value'].values.reshape(-1,1)
scaler = MinMaxScaler(feature_range=(0, 1))
df4 = scaler.fit_transform(df4)

df4=pd.DataFrame(df4)
df4.columns=['value']

X_in4=df4['value']
X_in4=X_in4.values

# Implementing moving average over window of 10
MX4=df4['value'].rolling(window=10).mean()
MX4=pd.DataFrame(MX4)

MX4.columns=['avg']
MX4.loc[MX4['avg'].isnull(),'avg'] = X_in4[0]

MX4=MX4.values

trainmx4=MX4.reshape((MX4.shape[0],1,1))

# Predicting the output
mypred = model.predict(trainmx2)

avg =np.mean(mypred)

mypred1=[]
for i in mypred:
    if(i>=avg):
        mypred1.append(1)
    else:
        mypred1.append(0)

mypred1=np.array(mypred1)
print(mypred1)

print("After OverSampling, counts of label '1': {}".format(sum(mypred1 == 1))) 
print("After OverSampling, counts of label '0': {}".format(sum(mypred1 == 0))) 

# Saving the output in .csv file
data4['label']=mypred1
data4.to_csv('Output_ec2_cpu_utilization_77c1ca.csv') 

