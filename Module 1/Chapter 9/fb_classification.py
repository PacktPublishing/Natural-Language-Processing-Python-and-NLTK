from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(min_df=2, ngram_range=(1, 2),  stop_words='english',  strip_accents='unicode',  norm='l2')
X_train = vectorizer.fit_transform(x_train)
X_test = vectorizer.transform(x_test)

from sklearn.linear_model import SGDClassifier
clf = SGDClassifier(alpha=.0001, n_iter=50).fit(X_train, y_train)
y_pred = clf.predict(X_test)
