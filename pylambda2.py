
def LEFT(a):
    def f(b):
        return a
    return f

def RIGHT(a):
    def f(b):
        return b
    return f

def TRUE(x):
    return lambda y: x

def FALSE(x):
    return lambda y: y

# lets define boolean operators: NOT, OR, AND, NOR

def NOT(x):
    ''' we know x is a function because only functions exist
    '''
    return x(FALSE)(TRUE)

def AND(x):
    ''' AND(TRUE)(TRUE): TRUE  -- make a truth table

    given by speaker
    '''
    return lambda y: x(y)(x)

def OR(x):
    ''' either, but not both or neither
    '''
    return lambda y: x(x)(y)

def NOR(x):
    ''' only NOR(FALSE)(FALSE) is TRUE
    '''
    return lambda y: y  # not implemented




