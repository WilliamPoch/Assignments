from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score ,confusion_matrix, classification_report
from sklearn import metrics
import numpy as np

categories = ['alt.atheism', 'talk.religion.misc', 'comp.graphics', 'sci.space']
y = fetch_20newsgroups(subset='train', remove=('headers', 'footers', 'quotes'),
                       categories=categories)
vectorizer = TfidfVectorizer(min_df=1, max_df=0.8)
x = vectorizer.fit_transform(y.data)
features = x.toarray()
svd = TruncatedSVD(n_components=5)
svd.fit(x)
reduced = svd.transform(x)

clf = LinearSVC(random_state=0, multi_class='ovr')
clf.fit(x, y.target)
test = vectorizer.fit_transform(y.data)
pred = clf.predict(test)
