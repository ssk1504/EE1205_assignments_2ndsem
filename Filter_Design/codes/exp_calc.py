from sympy import symbols, simplify

# Define symbolic variable s
s = symbols('s')

# Constants
omega0_val = 0.8312
B_val = 0.1331

# Define s_L in terms of s, omega0, and B
s_L = (s**2 + omega0_val**2) / (B_val * s)

# Given roots
s5 = -0.1411 - 0.9847j
s6 = -0.3407 - 0.4079j
s7 = -0.3407 + 0.4079j
s8 = -0.1411 + 0.9847j

# Define the given polynomial expression
polynomial_expr = 0.2411 / ((s_L - s5) * (s_L - s6) * (s_L - s7) * (s_L - s8))

# Simplify the expression
simplified_expr = simplify(polynomial_expr)

# Print the simplified expression
print("Simplified Polynomial in terms of s:")
print(simplified_expr)
