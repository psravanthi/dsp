[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)
```python
#Read the female respondent file.
%matplotlib inline
import chap01soln
resp = chap01soln.ReadFemResp()
#Make a PMF of numkdhh, the number of children under 18 in the respondent's household
import thinkstats2
pmf = thinkstats2.Pmf(resp.numkdhh)

def BiasPmf(pmf, label=''):
    """Returns the Pmf with oversampling proportional to value.

    If pmf is the distribution of true values, the result is the
    distribution that would be seen if values are oversampled in
    proportion to their values; for example, if you ask students
    how big their classes are, large classes are oversampled in
    proportion to their size.

    Args:
      pmf: Pmf object.
      label: string label for the new Pmf.

     Returns:
       Pmf object
    """
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf
biased = BiasPmf(pmf, label='biased')
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased])
thinkplot.Show()
```
[[statistics/actual vs biased.png]]

```python
pmf.Mean()
biased.Mean()
```
> Output :
Actual Mean: 1.0242051550438309
Biased Mean : 2.4036791006642821

> Observations:
As expected, class size paradox can be observed. There is no representation for the families with zero children and families with more children are over sampled. 
