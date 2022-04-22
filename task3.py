import ast
from _ast import arguments


class Visitor(ast.NodeVisitor):
    def visit_FunctionDef(self, node):
        print('\tFunction: {} in line {}'.format(node.name,node.lineno))
        self.generic_visit(node)

    def visit_Name(self, node):
        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
            print('\tVariable: {} in line {}'.format(node.id, node.lineno))
        self.generic_visit(node)





parsed=ast.parse('''import math

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
example(p,q,r,s)''')

Visitor().visit(parsed)