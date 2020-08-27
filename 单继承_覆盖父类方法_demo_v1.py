class Animal:

    def eat(self):
        print("吃东西")

    def drink(self):
        print("和水")

    def run(self):
        print("跑起来")

    def sleep(self):
        print("睡觉")


class Dog(Animal):

    def bark(self):

        print("汪汪叫 ")


class Xiao(Dog):

    def fly(self):

        print("我会飞")

    # def bark(self):
    #     # 如果子类方法复写父类方法 ， 调用的时候走子类方法 ， 不会再走父类方法
    #     print("叫的呱呱呱")

    def bark(self):

        # 编写特定的代码

        # 通过super() 调用父类方法
        super().bark()


xtq = Xiao()


xtq.bark()
