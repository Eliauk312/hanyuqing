#coding:gbk
"""
����Ŀ��:���RPSLS��Ϸ
����:������
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

def name_to_number(name):
    if name=="ʯͷ":
        return 0
    elif name=="ʷ����":
        return 1
    elif name=="��":
        return 2
    elif name=="����":
        return 3
    elif name=="����":
        return 4
    else:
        print("Error: No Correct Name")

def number_to_name(number):
    if number==0:
        return "ʯͷ"
    elif number==1:
        return "ʷ����"
    elif number==2:
        return "��"
    elif number==3:
        return "����"
    elif number==4:
        return "����"
    else:
        print("Error: No Correct Name")

def rpsls(player_choice):
	print("--------------------")
	print("����ѡ��Ϊ:",player_choice)
	play_number=name_to_number(player_choice)
	comp_number=random.randrange(0,5)
	comp_choice=number_to_name(comp_number)
	print("���Ե�ѡ��Ϊ:",comp_choice)
	n=(play_number-comp_number)%5
	if n==1 or n==2:
		print("��Ӯ��")
	elif n==3 or n==4:
		print("�����Ӯ��")
	else:
		print("���ͼ����һ����")

print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)
