def modelbuilding(smsdata,sms_labels):
	'''
	This is an example pipline to building a text classifier
	1. sampling
	2. TfidfVectorizer conversion
	3. building a naive_bayes model
	4. print the accuracy and other metrics
	5. print most relavent features 
	'''

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

def preprocessing(text):
    text = text.decode("utf8")
    # tokenize into words
    tokens = [word for sent in nltk.sent_tokenize(text) \
    for word in nltk.word_tokenize(sent)]

    # remove stopwords
    stop = stopwords.words('english')
    tokens = [token for token in tokens if token not in stop]

    # remove words less than three letters
    tokens = [word for word in tokens if len(word) >= 3]

    # lower capitalization
    tokens = [word.lower() for word in tokens]

    # lemmatize
    lmtzr = WordNetLemmatizer()
    tokens = [lmtzr.lemmatize(word) for word in tokens]
    preprocessed_text= ' '.join(tokens)

    return preprocessed_text

def main():
	smsdata = open('SMSSpamCollection') # check the structure of this file!
	smsdata_data = []
	sms_labels = []
	csv_reader = csv.reader(sms,delimiter='\t')
	for line in csv_reader:
	     # adding the sms_id 
	    sms_labels.append( line[0])
	    # adding the cleaned text We are calling preprocessing method 
	    sms_data.append(preprocessing(line[1]))

	sms.close() 
	# we are calling the model builing function here 
	modelbuilding(smsdata,sms_labels)   
if __name__ == '__main__':
	main()