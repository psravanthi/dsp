[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

'''python
import nsfg as ns

def cohens_d(firsts, others):
    first_wt_m = firsts.totalwgt_lb.mean()
    other_wt_m = others.totalwgt_lb.mean()
    first_wt_v = firsts.totalwgt_lb.var()
    other_wt_v = others.totalwgt_lb.var()
    n1,n2 = len(firsts),len(others)
    diff = first_wt_m - other_wt_m
    pooled_var = (n1 * first_wt_v + n2 * other_wt_v) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    print(first_wt_m,other_wt_m)
    return d
preg = nsfg.ReadFemPreg()
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]
'''
Output:
First Baby mean: 7.201094430437772
Other Babies mean: 7.325855614973262 
First Baby variance: 2.0180273009157768 
Other Babies variance: 1.9437810258964572 
First Baby mean - Other Babies mean: -0.12476118453549034
CohenEffectSize: -0.088672927072602

There appears to be a small difference with the non-first babies a little heavier. Though the cohen's d is larger than cohen's d for pregnancy length, it is still small and indicates that the difference is not significant.
