def fun_transfer(_fun_):

    def __fun__(self, *args, **kwargs):
        return _fun_(self.__value__, *args, **kwargs)

    return __fun__


not_transfer_fun = ['__class__', '__new__', '__getattribute__', '__setattr__']


class A:

    def __getattribute__(self, item):
        if item == '__value__':
            return super().__getattribute__('__value__')
        return getattr(super().__getattribute__('__value__'), item)

    def __setattr__(self, item, value):
        if item == '__value__':
            if isinstance(value, type(self.__value__)):
                super().__setattr__('__value__', value)
            else:
                raise ValueError('类型不匹配')
        else:
            setattr(super().__getattribute__('__value__'), item, value)

    def __init_subclass__(cls, **kwargs):
        for fun_name in dir(cls):
            if fun_name[:2] == fun_name[-2:] == '__' and\
                    fun_name not in not_transfer_fun and\
                    callable(getattr(cls, fun_name)):
                setattr(cls, fun_name, fun_transfer(getattr(cls, fun_name)))
            # print(fun_name, getattr(cls, fun_name))
        return cls


class B(int, A):
    pass


print(B())

# B()
# print(5)
# a = A()
# print(a.a)
