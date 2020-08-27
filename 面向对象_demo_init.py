class Cat:
    def __init__(self, new_name):
        self.name = new_name
        print("%s 来了" % self.name)

    def __del__(self):
        print("%s 走了" % self.name)


lazty = Cat("小香猪")
print(lazty.name)
# 如果用自定义函数del  系统会提前执行__del__方法 ， 否则 会执行完所有程序， 自动自行__del__方法
del lazty
