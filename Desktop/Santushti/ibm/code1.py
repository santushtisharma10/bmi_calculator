# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 18:54:04 2020

@author: Sai Nidhi
"""

import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt

df=pd.read_csv(r"C:\Users\Hp\Desktop\hackathon.csv",encoding="ISO-8859-1")
df.head()

import re
import nltk

nltk.download('stopwords')
from nltk.corpus import stopwords

from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()

df['Tweet_Text'][0]
copy=df['Tweet_Text']
c=[]
for i in range(0,2569):
    review = re.sub('[^a-zA-Z]',' ',df['Tweet_Text'][i])
    review=review.lower()
    review=review.split()
    ps=PorterStemmer()
    review=[ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review= ' '.join(review)
    c.append(review)
    
from sklearn.feature_extraction.text import CountVectorizer  
cv=CountVectorizer(max_features=1500)
x=cv.fit_transform(c).toarray()
with open('CountVectorizer','wb') as file:
    pickle.dump(cv,file)
y=df.iloc[:,1].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.1,random_state=0)

import keras
from keras.models import Sequential
from keras.layers import Dense

cls=Sequential()
cls.add(Dense(6, kernel_initializer='glorot_uniform', activation='sigmoid',input_dim=1500))
cls.add(Dense(6, kernel_initializer='glorot_uniform',activation='sigmoid'))
cls.add(Dense(6, kernel_initializer='glorot_uniform',activation='sigmoid'))
cls.compile(optimizer='adam',loss='binary_crossentropy')
cls.fit(x_train,y_train,epochs=50,batch_size=50)
cls.save('twitter1.h5')

y_pred=cls.predict(x_test)
y_pred=(y_pred>0.5)
print(y_pred)

x_intent="I am a good girl"
x_intent=cv.transform([x_intent])
y_pred=cls.predict(x_intent)
y_pred=(y_pred>0.5)
print(y_pred)
