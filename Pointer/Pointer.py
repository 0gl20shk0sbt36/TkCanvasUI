def refactor_lass(cls: type):
    def __init__(self, *args, **kwargs):
        self.__value__ = cls(*args, **kwargs)

    cls_ = type(cls.__name__, (object,), {'__init__': __init__, 'a': None})
    return cls_


@refactor_lass
class A:

    def __init__(self):
        self.b = None

    def a(self):
        pass




# A()
# A = refactor_lass(A)
#
#
# A()
