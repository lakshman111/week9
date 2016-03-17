# Linear search algorithm

def find(items, item):
  # 1. start at the first item of the list
  # 2. is it the item we're looking for?
  # 3. If so, we're done!
  # 4. If not, go to the next item, and go to step 2.

  # for i in range(len(items)):
  #   if item == items[i]:
  #     return True

  # return False

  # better way he wrote it
  # this is better because the program stops when it finds it
  position = 0
  found = False
  while (position < len(items) and not found):
    if (items[position] == item):
      found = True
    position += 1

  return found

numbers = list(range(80))
assert True == find(numbers, 20)
assert True == find(numbers, 70)
assert False == find(numbers, 101)
