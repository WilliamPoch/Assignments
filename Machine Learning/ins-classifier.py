from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score ,confusion_matrix, classification_report
from sklearn.model_selection import cross_val_predict

#load
iris = load_iris()
x,y = iris.data, iris.target
print(iris.target_names)

#train
clf = DecisionTreeClassifier()
clf.fit(x,y)

#validate
y_p = cross_val_predict(clf, x, y, cv=3)
score = accuracy_score(y, y_p)

print('accuracy_score', accuracy_score(y, y_p))
print('confusion matrix:')
print(confusion_matrix(y, y_p))
print('classification report')
print(classification_report(y, y_p))

#input
sl = input('sepal length:')
sw = input('sepal width:')
pl = input('petal length:')
pw = input('petal width:')

y_pred = clf.predict([[sl, sw, pl, pw]])
print(y_pred)

#print(x)
#print(y)
