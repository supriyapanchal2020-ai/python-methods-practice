# Logical Operators - and, or, not

a = 10
b = 20

# and - both must be True
print("and:", a > 5 and b > 15)

# or - any one True is enough
print("or:", a > 15 or b > 15)

# not - opposite
print("not:", not (a > 5))

# Real example
age = 20
has_id = True
print("Can enter:", age >= 18 and has_id)