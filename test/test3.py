class A:

    def __init__(self):
        self.a = True

    def __bool__(self):
        print(2)
        return False

    def __invert__(self):
        print(1)
        self.a = not self.a
        return self


a = A()
print(a)
print(a.a)
print(~a)
print(a.a)
