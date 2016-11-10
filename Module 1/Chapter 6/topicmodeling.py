from gensim import corpora, models, similarities
from itertools import chain
import nltk
from nltk.corpus import stopwords
from operator import itemgetter
import re
documents = [document for document in sms_data]
stoplist = stopwords.words('english')
texts = [[word for word in document.lower().split() if word not in stoplist] \
for document in documents]
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
si = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=100)
#lsi.print_topics(20)
n_topics = 5
lda = models.LdaModel(corpus_tfidf, id2word=dictionary, num_topics=n_topics)
for i in range(0, n_topics):
		temp = lda.show_topic(i, 10)
		terms = []
		for term in temp:
			terms.append(term[1])
			print "Top 10 terms for topic #" + str(i) + ": "+ ", ".join(terms)
