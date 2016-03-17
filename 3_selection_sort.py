# https://en.wikipedia.org/wiki/Selection_sort
import random

def sort(items):
  # arbitrarily pick the first item as the min
  for position in range(0, len(items)):
    min_position_so_far = position

    # then iterate throught the rest of the list
    # reason it is nested is becuase it is building up order
    # a good visualization on the link above
    for z in range(position+1, len(items)):
      if items[z] < items[min_position_so_far]:
        min_position_so_far = z

    # swap the minimum into the current position
    if position != min_position_so_far:
      temp = items[position]
      items[position] = items[min_position_so_far]
      items[min_position_so_far] = temp

  return items

numbers = list(range(10))
random.shuffle(numbers)
print("Will sort this list:", numbers)

sorted_numbers = sort(numbers)
print("The list should now be sorted:", sorted_numbers)

assert list(range(10)) == sorted_numbers
