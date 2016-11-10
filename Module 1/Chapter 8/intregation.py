>>>from scipy.integrate import quad, dblquad, tplquad
>>>def f(x):
>>>     return x
>>>
>>>x_lower = = 0 # the lower limit of x
>>>x_upper = = 1 # the upper limit of x
>>>val, abserr = = quad(f, x_lower, x_upper)
>>>print val,abserr
>>> 0.5 , 5.55111512313e-15
