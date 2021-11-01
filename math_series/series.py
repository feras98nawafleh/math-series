def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

def lucas(n):
  if n == 1:
    return 1
  if n == 2:
    return 2

  return lucas(n - 1) + lucas(n - 2)

def sum_series(n, option1 = 0, option2 = 1):
  if n < 0:
    return "Can't perform on negative numbers"
  if n == 0:
    return option1
  if n == 1:
    return option2
  return (
    sum_series(n - 1, option1, option2) + sum_series(n - 2, option1, option2)
  )

# print(fibonacci(10))
# print(lucas(10))
print(sum_series(10, 2, 3))

