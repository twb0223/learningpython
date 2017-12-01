'''
装饰器，带参数，不带参数，类似与aop，能在方法执行之前和之后进行一些操作。
'''

def dec1(func):
    def dec(*args):
        print('pre action')
        result = func(*args)
        print('aft action')
        return result

    return dec


def dec(name):
    def dec2(func):
        def dec(*args):
            print(name)
            print('pre action')
            result = func(*args)
            print('aft action')
            return result
        return dec
    return dec2

# @dec1
# def test1(name):
#     print(name)
#     return None


@dec('f2')
def test2(name):
    print(name)
    return None


test2('aaa')
