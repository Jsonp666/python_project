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


xtq = Xiao()

xtq.fly()

xtq.bark()

xtq.eat()

