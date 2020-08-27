class Women:
    def __init__(self, name):

        self.name = name
        # 私有属性
        self.__age = 18
    # 私有方法
    def __secret(self):
        print("我的名字叫 %s 我的年龄是 %d" % (self.name, self.__age))


nvren = Women("小王")

# print(nvren.__age)

nvren.__secret()
