

class Bicycle:
    def run(self,km):
        print(f"一共骑行了{km}km")



class Ebicycle(Bicycle):
    # 构造方法，定义一个参数剩余电池电量
    def __init__(self,valume):
        self.valume = valume

    def full_charge(self,vol):
        self.valume = self.valume+vol
        print(f"电动车已充电:{vol}度")
        print(f"冲完电之后还有:{self.valume}度")

    def run(self,km):
        e_km = self.valume*10
        if e_km <= km:
            print(f"电量用尽，用电骑行了{e_km}km，用脚骑行了{km-e_km}km")
        else:
            super().run(km)
            print(f"电量未用尽，骑行了{km}km")

ebike = Ebicycle(10)
ebike.full_charge(1)
ebike.run(100)
