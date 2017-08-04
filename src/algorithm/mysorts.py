class mysorts:
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
        # 插入排序

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
    def quick_sort(self, lst):
        if len(lst) <= 1:
            return lst  # 如果a為一位數則直接傳回a
        l = [x for x in lst[1:] if x <= lst[0]]  # 輸出排序後的比a[0]小的數列
        r = [x for x in lst[1:] if x > lst[0]]  # 輸出排序後的比a[0]大的數列
        t = self.quick_sort(l) + [lst[0]] + self.quick_sort(r)
        return t

    # 选择排序
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
        print(f'Total {exchanges_count} swappings')
        return lst

    # 堆排序
    @staticmethod
    def heap_sort(lst):
        def sif_down(start, end):
            start.b = '''最大调整'''
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
