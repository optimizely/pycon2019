# Lambda Calculus from the Ground Up

- Three Hour Seminar
- Pycon 2019: Wed, May 1st


## What is the lambda calculus (general question)

Carve all the python away, how much could you cut away and still have something to compute with?

- No packages/modules
- No objects
- No numbers/strings
- No ...
- No control flow
- No namespaces, global variables
    - we will use them for organization though

What if you can have functions but nothing else...

- There's no operators! No `+-*/` etc.
- Only single-argument functions (solves a lot of problems lol)
    - no zero argument functions
    - only return single argument function

**We know that everything going into our functions are functions because only functions exist.**

## Some interesting stuff

It's like we have compact styleguide that says we can use only single argument functions.

Currying is turning multiple argument functions into single argument functions.

```
def f(x):
  return x  # yes

def f(x):
  return x(x)  # yes

def f(x):
  ''' this is known as currying 
  '''
  def g(y):
    return x(y)
  return g
```

### Currying

Example of currying `add(x, y)` function. Instantiate with `add_curry(x)(y)`

'''
def add(x, y):
  return x + y
def add_curry(x):
  def f(y):
    return x + y
  return f
'''

## Lets make a switch

Two inputs, one output.

```
>>> LEFT('5V')
<function f at 0x10b3e9500>
>>> LEFT('5V')('gnd')
'5V'
>>> RIGHT('5V')('gnd')
'gnd'
```

### True and False are kind of arbitrary

```
def TRUE(x):
  return lambda y: x

def FALSE(x):
  return lambda y: y

>>> TRUE(0)(1)
0
>>> FALSE(1)(0)
1
```

### lets define boolean operators: NOT, OR, AND, NOR

We know that everything going into our functions are functions because only functions exist.

To implement these, use the replacement strategy with TRUE, FALSE functions

```
def NOT(x):
  ''' takes TRUE, FALSE methods: NOT(TRUE), NOT(FALSE)
  '''
  return x(FALSE)(TRUE)

def AND(x)
  return lambda y: x(y)(x)

def OR(x)
  return lambda y: x(x)(y)

```


### How about church numerals?

Challenge: how do you implement zero?

- We made a python function `incr` so we can see the result as a human number 
    - not a function representing a structure of functions
    - the sole purpose is for us to look at our work, not part of the lambda calculus
    - might make more sense to name it `print` or `show` or wrap it with that name

```
def incr(x):
  ''' give this a church numeral to see a human interpretable python number
  ONE(incr)(0)  # yields 1
  increment by whatever python number you give, 0 is identity
  '''
  return x + 1
```

```
# side note, unrelated: the implementation of zero is the exact implementation of FALSE(x)
# because it takes the SECOND curried value
ZERO = lambda f: lambda x: x  # you did not call the function, identity function
# Church numerals
ONE = lambda f: lambda x: f(x)
TWO = lambda f: lambda x: f(f(x))
THREE = lambda f: lambda x: f(f(f(x)))
FOUR = lambda f: lambda x: f(f(f(f(x))))
```

### CHALLENGE: Implement successor function, SUCC(x)

```
# SUCC(THREE) is FOUR
# SUCC(SUCC(THREE)) is FIVE
SUCC = lambda n:(lambda f: lambda x: f(n(f)(x))
```

### ADD, MUL

```
ADD = lambda x: lambda y: y(SUCC)(x)
# mul is left as exercise to the reader to fully grok
# speaker: i find this very hard to wrap my brain around
# it's like reading your four times f three times
MUL = lambda x: lambda y: lambda f: y(x(f))

>>> MUL(THREE)(FOUR)(incr)(0)
12
>>> ADD(THREE)(FOUR)(incr)(0)
7
```

## Digression: JSON object from hell

Say we are trying to navigate down into a nested json object / nested dict.

Same concept as repeated application of function on the result

> I thought you said this wouldn't be relevant work?

> You'll see: I'm going to make it irrelevant.

```

def getc(d):
  return d['a']['b']['c']

def getc(d):
  d = d.get('a')
  if d is not None:
    d = d.get('b')
  if d is not None:
    d = d.get('c')
  return d

# lots of code repetition! so lets clean it up...

def perhaps(d,  func):
  ''' helper function
  '''
  if d is not None:
    return func(d)
  else:
    return None

>>> perhaps(data, lambda d: d.get('a'))
