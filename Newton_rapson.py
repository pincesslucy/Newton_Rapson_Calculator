#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sympy as sym
import numpy as np
import math


# In[3]:
#1변수,1식

x = sym.symbols('x')
y = x**2 - 3*x + 2 #식
yprime = y.diff(x)
m = float(input('x값'))
for i in range(1,5):
    y_result = y.subs(x,m)
    yprime_result = yprime.subs(x,m)
    change = -y_result / yprime_result
    result = m + change
    print('fx:', y_result, 'fx미분값:', yprime_result, '변화량:', change, i, '번째답:', result)
    m = result


# In[11]:
#2변수,2식

x = sym.symbols('x')
y = sym.symbols('y')

fx = 2*y - x**2 #식1
fx2 = y - sym.cos(x) #식2

fx_prime_x = fx.diff(x)
fx_prime_y = fx.diff(y)
fx2_prime_x = fx2.diff(x)
fx2_prime_y = fx2.diff(y)

m = float(input('x값'))
n = float(input('y값'))

for i in range(1,4):
    fx_prime_x_result = fx_prime_x.subs([(x,m), (y,n)])
    fx_prime_y_result = fx_prime_y.subs([(x,m), (y,n)])
    fx2_prime_x_result = fx2_prime_x.subs([(x,m), (y,n)])
    fx2_prime_y_result = fx2_prime_y.subs([(x,m), (y,n)])

    j = np.array([[fx_prime_x_result, fx_prime_y_result],
                 [fx2_prime_x_result, fx2_prime_y_result]], dtype = 'float')

    fx_result = fx.subs([(x,m), (y,n)])
    fx2_result = fx2.subs([(x,m), (y,n)])

    a = np.array([[fx_result],
                 [fx2_result]], dtype = 'float')

    change = np.dot(-1*np.linalg.inv(j), a)

    org_mn = np.array([[m],
                      [n]], dtype = 'float')

    result = org_mn + change

    m = result[0,0]
    n = result[1,0]
    
    print(i, '번째 변화량:\n', change, '\n', i, '번째답:\n', result, '\nfx,fx2 값:', fx.subs([(x,m), (y,n)]), fx2.subs([(x,m), (y,n)]))

