import sys
import pickle
import nltk
for line in sys.stdin:
    line = line.strip()
    id, content,topics = line.split('\t')
    print '\t'.join([id,content,topics])
