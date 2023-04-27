def fun_transfer(_fun_):

    def __fun__(self, *args, **kwargs):
        return _fun_(self.__value__, *args, **kwargs)

    return __fun__


def init_transfer(_init_):

    def __init__(self, *args, **kwargs):
        self.__value__ = _init_(*args, **kwargs)

    return __init__


not_transfer_fun = ['__class__', '__new__', '__init__', '__getattribute__', '__setattr__']

def __getattribute__(self, item):
    print(0)
    if item == '__value__':
        return super().__getattribute__('__value__')
    return getattr(super().__getattribute__('__value__'), item)

def __setattr__(self, item, value):
    if item == '__value__':
        if not hasattr(self, '__value__'):
            super().__setattr__('__value__', None)
        if self.__value__ is None or isinstance(value, type(self.__value__)):
            super().__setattr__('__value__', value)
        else:
            raise ValueError('类型不匹配')
    else:
        setattr(super().__getattribute__('__value__'), item, value)


class A:

    # def __getattr__(self, item):
    #     print(1)

    def __init_subclass__(cls, **kwargs):
        for fun_name in dir(cls):
            if fun_name not in not_transfer_fun and callable(getattr(cls, fun_name)):
                setattr(cls, fun_name, fun_transfer(getattr(cls, fun_name)))
            # print(fun_name, getattr(cls, fun_name))
        if hasattr(cls, '__init__'):
            cls.__init__ = init_transfer(cls.__init__)
        return cls


class B(A, int):
    pass


print(B(1))

# B()
# print(5)
# a = A()
# print(a.a)
