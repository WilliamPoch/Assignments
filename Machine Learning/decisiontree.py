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


df = df.drop(columns = 'No')
df = df.drop(columns = 'Is')
df = df.drop(columns = 'Ir')


ef = ef.drop(columns = 'Is')
ef = ef.drop(columns = 'Ir')
ef = ef.drop(columns = 'No')

lb_make = LabelEncoder()
ef["cbwd"] =lb_make.fit_transform(ef["cbwd"])


df = df.dropna()
df =pd.get_dummies(df,prefix = ['cbwd'])
ef = ef.drop(columns = 'pm2.5')


x = df.values[:,:9]
y = df.values[:,9]
c = ef.values[:,:10]
d = ef.values[:,6]


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


y_c = cross_val_predict(clf,c,d,cv=3)
print("Test accuracy score:",accuracy_score(d,y_c)*100)
print("Confusion Matrix:")
print(confusion_matrix(d,y_c))
print("Classification_report")
print(classification_report(d,y_c))








# df = pd.read_csv('traindataset.csv',header = None,names = )
# ef = pd.read_csv('testdataset2.csv')
# columns = ['pm2.5']
# select = ['year',	'month',	'day',	'hour','DEWP'	,'TEMP'	,'PRES'	,'cbwd'	]

# remove = ['No','Is','Ir']

# df[["cbwd", "cbwd"]].head(11)

# ef["cbwd"] = lb_make.fit_transform(ef["cbwd"])
# # ef[["cbwd", "cbwd"]].head(11)

# df[columns] = df[columns].replace(0, numpy.NaN)

# # drop rows with missing values
# # df = df.dropna(axis=0)


# # df = df.drop(labels = remove, axis=1)

# # ef.dropna(df['pm2.5'],axis=1)




# x = df[select]
# y = df[columns]
# c = ef[select]
# d = ef[columns]
# # x_scale = preprocessing.scale(x)
# # c_scale = preprocessing.scale(c)






# clf = DecisionTreeClassifier(criterion='gini',max_depth=4,min_samples_split=3)
# clf.fit(x,y)
# y_p = cross_val_predict(clf,x,y,cv=3)
# print(" Train accuracy score:",accuracy_score(y,y_p)*100)
# print(" Train Confusion Matrix:")
# print(confusion_matrix(y,y_p))
# print("Train Classification_report")
# print(classification_report(y,y_p))

# clf.fit(c,d)
# y_c = cross_val_predict(clf,c,d,cv=3)
# print(" Test accuracy score:",accuracy_score(d,y_c)*100)
# print(" Test Confusion Matrix:")
# print(confusion_matrix(d,y_c))
# print("Test Classification_report")
# print(classification_report(d,y_c))













    













