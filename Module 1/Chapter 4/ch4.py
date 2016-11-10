
# toy CFG 
>>> from nltk import CFG
>>>toy_grammar = 
nltk.CFG.fromstring(
"""
  S -> NP VP  		 # S indicate the entire sentence   
  VP -> V NP              # VP is verb phrase the 
  V -> "eats" | "drinks"  # V is verb we are using only 2 verbs      in the example
  NP -> Det N   # NP is noun phrase (chunk that has noun in it)
  Det -> "a" | "an" | "the" # Det is determiner used in the sentences 
  N -> "president" |"Obama" |"apple"| "coke"  # N some example nouns 
   """)
>>> toy_grammar.productions()

# similarly a PCFG also can be built 

>>> from nltk import PCFG
>>> toy_pcfg1 = PCFG.fromstring("""
	S -> NP VP [1.0]
	NP -> Det N [0.5] | NP PP [0.25] | 'John' [0.1] | 'I' [0.15]
	Det -> 'the' [0.8] | 'my' [0.2]
	N -> 'man' [0.5] | 'telescope' [0.5]
	VP -> VP PP [0.1] | V NP [0.7] | V [0.2]
	V -> 'ate' [0.35] | 'saw' [0.65]
	PP -> P NP [1.0]
	P -> 'with' [0.61] | 'under' [0.39]
	""")
# ref :http://www.nltk.org/howto/grammar.html


# Regex parser

>>> chunk_rules=ChunkRule("<.*>+","chunk everything")
>>> import nltk
>>> from nltk.chunk.regexp import *
>>> reg_parser = RegexpParser('''
 		NP: {<DT>? <JJ>* <NN>*} # NP
  		 P: {<IN>}              # Preposition
             V: {<V.*>}             # Verb
  	      PP: {<P> <NP>}          # PP -> P NP
   	      VP: {<V> <NP|PP>*}  # VP -> V (NP|PP)*
  ''')
>>> test_sent="Mr. Obama played a big role in the Health insurance bill" 
>>> test_sent_pos=nltk.pos_tag(nltk.word_tokenize(test_sent))
>>> paresed_out=reg_parser.parse(test_sent_pos)

# Stanford Parser [Very useful]

>>>from nltk.parse.stanford import StanfordParser
>>>english_parser = StanfordParser('stanford-parser.jar', 'stanford-parser-3.4-models.jar')
>>>english_parser.raw_parse_sents(("this is the english parser test")

# Chunking 

>>>from nltk.chunk.regexp import *
>>>test_sent="The prime minister announced he had asked the chief government whip, Philip Ruddock, to call a special party room meeting for 9am on Monday to consider the spill motion."
>>>test_sent_pos=nltk.pos_tag(nltk.word_tokenize(test_sent))
>>>rule_vp = ChunkRule(r'(<VB.*>)?(<VB.*>)+(<PRP>)?', 'Chunk VPs')
>>>parser_vp = RegexpChunkParser([rule_vp],chunk_label='VP')
>>>print parser_vp.parse(test_sent_pos)    
>>>rule_np = ChunkRule(r'(<DT>?<RB>?)?<JJ|CD>*(<JJ|CD><,>)*(<NN.*>)+', 'Chunk NPs')
>>>parser_np = RegexpChunkParser([rule_np],chunk_label="NP")
>>>print parser_np.parse(test_sent_pos) 

# NP chunking (NER)

>>>f=open(# absolute path for the file of text for which we want NER)
>>>text=f.read()
>>>sentences = nltk.sent_tokenize(text)
>>>tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
>>>tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
>>>for sent in tagged_sentences:
>>>print nltk.ne_chunk(sent)

# Relation Extraction 

>>>import re
>>>IN = re.compile(r'.*\bin\b(?!\b.+ing)')
>>>for doc in nltk.corpus.ieer.parsed_docs('NYT_19980315'):
>>>	for rel in nltk.sem.extract_rels('ORG', 'LOC', doc, corpus='ieer', pattern = IN):
>>>print(nltk.sem.rtuple(rel))



