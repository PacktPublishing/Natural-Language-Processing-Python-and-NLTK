

# sampling steps 
trainset_size = int(round(len(sms_data)*0.70))
# i chose this threshold for 70:30 train and test split.
print 'The training set size for this classifier is ' + str(trainset_size) + '\n'
x_train = np.array([''.join(el) for el in sms_data[0:trainset_size]])
y_train = np.array([el for el in sms_labels[0:trainset_size]])
x_test = np.array([''.join(el) for el in sms_data[trainset_size+1:len(sms_data)]])
y_test = np.array([el for el in sms_labels[trainset_size+1:len(sms_labels)]])
print x_train
print y_train

# count vectorizer 
# not really used just for explanation 
from sklearn.feature_extraction.text import CountVectorizer
sms_exp=[ ]
for line in sms_list:
	sms_exp.append(preprocessing(line[1]))
vectorizer = CountVectorizer(min_df=1)
X_exp = vectorizer.fit_transform(sms_exp)
print "||".join(vectorizer.get_feature_names())
print X_exp.toarray()

# We are building a TFIDF vectorizer here
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(min_df=2, ngram_range=(1, 2),  stop_
words='english',  strip_accents='unicode',  norm='l2')
X_train = vectorizer.fit_transform(x_train)
X_test = vectorizer.transform(x_test)

from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB().fit(X_train, y_train)
y_nb_predicted = clf.predict(X_test)
print y_nb_predicted
print ' \n confusion_matrix \n '
cm = confusion_matrix(y_test, y_pred)
print cm
print '\n Here is the classification report:'
print classification_report(y_test, y_nb_predicted)
# print the top features 

coefs = clf.coef_
intercept = clf.intercept_
coefs_with_fns = sorted(zip(clf.coef_[0], feature_names))
n=10
top = zip(coefs_with_fns[:n], coefs_with_fns[:-(n + 1):-1])
for (coef_1, fn_1), (coef_2, fn_2) in top:
	print('\t%.4f\t%-15s\t\t%.4f\t%-15s' % (coef_1, fn_1, coef_2, fn_2))


# SGD mostly used

from sklearn.linear_model import SGDClassifier
from sklearn.metrics import confusion_matrix
clf=SGDClassifier(alpha=.0001, n_iter=50).fit(X_train, y_train)
y_pred = clf.predict(X_test)
print '\n Here is the classification report:'
print classification_report(y_test, y_pred)
print ' \n confusion_matrix \n '
cm = confusion_matrix(y_test, y_pred)
print cm

# SVM
from sklearn.svm import LinearSVC
svm_classifier = LinearSVC().fit(X_train, y_train)
y_svm_predicted = svm_classifier.predict(X_test)
print '\n Here is the classification report:'
print classification_report(y_test, y_svm_predicted)
cm = confusion_matrix(y_test, y_pred)
print cm

# RandomForestClassifier

from sklearn.ensemble import RandomForestClassifier
RF_clf = RandomForestClassifier(n_estimators=10)
predicted = RF_clf.predict(X_test)
print '\n Here is the classification report:'
print classification_report(y_test, predicted)
cm = confusion_matrix(y_test, y_pred)
print cm
