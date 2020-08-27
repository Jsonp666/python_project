class Person:
    def __init__(self, name, wight):
        # self.属性 = 形参

        self.name = name
        self.wight = wight

    def __str__(self):

        return "我叫 %s 我的体重是 %.2f " % (self.name, self.wight)

    def run(self):
        self.wight -= 0.5
        print("%s 跑步了，现在体重是 %.2f " % (self.name, self.wight))

    def eat(self):
        self.wight += 1
        print("%s 吃东西，现在体重是 %.2f" % (self.name, self.wight))


xiaoming = Person("小明", 75.0)
xiaoming.run()
xiaoming.eat()

print(xiaoming)
