import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
import csv

print("Success! Module imported")

data = pd.read_csv("df_pivoted.csv")
print(data.shape)

lis = [1, 100, 200, 300, 400]

with open('Book2.csv', 'a', newline='') as csvfile:
    #write = csvfile.writer(csvfile, delimiter = ',')
    write = csv.writer(csvfile,delimiter=',')
    row = [1 if i in lis else 0 for i in range(0, 404)]
    write.writerow(row)

data1 = pd.read_csv("Book2.csv")

X_test = data1.values[-1, :]

#data1 = pd.read_csv("Book2.csv")
#print("data :", data1)
print("data read")
#X = data.values( 1:2)
X = data.values[:, 1:]
Y = data.values[:, 0] 

#X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.01, random_state = 100) 

print(X)
print(Y)
print(X_test)
var_entr = DecisionTreeClassifier(criterion="entropy")
var_gini = DecisionTreeClassifier(criterion="gini")

var_gini.fit(X, Y)
var_entr.fit(X, Y)

y_pred1 = var_entr.predict([X_test])
y_pred2 = var_gini.predict([X_test])
print("ans :" , y_pred1, y_pred2)
