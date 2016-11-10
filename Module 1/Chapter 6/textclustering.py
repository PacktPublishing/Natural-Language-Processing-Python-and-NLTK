from sklearn.cluster import KMeans, MiniBatchKMeans
true_k=5
km = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
kmini = MiniBatchKMeans(n_clusters=true_k, init='k-means++', n_init=1,
                         init_size=1000, batch_size=1000, verbose=opts.verbose)
# we are using the same test,train data in TFIDF form as we did in text classification

km_model=km.fit(X_train)
kmini_model=kmini.fit(X_train)
print "For K-mean clustering "
clustering = collections.defaultdict(list)
for idx, label in enumerate(km_model.labels_):
        clustering[label].append(idx)
print "For K-mean Mini batch clustering "
clustering = collections.defaultdict(list)
for idx, label in enumerate(kmini_model.labels_):
        clustering[label].append(idx)
