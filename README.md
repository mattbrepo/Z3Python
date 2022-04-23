# Z3Python
Test of [Z3 Theorem Prover](https://en.wikipedia.org/wiki/Z3_Theorem_Prover) with Python

**Language: Python**

**Start: 2021**

## Why
I wanted to test Microsoft Z3 Theorem Prover.

## Example
A friend of mine is a teacher in a school for kids from 10 to 13 years old. He presented to me a math problem that was quite difficult for his students:

```
  3     x     y
 --- - --- = ---
  2     3     4
```

He wanted them to apply a bit of intuition to find at least one solution assuming x and y to be integer greater than or equal to zero. 

I tried and I quickly found a solution. Later using Z3, I found out that there are two solutions:

```python
x, y = Ints('x y')
s = Solver()
s.add(x >= 0, y >= 0, RealVal('3/2') - RealVal('1/3') * x - RealVal('1/4') * y == 0)
while s.check() == sat:
  print(s.model())
  s.add(Or(x != s.model()[x], y != s.model()[y])) # find a new solution
  
[y = 6, x = 0]
[y = 2, x = 3]
```
