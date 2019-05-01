''' How compact can we get the function?

if we have two lambdas in a row, we can write it as one
'''


def TRUE(x):
    return lambda y: x

def FALSE(x):
    return lambda y: y


def AND(x):
    def f(y):
        return  x(y)(x)
    return f

def AND(x):
    return lambda y: x(y)(x)

AND = lambda x: lambda y: x(y)(x)


# wait does python allow this?
# AND = lambda x y: x(y)(x)  # not allowed in python?
AND = lambda xy: xyz
AND = lambda xy.xyx  # usually in the lambda calc the vars are 1 letter, e.g use unicode

AND(TRUE)(TRUE)
