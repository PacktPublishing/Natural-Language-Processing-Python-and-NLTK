>>>import nltk
>>>results=[]
>>>for sent_no,sentence in enumerate(nltk.sent_tokenize(news_content)):
>>>    no_of_tokens=len(nltk.word_tokenize(sentence))
>>>    # Let's do POS tagging
>>>    tagged=nltk.pos_tag(nltk.word_tokenize(sentence))
>>>    # Count the no of Nouns in the sentence
>>>    no_of_nouns=len([word for word,pos in tagged if pos in ["NN","NNP"] ])
>>>    #Use NER to tag the named entities.
>>>    ners=nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sentence)), binary=False)
>>>    no_of_ners= len([chunk for chunk in ners if hasattr(chunk, 'node')])
>>>    score=(no_of_ners+no_of_nouns)/float(no_of_toekns)
>>>    results.append((sent_no,no_of_tokens,no_of_ners,\
no_of_nouns,score,sentence))

>>>for sent in sorted(results,key=lambda x: x[4],reverse=True):
>>>    print sent[5]
