num = [1, 2, 3, 4, 5, 6]
print(num[6:])
print(num[:6])


print(7/2)
print(7//2)
print(7.0/2)
print(7.0//2)

list1 = [1,2,3]
list2 = [1,2,3]
print(list1 is list2)
print(list1 == list2)

str1 = 'abc'
str2 = 'abc'
print(str2 is str1)
print(str2 == str1)



x = 1

def fun(x):
    x += 1
    return x

fun(x)
print(fun(x))
print(x)


list2 = [1, 3, 6, 5, 2]
for i in list2.sort():
    print(i)