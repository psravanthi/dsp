[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

from __future__ import print_function, division

import thinkstats2
import thinkplot
import matplotlib

import scipy.stats
mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)
type(dist)
h1 = dist.cdf(177.8)
h2 = dist.cdf(185.4)
diff = h2-h1
print(diff)

output : 0.34209468294595308
>  34% of thhe US population is between 5'10" and 6'1'