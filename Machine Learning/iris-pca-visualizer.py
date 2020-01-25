import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA

#load
iris = load_iris()
x,y = iris.data, iris.target
print(iris.target_names)

#apply PCA to data
pca = PCA()
pca.fit(x)
x_t = pca.transform(x)

#plot data as a scatter plot
plt.figure(1)
plt.scatter(x_t[:,0], x_t[:,1], c=y)
plt.xlabel('Component 1')
plt.ylabel('Component 2')
plt.show()
