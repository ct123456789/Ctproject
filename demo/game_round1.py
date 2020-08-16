def fight():
    my_hp = 100
    my_power = 200
    your_hp = 100
    your_power = 199

    # 一轮之后，双方的血量
    my_final_hp = my_hp - your_power
    your_final_hp = your_hp - my_power
    
    #对比双方的血量，判断输赢
    if my_final_hp > your_final_hp:
        print("我赢了")
    elif my_final_hp < your_final_hp:
        print("你赢了")
    else:
        print("平局了")

fight()