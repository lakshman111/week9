# Binary search algorithm

def find(sorted_items, item):
  if len(sorted_items) == 0:
    return False

  if len(sorted_items) == 1:
    return sorted_items[0] == item

  middle = len(sorted_items)//2
  upper = sorted_items[middle:]
  lower = sorted_items[:middle]

  if sorted_items[middle] == item:
    return True
  if sorted_items[middle] > item:
    return find(lower, item)
  if sorted_items[middle] < item:
    return find(upper, item)
  
  # HOW THE PROFESSOR DID IT w/o recursion
  # start = 0
  # end = len(sorted_items) - 1

  # while start <= end:
  #   midpoint = (start + end)//2
  #   if sorted_items[midpoint] == item:
  #     return True

  #   if sorted_items[midpoint] > item:
  #     end = midpoint - 1
  #   else:
  #     start = midpoint + 1

  
  return False


numbers = list(range(80))

assert True == find(numbers, 20)
assert True == find(numbers, 70)
assert False == find(numbers, 101)

