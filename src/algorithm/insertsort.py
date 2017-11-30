source = [92, 77, 67, 8, 6, 84, 55, 85, 43, 67]

# for index in range(1, len(source)):
#     current_val = source[index]
#     position = index

#     while position > 0 and source[position + 1] > current_val:
#         source[position] = source[position - 1]
#         position -= 1

#     source[position] = current_val
#     print(source)

# for i in range(1, len(source)):
#     while i > 0 and source[i] < source[i - 1]:
#         tmp = source[i]
#         source[i] = source[i - 1]
#         source[i - 1] = tmp
#         i -= 1
#         print(source)


def Quick_sort(arry, left, right):
    '''
    '''
    if left >= right:
        return
    low = left
    high = right
    key = arry[low]

    while low < high:
        while low < high and array[high] > key:
            high -= 1

        arry[low] = arry[high]
        arry[high] = key

        while low < high and arry[low] <= key:
            low += 1

        arry[high] = arry[low]
        arry[low] = key

    Quick_sort(arry, left, low - 1)
    Quick_sort(arry, low + 1, right)


if __name__ == '__main__':

    array = [96, 14, 10, 9, 6, 99, 16, 5, 1, 3, 2, 4, 1, 13, 26, 18, 2, 45, 34, 23]
    # array = [8,4,1, 14, 6, 2, 3, 9,5, 13, 7,1, 8,10, 12]
    print("before sort:", array)
    Quick_sort(array, 0, len(array) - 1)

    print("-------final -------")
    print(array)