class Dog(object):

    def __init__(self, name, type):

        self.name = name
        self.type = type

    def game(self):

        print("%s 蹦蹦跳跳的玩耍" % self.name)


class XiaoTian(Dog):

    def game(self):

        print("%s %s到天上去" % (self.name, self.type))


class Person(object):

    def __init__(self, name):

        self.name = name

    def game_with_dog(self, dog):

        print("%s 和 %s 快乐的玩耍" % (self.name, dog.name))

        dog.game()


# dog = Dog("旺财")
xiaotian = XiaoTian("飞猪", "跑")

xiaoming = Person("小明")

xiaoming.game_with_dog(xiaotian)


