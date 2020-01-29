'''
https://www.youtube.com/watch?v=spUNpyF58BY
'''
from sympy import *


class main:
    def __init__(self):
        self.x = Symbol('x')
        self.funct = sin(self.x*pi)+cos(self.x*(pi)/(1.5))
        self.interv = 20
        self.delt = 2
        self.start()

    def start(self):
        f,t1,t2 = symbols('f t1 t2')
        t1 = 0
        t2 = self.interv
        expr = 1/(t2-t1) * Integral(self.funct*E**(-2*pi*I*(1/f)*self.x),(self.x,t1,t2))
        print (expr)
        res = []
        for u in range(self.interv,0,-1):
            q = expr.subs(f,u)
            res.append(q.evalf())
        res = [sqrt(re(t)**2 + im(t)**2) for t in res[::-1]]
        a = []
        for u in range(self.delt):
            a.append(res.index(max(res))+1)
            res  = res[:res.index(max(res))]+[0]+res[res.index(max(res))+1:]
        print (a)
        
if __name__ == "__main__":
    init_printing(use_unicode=True) 
    main()
