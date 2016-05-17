from sklearn import svm

#X is a matrix of input examples [[x1.....xn],...[x1,..., xn]]
#Y is a vector of labels corresponding to emotion [1, 2, 8, ... yn]


def train(X, y):
	clf = svm.SVC(decision_function_shape='ovo')
	clf.fit(X,y)
	print 'Finished Training SVM'
	return clf

def test(clf, X):
	#Takes all examples to predict and returns an array of lables
	predictions = clf.predict(X)
	print 'Finished Predictions for SVM'
	return predictions


############ Sample usage ####################

#X = [[0,1], [3,4], [6,2], [1,2]]
#y = [1,2,3,4]

#clf = train(X, y)
#predictions = test(clf, X)

#print predictions
