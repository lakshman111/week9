# Fibonacci Sequence:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....

# Recursive implementation:
# def fibonacci(n):
#   if n == 0:
#     return 0
#   if n == 1:
#     return 1
#
#   return fibonacci(n-1) + fibonacci(n-2)

# Iterative implementation
def fibonacci(n):
  if n == 0:
    return 0

  if n == 1:
    return 1

  current_value = 1
  prev_value = 0

  for position in range(2, n+1):
    new_value = current_value + prev_value
    prev_value = current_value
    current_value = new_value

  return current_value


position = 7  # should yield 13

value = fibonacci(position)

print("At position", position, "the value is", value)

# Fibonacci Sequence:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
