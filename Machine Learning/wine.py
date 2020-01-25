import pandas as pd
from sklearn.datasets import load_wine
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import cross_val_predict
from sklearn.tree import DecisionTreeClassifier

import graphviz
from sklearn.tree import export_graphviz
from subprocess import check_call


iris = load_wine()
x, y = iris.data, iris.target

clf = DecisionTreeClassifier()
clf.fit(x,y)

y_p = clf.predict(x)
y_p = cross_val_predict(clf, x, y, cv=3)

print('Accuracy Score:', accuracy_score(y, y_p))
print('Confusion Matrix:') 
print(confusion_matrix(y, y_p))
print('Classification Report')
print(classification_report(y, y_p))


#dot_data = export_graphviz(clf, out_file='tree-led00.dot', 
#feature_names=['a0','a1','a2','a3','a4','a5','a6'], rounded=True)
#graph = graphviz.Source(dot_data)
#graph
#check_call(['graphviz/bin/dot', '-Tpng', 'tree-led00.dot', '-o', 'tree-led00.png'])
	