# -*- coding: utf-8 -*-
"""decision tree.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WnSqPNsy88rs_5nRPoLEiZm1Tn4xe8lC
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score

data = pd.read_csv('/diabetes.csv')
data.head()

x = data[['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']].values
y = data['Outcome'].values
print(x)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)

clf = DecisionTreeClassifier()
clf = clf.fit(x_train,y_train)
print(clf.score(x_test,y_test))

y_pred = clf.predict(x_test)
print(y_pred)

clf = DecisionTreeClassifier(criterion='entropy',max_depth=3)
clf = clf.fit(x_train,y_train)
print(clf.score(x_test,y_test))

decision=DecisionTreeClassifier(max_depth=3)
decision.fit(x_train,y_train)
y_pred=decision.predict(x_test)

y_pred = clf.predict(x_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1-score:", f1_score(y_test, y_pred))

from sklearn import tree
plt.figure(figsize=(12,12))
tree.plot_tree(clf,filled=True)
plt.show()

