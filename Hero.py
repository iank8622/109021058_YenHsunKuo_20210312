import random
"""
Last update: 2021.03.12
Hero屬性列表:
"""


class Hero:
    def __init__(self, name, STR, DEF, DEX, CON): # _號為頭尾2個
        self.IdName = name
        self.IdSTR = STR
        self.IdDEF = DEF
        self.IdDEX = DEX
        self.IdCON = CON

    def showInfo(self):
        print(self.IdName, "\t", self.IdSTR, "\t", self.IdDEF, "\t", self.IdDEX, "\t", self.IdCON)


IName = ["關羽", "劉備", "張飛", "諸葛亮"]
ISTR = ["STR:S", "STR:A", "STR:B", "STR:C", "STR:D"]
IDEF = ["DEF:S", "DEF:A", "DEF:B", "DEF:C", "DEF:D"]
IDEX = ["DEX:S", "DEX:A", "DEX:B", "DEX:C", "DEX:D"]
ICON = ["CON:S", "CON:A", "CON:B", "CON:C", "CON:D"]

x1 = Hero(random.choice(IName), random.choice(ISTR), random.choice(IDEF), random.choice(IDEX), random.choice(ICON))
x1.showInfo()
x2 = Hero(random.choice(IName), random.choice(ISTR), random.choice(IDEF), random.choice(IDEX), random.choice(ICON))
x2.showInfo()
x3 = Hero(random.choice(IName), random.choice(ISTR), random.choice(IDEF), random.choice(IDEX), random.choice(ICON))
x3.showInfo()
x4 = Hero(random.choice(IName), random.choice(ISTR), random.choice(IDEF), random.choice(IDEX), random.choice(ICON))
x4.showInfo()
x5 = Hero(random.choice(IName), random.choice(ISTR), random.choice(IDEF), random.choice(IDEX), random.choice(ICON))
x5.showInfo()
