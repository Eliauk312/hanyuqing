#coding:gbk
"""
程序目标:完成RPSLS游戏
作者:韩雨晴
"""

import random



# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

def name_to_number(name):
    if name=="石头":
        return 0
    elif name=="史波克":
        return 1
    elif name=="布":
        return 2
    elif name=="蜥蜴":
        return 3
    elif name=="剪刀":
        return 4
    else:
        print("Error: No Correct Name")

def number_to_name(number):
    if number==0:
        return "石头"
    elif number==1:
        return "史波克"
    elif number==2:
        return "布"
    elif number==3:
        return "蜥蜴"
    elif number==4:
        return "剪刀"
    else:
        print("Error: No Correct Name")

def rpsls(player_choice):
	print("--------------------")
	print("您的选择为:",player_choice)
	play_number=name_to_number(player_choice)
	comp_number=random.randrange(0,5)
	comp_choice=number_to_name(comp_number)
	print("电脑的选择为:",comp_choice)
	n=(play_number-comp_number)%5
	if n==1 or n==2:
		print("您赢了")
	elif n==3 or n==4:
		print("计算机赢了")
	else:
		print("您和计算机一样呢")

print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
rpsls(choice_name)
