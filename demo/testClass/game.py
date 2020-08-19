class Game:

    def __init__(self):
        self.my_hp = 1000
        self.my_power = 200
        self.your_hp = 1000
        self.your_power = 199

    def fight():
        my_hp = 1000
        my_power = 200
        your_hp = 1000
        your_power = 199

        # 一轮之后，双方的血量
        while True:
            my_hp = my_hp - your_power
            your_hp = your_hp - my_power

            # 对比双方的血量，判断输赢
            if my_hp <= 0:
                print("我赢了")
                break

            elif your_hp <= 0:
                print("你输了")
                break
