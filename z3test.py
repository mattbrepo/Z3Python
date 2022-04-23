from z3 import *  # pip install z3-solver

# problem from a math teacher
#
#    3     x     y
#   --- - --- = ---
#    2     3     4
#
x, y = Ints('x y')
s = Solver()
s.add(x >= 0, y >= 0, RealVal('3/2') - RealVal('1/3') * x - RealVal('1/4') * y == 0)
while s.check() == sat:
  print(s.model())
  s.add(Or(x != s.model()[x], y != s.model()[y])) # find a new solution

# problem from a scientific paper I was dealing with
#
# (3-h)(2-h) + R = 4
#
h, R = Ints('h R')
s = Solver()
s.add(h >= 0)
s.add(R >= 0)

s.add((3 - h) * (2 - h) + R == 4)
while s.check() == sat:
  print(s.model())
  s.add(Or(h != s.model()[h], R != s.model()[R])) # find a new solution

#
# Examples from https://ericpony.github.io/z3py-tutorial/guide-examples.htm
#

# find one solution
x, y, z = Ints('x y z')
s = Solver()
s.add(3*x + 2*y - z == 1)
s.add(2*x - 2*y + 4*z == -2)
s.add(x + y + z == 222)

s.check()
print(s.model())

# simplify an equation
x, y = Ints('x y')
print(simplify(x + 1 + y + x + 1))

# simplify an equation
x = Int('x')
print(simplify(5*(2+x)+3*(5*x+4)-(x**2)**2))

# test with Real
x, y, z = Reals('x y z')
s = Solver()
s.add(x > 1, y > 1, x + y > 3, z - x < 10)
print(s.check())

m = s.model()
print("x = %s" % m[x])
print("y = %s" % m[y])
print("z = %s" % m[z])

# test with Real with 'unknown' result
#x = Real('x')
#s = Solver()
#s.add(2**x == 3)
#print(s.check()) # cannot solve non-polynomial (but there are workarounds...check website)

