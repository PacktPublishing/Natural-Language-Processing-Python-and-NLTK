import sys
import pickle
import nltk
for line in sys.stdin:
    line = line.strip()
    id, content = line.split('\t')
    tokens =nltk.word_tokenize(concat_all_text)
    print '\t'.join([id,content,tokens])
