
import itertools

a = [1, 1, 3, 4, 4, 1]
for i in itertools.groupby(a):
    print(i[0])

def foo(lst):
    return list(i[0] for i in itertools.groupby(lst))

print(foo(a))