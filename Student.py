import random
"""
Last update: 2021.03.16
Student屬性列表:
"""


class Student:
    def __init__(self, number, name, hight, weight, age): # _號為頭尾2個
        self.IdNumber = number
        self.IdName = name
        self.Idhight = hight
        self.Idweight = weight
        self. = age

    def showInfo(self):
        print(self.IdNumber, "\t", self.IdName, "\t", self.Idhight, "\t", self.Idweight, "\t", self.)

Irandom_data = []
i = 0

while i != 5:
    Irandom = random.randint(0,9)
    flag = True
    j = 0

    while j != i and flag == True:

        if Irandom_data[j] == Irandom:
            flag = False

        j += 1
        
    if flag:
        Irandom_data.append(Irandom)
        i += 1

Inumber = ["109021051", "109021052", "109021053", "109021054", "109021055", "109021056", "109021057", "109021058", "109021059", "109021060"]
Iname = ["name:張小一", "name:陳小二", "name:王小三", "name:簡小四", "name:米小五", "name:林小六", "name:蔡小七", "name:郭小八", "name:蘇小九", "name:吳小十"]
Ihight = ["hight:185", "hight:170", "hight:178", "hight:168", "hight:174", "hight:165", "hight:171", "hight:173", "hight:176", "hight:160"]
Iweight = ["weight:85", "weight:70", "weight:78", "weight:68", "weight:74", "weight:65", "weight:71", "weight:73", "weight:76", "weight:60"]
Iage = ["age:15", "age:20", "age:18", "age:18", "age:24", "age:15", "age:21", "age:23", "age:26", "age:20"]

x1 = Student(Inumber[Irandom_data[0]], Iname[Irandom_data[0]], Ihight[Irandom_data[0]], Iweight[Irandom_data[0]], Iage[Irandom_data[0]])
x1.showInfo()
x2 = Student(Inumber[Irandom_data[1]], Iname[Irandom_data[1]], Ihight[Irandom_data[1]], Iweight[Irandom_data[1]], Iage[Irandom_data[1]])
x2.showInfo()
x3 = Student(Inumber[Irandom_data[2]], Iname[Irandom_data[2]], Ihight[Irandom_data[2]], Iweight[Irandom_data[2]], Iage[Irandom_data[2]])
x3.showInfo()
x4 = Student(Inumber[Irandom_data[3]], Iname[Irandom_data[3]], Ihight[Irandom_data[3]], Iweight[Irandom_data[3]], Iage[Irandom_data[3]])
x4.showInfo()
x5 = Student(Inumber[Irandom_data[4]], Iname[Irandom_data[4]], Ihight[Irandom_data[4]], Iweight[Irandom_data[4]], Iage[Irandom_data[4]])
x5.showInfo()
