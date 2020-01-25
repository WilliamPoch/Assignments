from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,confusion_matrix ,classification_report
from sklearn.model_selection import cross_val_predict
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn import preprocessing
import numpy

columne = ['No', 'year', 'month', 'day', 'hour', 'pm2.5', 'DEWP', 'TEMP', 'PRES', 'cbwd','Iw']
df = pd.read_csv('traindataset.csv')
ef = pd.read_csv('testdataset2.csv')
lb_make = LabelEncoder()


df = df.drop(columns = 'Is')
df = df.drop(columns = 'Ir')
df = df.drop(columns = 'No')


df = df.dropna()
df =pd.get_dummies(df,prefix = ['cbwd'])
lb_make = LabelEncoder()
ef["cbwd"] =lb_make.fit_transform(ef["cbwd"])

ef = ef.drop(columns = 'pm2.5')
ef = ef.drop(columns = 'Is')
ef = ef.drop(columns = 'Ir')
ef = ef.drop(columns = 'No')


x = df.values[:,:9]
y = df.values[:,9]
c = ef.values[:,:10]
d = ef.values[:,7]


x_scale = preprocessing.scale(x)
c_scale = preprocessing.scale(c)




gnb = GaussianNB()
gnb.fit(x_scale, y)


y_pred = cross_val_predict(gnb,x,y,cv=3)
from sklearn import metrics


print(" Train Accuracy:",accuracy_score(y, y_pred)*100)

c_pred = cross_val_predict(gnb,c,d,cv=3)

print(" Test Accuracy:",accuracy_score(d, c_pred)*100)




