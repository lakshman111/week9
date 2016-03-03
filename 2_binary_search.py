# Binary search algorithm

def find(sorted_items, item):
  if len(sorted_items) == 0:
    return False

  if len(sorted_items) == 1:
    return sorted_items[0] == item

  # Uh oh... now what?
  #
  
  return False


numbers = list(range(80))

assert True == find(numbers, 20)
assert True == find(numbers, 70)
assert False == find(numbers, 101)
