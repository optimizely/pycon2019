# Python Decorators

- Speaker: Rubin
- Advanced Talk

Note:  The author gave examples 1, 2, and 5... what are 3 and 4? Were they contained in 2?

## Lets decorate

Note: this is a warmup

@mydeco
def add(a, b):
  return a + b

- think of def as doing 2 things:
    1. create function object
    2. assign function object to name 'add'
- think like this, decorator adds...
    3. add = mydeco(add)


- Callables
  - Functions, Classes
  - a decorated function has 3 callables, function, decorator, and what is returned when you call `mydeco(add)`, typically a wrapper.

### Typical way to write a decorator

```
def mydeco(func):
  def wrapper(*args, **kwargs):
    return f'{func(*args, **kwargs)}!!!'
  return wrapper
```

- So the third callable is `wrapper`.


## Five Decorator Examples

### Example 1: Timing

- How long does it take a function to run?
- time.time() to get unix time now, subtract to get the difference

```
def logtime(func)
  def wrapper(*args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    total_time = time.time() - start_time()
    logging.info('put the 2 times here') # i simplified this for notes 
    return result
  return wrapper
```

- Here he abstracts the wrapper

```
def decorator(func):

  def wrapper(*args, **kwargs):

    pass  # do stuff

    return func(*args, **kwargs)

  return wrapper
```

# speaker implemented a @once_per_minute that only allows a function to run once per time interval
# speaker then modifies this to @once_per_interval which takes a value in seconds: @once_per_n(5)

```
def once_per_n(n):
  def middle(func):
    last_invoked = 0

    def wrapper(*args, **kwargs):
      nonlocal last_invoked
      if time.time() - last_invoked < n:
        raise CalledTooOftenError("Only __ has passed")

    # missing the rest
    # probably easy enough to tie these off...

```

### Example 2: Memoization

Cache the results of function calls so we don't need to call them again.

Over 50 year old technique.

If you have a function that always has the same result.

Look at the arguments and if you saw them before, return the cached value

SHA1, RSA, etc.

```
# this function is in my camera
def memoize(func)

#...

    # core cache is interesting too
    if args not in cache:
      # i guess args is just a tuple or other hashable, what about kwargs...
      # lol speaker predicted these and wants us to pickle args, kwargs, make them a tuple: pickle(tuple(args), tuple(kwargs)) ... sure
      cache[args] = func(*args, **kwargs)

```

### Example 5: Attributes

Give many objects the same attributes without inheritance.

Author hates multiple inheritance.

```
def better_repr(c):
  c.__repr__ = fancy_repr
  # don't even bother wrapping it
  return c
```




