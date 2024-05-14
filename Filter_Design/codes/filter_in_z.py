import sympy as sp

# Define symbols
s, z = sp.symbols('s z')

# Given transfer function
Ha_BP_s = 2.9195e-5 * s**4 / (s**8 + 0.1282*s**7 + 2.7895*s**6 + 0.2676*s**5 + 2.8990*s**4 + 0.1848*s**3 + 1.3315*s**2 + 0.0422*s + 0.2278)

# Perform substitution
substitution = ((1 - z**-1) / (1 + z**-1))
substituted_expression = Ha_BP_s.subs(s, substitution)

# Simplify the expression
simplified_expression = sp.simplify(substituted_expression)

# Print the result
print("Expression in z:")
print(simplified_expression)


