>>>import pandas as pd
>>># Please provide the absolute path of the input file
>>>data = pd.read_csv("PATH\\iris.data.txt",header=0")
>>>data.head()

>>>data = pd.read_csv("PATH\\iris.data.txt", names=["sepal length"," sepal\
width", "petal length", "petal width", "Cat"], header=None)
>>>data.head()

>>>data.describe()

>>>sepal_len_cnt=data['sepal length'].value_counts()
>>>sepal_len_cnt
>>>data['Iris-setosa'].value_counts()
>>>data['Iris-setosa'] == 'Iris-setosa'
>>>sntsosa=data[data['Cat'] == 'Iris-setosa']
>>>sntsosa[:5]

# series data

>>>import pandas as pd
>>>stockdata = pd.read_csv("C:\\Users\\a549369\\Documents\\book\\dow_
jones_index.data",parse_dates=['date'], index_col=['date'], nrows=100)
>>>>stockdata.head()
>>>max(stockdata['volume'])
>>>max(stockdata['percent_change_price'])
>>>stockdata.index
>>>stockdata.index.day
>>>stockdata.index.month
>>>stockdata.index.year
>>>import numpy as np
>>>stockdata.resample('M', how=np.sum)

#transformation
>>>stockdata.drop(["percent_change_volume_over_last_wk"],axis=1)

>>>stockdata_new = pd.DataFrame(stockdata, columns=["stock","open","high"
,"low","close","volume"])
>>>stockdata_new.head()
>>>stockdata["previous_weeks_volume"] = 0

# noisy data
>>>import numpy
>>>stockdata_new.open.describe()
>>>stockdata_new.open = stockdata_new.open.str.replace('$', '').convert_
objects(convert_numeric=True)
>>>stockdata_new.close = stockdata_new.close.str.replace('$', '').
convert_objects(convert_numeric=True)
>>>(stockdata_new.close - stockdata_new.open).convert_objects(convert_
numeric=True)
>>>stockdata_new.open.describe()
>>>stockdata_new['newopen'] = stockdata_new.open.apply(lambda x: 0.8 * x)
>>>stockdata_new.newopen.head(5)
>>>stockAA = stockdata_new.query('stock=="AA"')
>>>stockAA.head()
