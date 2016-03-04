# Pascal's Problem: Dice Simulation
#
# Would it be profitable to bet that within 24 rolls of a pair of dice,
# that you would roll a double 6?
#
import random
got_double_sixes = 0
number_of_simulations = 10000

for i in range(number_of_simulations):
  for j in range(24):
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    if die1 == 6 and die2 ==6:
      got_double_sixes +=1
      break

print("It happened",got_double_sixes/number_of_simulations,"% of the time")