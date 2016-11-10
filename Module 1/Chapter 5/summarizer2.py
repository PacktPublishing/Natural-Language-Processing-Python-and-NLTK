>>>import nltk
>>>from sklearn.feature_extraction.text import TfidfVectorizer
>>>results=[]
>>>sentences=nltk.sent_tokenize(news_content)
>>>vectorizer = TfidfVectorizer(norm='l2',min_df=0, use_idf=True, smooth_idf=False, sublinear_tf=True)
>>>sklearn_binary=vectorizer.fit_transform(sentences)
>>>print countvectorizer.get_feature_names()
>>>print sklearn_binary.toarray()
>>>for sent_no,i in enumerate(sklearn_binary.toarray()):
>>>	results.append(sent_no,i.sum()/float(len(i.nonzero()[0])))

