# -*- coding: utf-8 -*-
"""ios_defect_2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16GWFZwH07gnPOCvBq6BFZ7VCTeSxbcS6
"""

import pandas as pd

master_data = pd.read_csv('ios(1).csv',sep=',', encoding='latin-1')
print('data shape: ', master_data.shape)
master_data.head()

master_data.isnull().sum()

mydataset_without_null = master_data.fillna(0)
print(mydataset_without_null.isnull().sum())

mydataset_without_null.info()

data_copy = mydataset_without_null.drop(['ios version'], axis=1)
#data_copy = data_copy.drop(['total_bugs'], axis=1)

print(data_copy)

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split

var_holder = {}
x_test_holder = {}
y_test_holder = {}
x_train_holder = {}
y_train_holder = {}


def training(i):


    print(i)
    y=data_copy[i].values
    x=data_copy['ios_version'].values
    x=x.reshape(-1,1)
    x_train_holder['train_x_of_' + str(i)], x_test_holder['test_x_of_' + str(i)], y_train_holder['train_y_of_' + str(i)], y_test_holder['test_y_of_' + str(i)] = train_test_split(x, y, test_size=0.2, shuffle=True)
    var_holder['trained_model_of_' + str(i)] = GradientBoostingClassifier(n_estimators=100, learning_rate=2,max_depth=1, random_state=42).fit(x_train_holder.get('train_x_of_' + str(i)), y_train_holder.get('train_y_of_' + str(i)))

for i in data_copy.columns:
  if i == 'ios_version':
    break

  training(i)

locals().update(var_holder)

var_holder = {}
x_test_holder = {}
y_test_holder = {}
x_train_holder = {}
y_train_holder = {}


def training(i):

  try:
    print(i)
    y=data_copy[i].values
    x=data_copy['ios_version'].values
    x=x.reshape(-1,1)
    x_train_holder['train_x_of_' + str(i)], x_test_holder['test_x_of_' + str(i)], y_train_holder['train_y_of_' + str(i)], y_test_holder['test_y_of_' + str(i)] = train_test_split(x, y, test_size=0.2, shuffle=True)
    var_holder['trained_model_of_' + str(i)] = GradientBoostingClassifier(n_estimators=100, learning_rate=2,max_depth=1, random_state=42).fit(x_train_holder.get('train_x_of_' + str(i)), y_train_holder.get('train_y_of_' + str(i)))

  except:
    print('error___________________________________________',i)
    training(i)

for i in data_copy.columns:
  if i == 'ios_version':
    break

  training(i)

locals().update(var_holder)

var_holder.keys()

x_train_holder.keys()

x_test_holder.keys()

y_test_holder.keys()

y_train_holder.keys()

from sklearn.metrics import accuracy_score

def accu(name_of_model,x_test_for_pre,y_test_for_pre):
  pred = var_holder.get(name_of_model).predict(x_test_holder.get(x_test_for_pre))
  print(pred)
  print("Accuracy Score: ",accuracy_score(y_test_holder.get(y_test_for_pre),pred))

for bla in data_copy.columns:
  if bla == 'ios_version':
    break
  name_of_model= 'trained_model_of_'+str(bla)
  x_test_for_pre= 'test_x_of_'+str(bla)
  y_test_for_pre= 'test_y_of_'+str(bla)
  accu(name_of_model,x_test_for_pre,y_test_for_pre)

pred_data = pd.read_csv('pred_test.csv',sep=',', encoding='latin-1')

df = pred_data.drop(['ios version'], axis=1)
df

matrix_list=[]
def fp(name_of_model,f_x):
  pred = var_holder.get(name_of_model).predict(f_x)
  print(pred)
  global matrix_list
  matrix_list.append(pred.item())
  print('(---------------------------------------------------------------------------------------)')

f_x=df['ios_version'].values
f_x=f_x.reshape(-1,1)
for blaa in df.columns:
  if blaa == 'ios_version':
    break

  name_of_model= 'trained_model_of_'+str(blaa)
  print(blaa)
  fp(name_of_model,f_x)

print(matrix_list)

actual_list = [0,1,0,0,0,1,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0]

import matplotlib.pyplot as plt
import numpy
from sklearn import metrics

confusion_matrix = metrics.confusion_matrix(actual_list, matrix_list)

cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = ['1','0'])
cm_display.plot()
plt.show()