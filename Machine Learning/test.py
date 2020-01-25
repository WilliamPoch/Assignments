
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,confusion_matrix ,classification_report
from sklearn.model_selection import cross_val_predict
import graphviz
from sklearn.tree import export_graphviz
from sklearn.preprocessing import LabelEncoder
from sklearn import preprocessing
from subprocess import check_call
import pandas as pd
import numpy 
columne = ['No', 'year', 'month', 'day', 'hour', 'pm2.5', 'DEWP', 'TEMP' ,'PRES' ,'cbwd' ,'Iw'
]
pm = 'pm2.5'
e = 'cbwd'
select = ['No','pm2.5','Iw']
df = pd.read_csv('traindataset.csv')
ef = pd.read_csv('testdataset2.csv')
gf = pd.read_csv('testdataset2.csv')


# ef = pd.get_dummies(ef,columns = columne ,dummy_na = True)





df = df.drop(columns = 'Is')
df = df.drop(columns = 'Ir')
# lb_make = LabelEncoder()
# df["cbwd"] =lb_make.fit_transform(df["cbwd"])


ef = ef.drop(columns = 'Is')
ef = ef.drop(columns = 'Ir')
# lb_make = LabelEncoder()
# ef["cbwd"] =lb_make.fit_transform(ef["cbwd"])




df = df.dropna()
ef = ef.dropna()
# ef = ef.drop(['pm2.5'],axis = 1)
# gf = gf.dropna()

df =pd.get_dummies(df,prefix = ['cbwd'])
ef =pd.get_dummies(ef,prefix = ['cbwd'])


print(df)
x = df.values[:,:10]
y = df.values[:,10]
c = ef.values[:,:10]
d = ef.values[:,5]

x_scale = preprocessing.scale(x)
c_scale = preprocessing.scale(c)

clf = DecisionTreeClassifier(criterion='gini', max_depth=4)
clf.fit(x_scale,y)
y_p = cross_val_predict(clf,x,y,cv=3)
print(" Training accuracy score:",accuracy_score(y,y_p)*100)
print("Confusion Matrix:")
print(confusion_matrix(y,y_p))
print("Classification_report")
print(classification_report(y,y_p))




clf.fit(c_scale,d)
y_c = cross_val_predict(clf,c,d,cv=3)
print("Test accuracy score:",accuracy_score(d,y_c)*100)
print("Confusion Matrix:")
print(confusion_matrix(d,y_c))
print("Classification_report")
print(classification_report(d,y_c))