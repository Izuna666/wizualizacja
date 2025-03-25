import pandas
import matplotlib.pyplot as plt
import scipy
import sklearn
import sklearn.metrics

#build in dataset:
iris = sklearn.datasets.load_iris()
df = pandas.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target

#print(df)

#separating data into input and output:
X = df.iloc[:, :-1].values
Y = df.iloc[:, -1].values

#separating data into learning and testing sets with common 80/20 split, rsndom state decides about bootstraping data and it randomness
X_train, X_test, Y_train, Y_test = sklearn.model_selection.train_test_split(X, Y, test_size=0.2, random_state=1)

classifier = sklearn.ensemble.RandomForestClassifier(n_estimators=100, random_state=1)
classifier.fit(X_train, Y_train)
Y_pred = classifier.predict(X_test)

#testing our model with accuracy
accuracy = sklearn.metrics.accuracy_score(Y_test, Y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')

conf_matrix = sklearn.metrics.confusion_matrix(Y_test, Y_pred)
display_matrix = sklearn.metrics.ConfusionMatrixDisplay(confusion_matrix= conf_matrix)
display_matrix.plot()
plt.show()



