
# please refer to code modelbuilding.py in ch 6 and just serialize the vectorizer and mode
# object using joblib.dump
vectorizer = TfidfVectorizer(sublinear_tf=True, min_df=in_min_df,
stop_words='english', ngram_range=(1,2), max_df=in_max_df)
joblib.dump(vectorizer, "vectorizer.pkl", compress=3)
clf = GaussianNB().fit(X_train,y_train)
joblib.dump(clf, "classifier.pkl")