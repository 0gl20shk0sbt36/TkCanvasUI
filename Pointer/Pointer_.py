def fun_(_fun_):
    def fun__(self_, *args_, **kwargs_):
        return _fun_(self_.__value__, *args_, **kwargs_)
    return fun__


class Pointer:

    __TypePointer = {}
    __dir = ['__class__', '__new__', '__init__', '__getattribute__', '__setattr__']

    def __new__(cls, *args, **kwargs):
        bases = cls.__bases__
        if bases[0] != Pointer:
            raise TypeError('Pointer需要作为第一个被继承的父类')
        if len(bases) == 1:
            return super().__new__(cls)
        elif len(bases) == 2:
            class_ = cls.__bases__[1]
        else:
            raise TypeError('只能设置一个类型作为指针类型')
        if cls.__name__ not in cls.__TypePointer:
            p = type(cls.__name__, (Pointer,), {'__type__': class_, '__value__': class_()})
            for name in dir(class_):
                if name in cls.__dir:
                    continue
                if name[:2] == name[-2:] == '__':
                    fun = getattr(class_, name)
                    if callable(fun):
                        setattr(p, name, fun_(fun))
            cls.__TypePointer[cls.__name__] = p
        else:
            p = cls.__TypePointer[cls.__name__]
        p = p(*args, **kwargs)
        return p

    def __init__(self, value=None):
        self.__value__ = value

    def __getattribute__(self, item):
        if item == '__value__':
            return super().__getattribute__('__value__')
        if item == '__type__':
            return super().__getattribute__('__type__')
        return getattr(super().__getattribute__('__value__'), item)

    def __setattr__(self, item, value):
        if item == '__value__':
            if type(value) == self.__type__:
                super().__setattr__('__value__', value)
            else:
                raise ValueError('类型不匹配')
        else:
            setattr(super().__getattribute__('__value__'), item, value)


class StrPointer(Pointer, str):
    pass


class IntPointer(Pointer, int):
    pass


class BoolPointer(Pointer, int):
    pass
