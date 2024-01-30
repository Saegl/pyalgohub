a = -7
b = 2

# division between integers return float
assert a / b == -3.5

# division with double '/' returns floor (int)
# truncates towards negative infinity
assert a // b == -4

# this one truncates decimal part
# truncates towards zero
assert int(a / b) == -3

# For x > 0 and y > 0
x = 10
y = 3
assert int(x / y) == x // y


quotient, remainder = divmod(a, b)
# just a shorthand for
quotient2, remainder2 = a // b, a % b
assert quotient == quotient2
assert remainder == remainder2

