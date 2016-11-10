>>>import matplotlib
>>>import matplotlib.pyplot as plt
>>>import numpy
>>>stockCSCO = stockdata_new.query('stock=="CSCO"')
>>>stockCSCO.head()
>>>from matplotlib import figure
>>>plt.figure()
>>>plt.scatter(stockdata_new.index.date,stockdata_new.volume)
>>>plt.xlabel('day') # added the name of the x axis
>>>plt.ylabel('stock close value') # add label to y-axis
>>>plt.title('title') # add the title to your graph
>>>plt.savefig("matplot1.jpg") # savefig in local

# subplot 
>>>plt.subplot(2, 2, 1)
>>>plt.plot(stockAA.index.weekofyear, stockAA.open, 'r--')
>>>plt.subplot(2, 2, 2)
>>>plt.plot(stockCSCO.index.weekofyear, stockCSCO.open, 'g-*')
>>>plt.subplot(2, 2, 3)
>>>plt.plot(stockAA.index.weekofyear, stockAA.open, 'g--')
>>>plt.subplot(2, 2, 4)
>>>plt.plot(stockCSCO.index.weekofyear, stockCSCO.open, 'r-*')
>>>plt.subplot(2, 2, 3)
>>>plt.plot(x, y, 'g--')
>>>plt.subplot(2, 2, 4)
>>>plt.plot(x, y, 'r-*')
>>>fig.savefig("matplot2.png")

>>>fig, axes = plt.subplots(nrows=1, ncols=2)
>>>for ax in axes:
>>>     ax.plot(x, y, 'r')
>>>     ax.set_xlabel('x')
>>>     ax.set_ylabel('y')
>>>     ax.set_title('title');

>>>fig = plt.figure()
>>>axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # left, bottom, width,
height (range 0 to 1)
>>>axes.plot(x, y, 'r')

>>>fig = plt.figure()
>>>ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
>>>ax.plot(stockAA.index.weekofyear,stockAA.open,label="AA")
>>>ax.plot(stockAA.index.weekofyear,stockCSCO.open,label="CSCO")
>>>ax.set_xlabel('weekofyear')
>>>ax.set_ylabel('stock value')
>>>ax.set_title('Weekly change in stock price')
>>>ax.legend(loc=2); # upper left corner
>>>plt.savefig("matplot3.jpg")

# scatter plot 
>>>import matplotlib.pyplot as plt
>>>plt.scatter(stockAA.index.weekofyear,stockAA.open)
>>>plt.savefig("matplot4.jpg")
>>>plt.close()
# bar plot 
>>>n = 12
>>>X = np.arange(n)
>>>Y1 = np.random.uniform(0.5, 1.0, n)
>>>Y2 = np.random.uniform(0.5, 1.0, n)
>>>plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
>>>plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

# 3d plot 
>>>from mpl_toolkits.mplot3d import Axes3D
>>>fig = plt.figure()
>>>ax = Axes3D(fig)
>>>X = np.arange(-4, 4, 0.25)
>>>Y = np.arange(-4, 4, 0.25)
>>>X, Y = np.meshgrid(X, Y)
>>>R = np.sqrt(X**2+ + Y**2)
>>>Z = np.sin(R)
>>>ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='hot')