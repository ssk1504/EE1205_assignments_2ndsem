import sympy as sp
s = sp.symbols('s')
x = sp.symbols('x')
o = 0.8312
B = 0.1331

s5 = -0.1411 + 0.9847j
s6 = -0.3407 + 0.4079j
s7 = -0.3407 - 0.4079j
s8 = -0.1411 - 0.9847j
Dr = sp.expand((s-s5)*(s-s6)*(s-s7)*(s-s8))
print(f"{Dr}")
s = (x**2 + o**2)/(B*x)
print('\n')
Dr_2 = sp.expand((s-s5)*(s-s6)*(s-s7)*(s-s8))
print(f"{Dr_2}") #coefficient of x^8 in order to normalize it.
print('\n')
print((0.2411*1.1187)/(9238.45426026515))
