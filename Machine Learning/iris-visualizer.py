import matplotlib.pyplot as plt
from sklearn.datasets import load_iris


#load
iris = load_iris()
x,y = iris.data, iris.target
print(iris.target_names)

#plot data as a scatter plot
a, b = 2, 3
plt.figure(1)
plt.scatter(x[:,a], x[:,b], c=y)
plt.xlabel(iris.feature_names[a])
plt.ylabel(iris.feature_names[b])
plt.show()
