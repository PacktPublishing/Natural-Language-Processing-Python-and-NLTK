>>>import sys
>>>import datetime
>>>import pickle
>>>import nltk
>>>nltk.download('punkt')
>>>for line in sys.stdin:
>>>    line = line.strip()
>>>    id, content= line.split('\t')
>>>    tokens =nltk.word_tokenize(concat_all_text)
>>>    print '\t'.join([id,content,tokens])
