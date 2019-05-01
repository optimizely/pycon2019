
def cons(a, b):
  def select(m):
    if m == 0:
      return a
    elif m == 1:
      return b
  return select

def CAR(p):
  return p(0)

def CDR(p):
  return p(1)


# what if we do this with lambda calculus

#
# BEGIN prev definitions
#

def TRUE(x):
    return lambda y: x

def FALSE(x):
    return lambda y: y

SUCC = lambda n:(lambda f: lambda x: f(n(f)(x)))

# Church numerals
ZERO = lambda f: lambda x: x # don't call the function (this is just identity function)
ONE = lambda f: lambda x: f(x)
TWO = lambda f: lambda x: f(f(x))
THREE = lambda f: lambda x: f(f(f(x)))
FOUR = lambda f: lambda x: f(f(f(f(x))))

def incr(x):
    ''' this is illegal in our rules
    all will return 3:
    incr(0)
    incr(incr(0))
    incr(incr(incr(0)))
    THREE(incr(0))
    '''
    return x + 1 ### illegal in rules

ADD = lambda x: lambda y: y(SUCC)(x)
MUL = lambda x: lambda y: lambda f: y(x(f))

#
# END prev definitions
#

CONS =  lambda a: lambda b: (lambda s: s(a)(b))

p = CONS(2)(3)
p(TRUE)  # 2
p(FALSE)  # 3

CAR = lambda p: p(TRUE)
CDR = lambda p: p(FALSE)

CAR(p)  # 2
CDR(p)  # 3

CONS(2)(CONS(3)(4)) # function

# maybe we can use pairs to get the predecessor

# (0, 0)
# (1, 0)
# (2, 1)
# (3, 2)

def t(p):
    ''' lets make this in a lambda calculus valid function
    THREE(t)((0,0))
    a = (0,0)
    t(a)
    t(_)
    t(_)
    t(_)
    '''
    return (p[0]+1, p[0])

SUCC = lambda n:(lambda f: lambda x: f(n(f)(x)))

T = lambda p: CONS(SUCC(CAR(p)))(CAR(p))

# i think the problem is in  the definition of a since PRED takes T and works
a = FOUR(T)(CONS(ZERO)(ZERO))
CAR(a)(incr)(0)  # 4
CDR(a)(incr)(0)  # 3

PRED = lambda n: CDR(n(T)(CONS(ZERO)(ZERO)))

# THIS WORKS FINE - yay - so PRED is working, and T is working
a = FOUR(THREE)  # 3**4 = 81
b = PRED(a)  # 80 == 81-1
b(incr)(0)  # view it


# OK so how do we define 0?

# need subtraction
SUB = lambda x: lambda y: y(PRED)(x)

ZERO = lambda f: lambda x: x  # same definition, identity function
TWO = lambda f: lambda x: f(f(x))

ISZERO = lambda n: n(lambda f: FALSE)(TRUE)

# all worked
ISZERO(ZERO)
ISZERO(ONE)
ISZERO(TWO)

def fact(n):
    ''' factorial
    '''
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

# fact(4) returns 24

FACT = lambda n: ISZERO(n)(ONE)(MUL(n)(FACT(PRED(n))))  # max recursion depth

# python evaluates arguments first
# evaluative order not applicative order? see SICP first section.
# second path explodes in recursion
# eagerly evaluates arguments - possible to turn off but not in the way you may think!

#FACT(THREE) # maximum recursion depth exceeded, as expected

# another example of the problem in python

def choose(t, a, b):
    if t:
        return a
    else:
        return b

# note that this assigns the check to the first positional variable
choose(a < b, a, b)  # all good

a = 0
#choose(a != 0, a, 1/a)
# ZeroDivisionError: integer division or modulo by zero


# so lets make choose for lambda calculus

def choose(t, a, b):
    ''' this pulls us back from the brink
    '''
    if t:
        return a() # evaluate only if needed
    else:
        return b()

# this implementation of choose returns 0
choose(a==0, lambda: a, lambda: 1/a)

# so we need a new implementation of TRUE and FALSE:
# really not part of lambda calculus, just getting applicative order
LAZY_TRUE = lambda x: lambda y: x()  # added function call
LAZY_FALSE = lambda x: lambda y: y()  
ISZERO = lambda n: n(lambda f: LAZY_FALSE)(LAZY_TRUE) # rewrite for lazy

FACT = lambda n: ISZERO(n)(lambda: ONE)(lambda: MUL(n)(FACT(PRED(n))))

FACT(THREE)(incr)(0)  # return 6 - it worked!
