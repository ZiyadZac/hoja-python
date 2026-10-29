def outer(x):
  def inner(y):
    return x+y
  return inner

add5=outer(5)
print(add5(10))