"""
    常用排序算法实现
"""
from collections import deque


class MySorts:
    """
    插入排序：T=O(n^2)
    1.从第一个元素开始，该元素可认为已经排序
    2.取下一个元素，在已经排序的元素序列中从后向前扫描
    3.如果该元素（已排序）大于新元素，该元素移到下一位置
    4.重复步骤3，直到找到已排序的元素小于或者等于新元素位置
    5.将新元素插入到该位置后
    6.重复步骤2-5
    """

    @staticmethod
    def insertion_sort(lst):
        if len(lst) == 1:
            return lst
        for i in range(1, len(lst)):
            temp = lst[i]
            j = i - 1
            while j >= 0 and temp < lst[j]:
                lst[j + 1] = lst[j]
                j -= 1
            lst[j + 1] = temp
        return lst

    @staticmethod
    def insert_sort(lst):
        n = len(lst)
        if n == 1:
            return lst
        for i in range(1, n):
            for j in range(i, 0, -1):
                if lst[j] < lst[j - 1]:
                    lst[j], lst[j - 1] = lst[j - 1], lst[j]
        return lst

    # quick_sort
    """
    快速排序：使用分治法策略来把一个序列分为连个序列 时间复杂度 avg:O(nlogn) bad:O(n^2)
    1.从序列中挑出一个元素，称为基准
    2.重新排序数列，所有比基准值小的元素摆放到基准前面，所有比基准值大的元素放到后面(相同则放任意一边)，在这个
        分区结束之后，该元素就处于数列中间位置。称之为分区操作。
    3.递归把将两边的数列排序
    
    """

    def quick_sort(self, lst):
        if len(lst) <= 1:
            return lst  # 如果a為一位數則直接傳回a
        l = [x for x in lst[1:] if x <= lst[0]]  # 輸出排序後的比a[0]小的數列
        r = [x for x in lst[1:] if x > lst[0]]  # 輸出排序後的比a[0]大的數列
        t = self.quick_sort(l) + [lst[0]] + self.quick_sort(r)
        return t

    # 选择排序
    """
    
    """

    @staticmethod
    def selection_sort(lst):
        n = len(lst)
        exchanges_count = 0
        for i in range(n - 1):
            min_index = i
            for j in range(i + 1, n):
                if lst[min_index] > lst[j]:
                    min_index = j
            if min_index != i:
                lst[min_index], lst[i] = lst[i], lst[min_index]
                exchanges_count += 1
            print('iteration #{}: {}'.format(i, lst))
        print(f'Total {exchanges_count} swap')
        return lst

    # 堆排序
    @staticmethod
    def heap_sort(lst):
        def sif_down(start, end):
            root = start
            while True:
                child = root * 2 + 1
                if child > end:
                    break
                if child + 1 <= end and lst[child] < lst[child + 1]:
                    child += 1
                if lst[root] < lst[child]:
                    lst[root], lst[child] = lst[child], lst[root]
                    root = child
                else:
                    break

            for start in range(len(lst) // 2, -1, -1):
                sif_down(start, len(lst) - 1)

    """
    归并排序
    """

    def merge_sort(self, lst):
        if len(lst) <= 1:
            return lst

        middle = int(len(lst) // 2)
        left = self.merge_sort(lst[:middle])
        right = self.merge_sort(lst[middle:])
        return self.__merge(left, right)

    @staticmethod
    def __merge(l, r):
        merged, l, r = deque(), deque(l), deque(r)
        while l and r:
            merged.append(l.popleft() if l[0] <= r[0] else r.popleft())  # deque popleft is also O(1)
        merged.extend(r if r else l)
        return list(merged)
