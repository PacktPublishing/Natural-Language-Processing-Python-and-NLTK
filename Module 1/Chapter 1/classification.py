import sys
import pickle
import sklearn
from sklearn.externals import joblib

clf = joblib.load('classifier.pkl')
vectorizer = joblib.load('vectorizer.pkl')

for line in sys.stdin:
    line = line.strip()
    id, content= line.split('\t')
    X_test = vectorizer.transform([str(content)])
  
    prob = clf.predict_proba(X_test)
    pred = clf.predict (X_test)
    prob_score =prob[:,1]
    print '\t'.join([id, content,pred,prob_score])
