import math
import snoop

@snoop
def xabc(z, y):
    return math.log2(z)/math.log2(y)
def cd(y,a,c,n):
    return y*n/a*c
def example(a,b,c,d):
    a=xabc(a,b)
    b=xabc(b,a)
    c=xabc(c,d)
    d=xabc(c,d)
    return cd(a,b,c,d)
p=10
q=5
r=3
s=1
example(p,q,r,s)