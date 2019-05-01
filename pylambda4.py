
d =  {
        'a' : {
            'b' : {
                'c' : 42 }}}

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

perhaps(data, lambda d: d.get('a'))

# syntax error here, deal with later, concept is clear
perhaps(perhaps(data, lambda d: d.get('a')) \
        lambda d: d.get('b'))

perhaps(perhaps(perhaps(data, lambda d: d.get('a')) \
        lambda d: d.get('b')) \
        lambda d: d.get('c'))


class Perhaps:
    ''' PERHAPS this is an example of a monad 
    
    monad - it's associated with the 'turning the crank' concept
    hard to commit to it being a monad because the definition is pretty peculiar

    In some sense this is an extension of the church numeral idea: turning the crank
    '''
    def __init__(self, value):
        self.value = value

    def __rshift__(self, other):
        if self.value is not None:
            return Perhaps(other(self.value))
        else:
            return self
