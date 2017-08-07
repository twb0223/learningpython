import time
from collections import deque

from src.algorithm.mysorts import MySorts

lst1 = [123, 24, 234, 444, 562, 2, 45, 73, 36]

my_sorts = MySorts()

# print(my_sorts.quick_sort(lst1))
# print(my_sorts.selection_sort(lst1))
# start = time.clock()
#
# print(my_sorts.merge_sort(lst1))
#
# end = time.clock()
#
# print(end - start)
lst2 = deque(lst1)

print(lst2.pop())
print(lst2)
print(lst2.popleft())
print(lst2)
