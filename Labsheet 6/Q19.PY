
from itertools import chain, combinations


def power_set(s):
  s_list = list(s)
  return set(
      frozenset(subset)
      for subset in chain.from_iterable(
          combinations(s_list, r) for r in range(len(s_list) + 1)
      )
  )


my_set = {1, 2, 3}
print("Original set:", my_set)
p_set = power_set(my_set)
print("Power set:")
for subset in p_set:
  print(set(subset))