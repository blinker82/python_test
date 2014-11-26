#! /usr/bin/env python

class MyClass:
    """A simple example class"""
    i = 12345
    def f(self):
        return 'hello world'
    def __init__(self):
        self.data = []

if __name__ == "__main__":
    x = MyClass()
    print x.f()
    print x.i
