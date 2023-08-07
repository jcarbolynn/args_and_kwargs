def add(*args):
  # print(type(args))
  # args is a tuple
  sum = 0
  for n in args:
    sum += n
  return sum

add(4,5,6,7,8)

def calculate(n, **kwargs):
  # kwargs is a dictionary, each key word argument and their values
  print(kwargs)
  for key, value in kwargs.items():
    print(key, value)
  print(kwargs['add'], kwargs['multiply'])
  # lets you look through inputs, find the one you want, and do something with it
  n += kwargs['add']
  n *= kwargs['multiply']
  print(n)
