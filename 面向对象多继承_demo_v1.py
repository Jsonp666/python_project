class A:

    def __init__(self):
        pass

    def test(self):
        print("这个是类A")


class B:

    def __init__(self):
        pass

    def test2(self):
        print("分类2")


class C(A, B):

    def __init__(self):
        pass


demo = C()

demo.test2()

demo.test()
