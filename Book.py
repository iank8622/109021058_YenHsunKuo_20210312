import random
"""
Last update: 2021.03.16
Book屬性列表:
"""


class Book:
    def __init__(self, name, year, writer): # _號為頭尾2個
        self.IdName = name
        self.IdYear = year
        self.IdWriter = writer

    def showInfo(self):
        print(self.IdName, "\t", self.IdYear, "\t", self.IdWriter)

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

Iname = ["亞大好廚房", "亞大文學館", "亞大貼圖瘋", "亞大漫遊社", "亞大健身房", "亞大田園趣", "亞大玩設計", "亞大資工路", "亞大心靈雞湯", "亞大旅遊書"]
Iyear = ["year:2001", "year:2002", "year:2003", "year:2004", "year:2005", "year:2006", "year:2007", "year:2008", "year:2009", "year:2010"]
Iwriter = ["writer:張小一", "writer:陳小二", "writer:王小三", "writer:簡小四", "writer:米小五", "writer:林小六", "writer:蔡小七", "writer:郭小八", "writer:蘇小九", "writer:吳小十"]

x1 = Book(Iname[Irandom_data[0]], Iyear[Irandom_data[0]], Iwriter[Irandom_data[0]])
x1.showInfo()
x2 = Book(Iname[Irandom_data[1]], Iyear[Irandom_data[1]], Iwriter[Irandom_data[1]])
x2.showInfo()
x3 = Book(Iname[Irandom_data[2]], Iyear[Irandom_data[2]], Iwriter[Irandom_data[2]])
x3.showInfo()
x4 = Book(Iname[Irandom_data[3]], Iyear[Irandom_data[3]], Iwriter[Irandom_data[3]])
x4.showInfo()
x5 = Book(Iname[Irandom_data[4]], Iyear[Irandom_data[4]], Iwriter[Irandom_data[4]])
x5.showInfo()
