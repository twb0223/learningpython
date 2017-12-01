'''
上下文管理器，要实现__enter__ 和__exit__方法
'''

class openfile(object):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.f = open(self.filename, self.mode)
        return self.f

    def __exit__(self, type, value, tb):
        self.f.close()
        return False


with openfile('my.txt', 'w') as f:
    f.write('hi \n')
    f.write('nihao')