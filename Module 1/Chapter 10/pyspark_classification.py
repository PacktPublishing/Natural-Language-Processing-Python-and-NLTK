
# here I am assuming that we have pyspark configured on your hadoop cluster 
>>>from pyspark import SparkContext
>>>sc = SparkContext(appName="comment_classifcation")
#http://spark.apache.org/docs/0.7.3/api/pyspark/pyspark.context.SparkContext-class.html.
#The next thing is reading a tab delimited text file. Reading the file should be on HDFS. This file could be huge (~Tb/Pb):
>>>lines = sc.textFile("testcomments.txt")
#The lines are now a list of all the rows in the corpus:
>>>parts = lines.map(lambda l: l.split("\t"))
>>>corpus = parts.map(lambda row: Row(id=row[0], comment=row[1], class=row[2]))
#The parts is a list of fields as we have each field in the line delimited on “\t”.
#Let's break the corpus that has [ID, comment, class (0,1)] in the different RDD objects:
>>>comment = corpus.map(lambda row: " " + row.comment)
>>>class_var = corpus.map(lambda row:row.class)
#Once we have the comments, we need to do a process very similar to what we did in Chapter 6, Text Classification, where we used scikit to do tokenization, hash vectorizer and calculate TF, IDF, and tf-idf using a vectorizer.
#The following is the snippet of how to create tokenization, term frequency, and inverse document frequency:
>>>from pyspark.mllib.feature import HashingTF
>>>from pyspark.mllib.feature import IDF
# https://spark.apache.org/docs/1.3.0/mllib-feature-extraction.html 
>>>comment_tokenized = comment.map(lambda line: line.strip().split(" "))
>>>hashingTF = HashingTF(1000) # to select only 1000 features 
>>>comment_tf = hashingTF.transform(comment_tokenized)

>>>comment_idf = IDF().fit(comment_tf)
>>>comment_tfidf = comment_idf.transform(comment_tf)
#Will merge the class with the c tfidf RDD like this:
>>>finaldata = class_var.zip(comment_tfidf)
#We will do a typical test and train smapling
>>>train, test = finaldata.randomSplit([0.8, 0.2], seed=0)
#Let's perform the main classification commands, which are quite similar to scikit. We are using a logistic regression, which is widely used classifier. The pyspark.mllib provides you a variety of algorithms.
#For more information on pyspark.mllib visit https://spark.apache.org/docs/latest/api/python/pyspark.mllib.html

#The following is an example of logistic regression classifier:
>>>from pyspark.mllib.regression import LabeledPoint
>>>from pyspark.mllib.classification import NaiveBayes
>>>train_rdd = train.map(lambda t: LabeledPoint(t[0], t[1]))
>>>test_rdd = test.map(lambda t: LabeledPoint(t[0], t[1]))
>>>nb = NaiveBayes.train(train_rdd,lambda = 1.0)
>>>nb_output = test_rdd.map(lambda point: (NB.predict(point.features), point.label))
>>>print nb_output
