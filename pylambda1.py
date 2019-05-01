'''
'''


f = lambda x: 3*x + 1

f(2)  # eli5 - you replace the x with the 2
f(4)


'''
def f(x):
    return x
def f(x):
    return x(x)
'''


def f(x):
    def g(y):
        return x(y)
    return g


