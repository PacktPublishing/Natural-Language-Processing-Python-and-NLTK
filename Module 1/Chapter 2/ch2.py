# csv load 
>>>import csv
>>>with open('example.csv','rb')  as f:
>>>    reader=csv.reader(f,delimiter=',',quotechar='"')
>>>    for line in reader :
>>>        print line[1]  # assuming the second field is the raw sting

# json load 
>>>import json
>>>jsonfile=open('example.json')
>>>data=json.load(jsonfile)
>>>print data['string']

# sentence splitter 

>>>inputstring = ' This is an example sent. The sentence splitter will split on sent markers. Ohh really !!'
>>>from nltk.tokenize import sent_tokenize
>>>all_sent=sent_tokenize(inputstring)
>>>print all_sent
>>>[' This is an example sent', 'The sentence splitter will split on markers.','Ohh really !!']

>>>import nltk.tokenize.punkt
>>>tokenizer =nltk.tokenize.punkt.PunktSentenceTokenizer()

# word tokenizer
>>>s ="Hi Everyone !    hola gr8" # simplest tokenizer
>>>print s.split()

>>>from nltk.tokenize import word_tokenize
>>>word_tokenize(s)

>>>from nltk.tokenize import regexp_tokenize, wordpunct_tokenize, blankline_tokenize
>>>regexp_tokenize(s, pattern='\w+')

>>>regexp_tokenize(s, pattern='\d+')

>>>wordpunct_tokenize(s)
>>>blankline_tokenize(s)

#Porter stemmer
>>>from nltk.stem import PorterStemmer # import Porter stemmer
>>>from nltk.stem.lancaster import LancasterStemmer
>>>from nltk.stem.Snowball import SnowballStemmer
>>>pst=PorterStemmer()   # create obj of the PorterStemmer
>>>lst = LancasterStemmer() # create obj of LancasterStemmer
>>>lst.stem("eating")
>>>pst.stem("shopping")

#Lemmatizer
>>>from nltk.stem import WordNetLemmatizer
>>>wlem=WordNetLemmatizer()
>>>wlem.lemmatize("ate")

# stop word 

>>>from nltk.corpus import stopwords
>>>stoplist=stopwords.words('english') # config the language name
>>>text = "This is just a test"
>>>cleanwordlist=[word for word in text.split() if word not in stoplist]


# rare word removal 

>>>freq_dist=nltk.FreqDist(token)
>>>rarewords =freq_dist.keys()[-50:]
>>>after_rare_words= [ word for word in token not in rarewords]

# spell check

>>>from nltk.metrics import edit_distance
>>>edit_distance(“rain”,”shine”)


