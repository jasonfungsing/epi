__author__ = 'jasonfungsing'

# bit wise operation

#   The Operators:
#
#   x << y
#   Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y.
#   x >> y
#   Returns x with the bits shifted to the right by y places. This is the same as //'ing x by 2**y.
#   x & y
#   Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.
#   x | y
#   Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1.
#   ~ x
#   Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as -x - 1.
#   x ^ y
#   Does a "bitwise exclusive or". Each bit of the output is the same as the corresponding bit in x if that bit in y is 0, and it's the complement of the bit in x if that bit in y is 1.




a = 5 # 0101
b = a << 1
c = a >> 1
d = a & 1
e = a | 2
f = ~ a
g = a ^ 1

print("a: " + str(a) + " --> " + bin(a))
print("a << 1 : " + str(b) + " --> " + bin(b))
print("a >> 1 : " + str(c) + " --> " + bin(c))
print("a & 1 : " + str(d) + " --> " + bin(d))
print("a | 2 : " + str(e) + " --> " + bin(e))
print("~ a : " + str(f) + " --> " + bin(f))
print("a ^ 1 : " + str(g) + " --> " + bin(g))

