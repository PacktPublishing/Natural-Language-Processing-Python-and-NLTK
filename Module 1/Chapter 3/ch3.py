# POS tagging 
>>>import nltk
>>>from nltk import word_tokenize
>>>s="I was watching TV"
>>>print nltk.pos_tag(word_tokenize(s))

# all nouns

>>>tagged=nltk.pos_tag(word_tokenize(s))
>>>allnoun=[word for word,pos in tagged if pos in ['NN','NNP'] ]

# Stanford POS tagger 

>>>from nltk.tag.stanford import POSTagger
>>>import nltk
>>>stan_tagger=POSTagger('models/english-bidirectional-distdim.tagger','standford-postagger.jar')
>>>tokens =nltk.word_tokenize(s)
>>>stan_tagger.tag(tokens)

# POS tags freq distribtuion
>>>from nltk.corpus import brown
>>>import nltk
>>>tags = [tag for (word, tag) in brown.tagged_words(categories='news')]
>>>print nltk.FreqDist(tags)

# default tagger
>>>brown_tagged_sents = brown.tagged_sents(categories='news')
>>>default_tagger = nltk.DefaultTagger('NN')
>>>print default_tagger.evaluate(brown_tagged_sents)

# N-gram taggers

>>>from nltk.tag import UnigramTagger
>>>from nltk.tag import DefaultTagger
>>>from nltk.tag import BigramTagger
>>>from nltk.tag import TrigramTagger
# we are dividing the data into a test and train to evaluate our taggers.
>>>train_data= brown_tagged_sents[:int(len(brown_tagged_sents) * 0.9)]
>>>test_data= brown_tagged_sents[int(len(brown_tagged_sents) * 0.9):]
>>>unigram_tagger = UnigramTagger(train_data,backoff=default_tagger)
>>>print unigram_tagger.evaluate(test_data)
>>>bigram_tagger= BigramTagger(train_data, backoff=unigram_tagger)
>>>print bigram_tagger.evaluate(test_data)
>>>trigram_tagger=TrigramTagger(train_data,backoff=bigram_tagger)
>>>print trigram_tagger.evaluate(test_data)

# Regex tagger 

>>>from nltk.tag.sequential import RegexpTagger
>>>regexp_tagger = RegexpTagger(
         [( r'^-?[0-9]+(.[0-9]+)?$', 'CD'),   # cardinal numbers
          ( r'(The|the|A|a|An|an)$', 'AT'),   # articles
          ( r'.*able$', 'JJ'),                # adjectives
          ( r'.*ness$', 'NN'),         # nouns formed from adj
          ( r'.*ly$', 'RB'),           # adverbs
          ( r'.*s$', 'NNS'),           # plural nouns
          ( r'.*ing$', 'VBG'),         # gerunds
          (r'.*ed$', 'VBD'),           # past tense verbs
          (r'.*', 'NN')                # nouns (default)
          ])
>>>print regexp_tagger.evaluate(test_data)



# NER tagger 
>>>import nltk
>>>from nltk import ne_chunk
>>>from nltk import word_tokenize
>>>sent = "Mark is studying at Stanford University in California"
>>>print(ne_chunk(nltk.pos_tag(word_tokenize(sent)), binary=False))

# NER stanford tagger 

>>>from nltk.tag.stanford import NERTagger
>>>st = NERTagger('<PATH>/stanford-ner/classifiers/all.3class.distsim.crf.ser.gz',...               '<PATH>/stanford-ner/stanford-ner.jar')
# <PATH> will be the relative path where you downloaded the tagger 
#http://nlp.stanford.edu/software/ 
