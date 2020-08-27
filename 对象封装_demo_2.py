class Gun:

    def __init__(self, model):

        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        # 填装子弹
        self.bullet_count += count

    def shoot(self):

        # 发射子弹
        # 判断是否有子弹

        if self.bullet_count <= 0:
            print("%s没有子弹了" % self.model)
            return

        self.bullet_count -= 1

        print("[%s] 突突突，剩余 [%d] 发子弹" % (self.model, self.bullet_count))


class Soldier:
    def __init__(self, name):
        # 士兵的名字
        self.name = name
        # 枪
        self.gun = None

    def fire(self):

        # 判断士兵是否有枪
        if self.gun is None:
            print("你还没有枪")
            return
        # 高喊口号
        print("冲啊")
        # 给枪装填子弹
        self.gun.add_bullet(50)
        # 发射子弹
        self.gun.shoot()


ak47 = Gun("AK47")

ak47.add_bullet(50)

ak47.shoot()

# 创建士兵对象
soldier = Soldier("许三多")

soldier.gun = ak47
soldier.fire()
print(soldier.gun)

