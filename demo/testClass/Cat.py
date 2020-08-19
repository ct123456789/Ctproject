
# 定义类，首字母需要大写
class Cat:
    color = "black"
    leg = 4
    eye = 2

    def eat(self):
        print("猫会吃")
    def sleep(self):
        print("猫会睡觉")

print(Cat.color)
cat = Cat()
cat.sleep()
print(cat.eye)