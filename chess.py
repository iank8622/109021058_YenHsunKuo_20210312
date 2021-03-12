import random
"""
Last update: 2021.03.12
Chess:
"""


class Chess:
    def __init__(self, color, name): # _號為頭尾2個
        self.IdColor = color
        self.IdName = name


    def showInfo(self):
        print(self.IdColor, "\t", self.IdName)


IColor = ["紅", "黑"]
IName = ["將", "士", "象", "車", "馬", "炮", "卒"]

x1 = Chess(random.choice(IColor), random.choice(IName))
x1.showInfo()
x2 = Chess(random.choice(IColor), random.choice(IName))
x2.showInfo()
x3 = Chess(random.choice(IColor), random.choice(IName))
x3.showInfo()
x4 = Chess(random.choice(IColor), random.choice(IName))
x4.showInfo()
x5 = Chess(random.choice(IColor), random.choice(IName))
x5.showInfo()
