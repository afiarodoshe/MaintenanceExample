import math
from sys import settrace

def my_tracer(frame, event, args=None):
    code = frame.f_code
    func_name = code.co_name
    line_no = frame.f_lineno
    if((event == 'return') and (func_name == 'example') or (func_name == 'xabc') or (func_name == 'cd')):
        print(f"A {event} encountered in {func_name}() at line number {line_no}")
    return my_tracer

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

settrace(my_tracer)
p=10
q=5
r=3
s=10
example(p,q,r,s)

settrace(None)