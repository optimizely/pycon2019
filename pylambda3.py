
# Church numerals
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

def p(t):
    ''' another radically different example
    '''
    return (t[0]+1, y[0])

#p((0,0))  # (1, 0)

a = FOUR(THREE)  ## what happens?  # returns 81 - does 3**4, exponentiation


''' 
returning a church number function, think about the API to a number
there is always and f and an x, you'll be returning a number
'''
SUCC = lambda n:(lambda f: lambda x: f(n(f)(x)))
SUCC(SUCC(FOUR))(incr)(0)
 
ADD = lambda x: lambda y: y(SUCC)(x)
MUL = lambda x: lambda y: lambda f: y(x(f))
