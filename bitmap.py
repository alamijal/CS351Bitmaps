"""
    Jala Alamin
    CS 351
    Assignment 4
    Due: February 28
    Instructor Ben McCamish"""


import sys

class BitmapIndex():
    def getBitmap(self, data):
        bitmap_list = list()
        bitmap = ['0']*16
        x=0
        for line in data:
            bitmap = ['0'] * 16
            if line[0] == "cat":
                bitmap[0] = '1'
                bitmap[1] = '0'
                bitmap[2] = '0'
                bitmap[3] = '0'
            elif line[0] == "dog":
                bitmap[0] = '0'
                bitmap[1] = '1'
                bitmap[2] = '0'
                bitmap[3] = '0'
            elif line[0] == "turtle":
                bitmap[0] = '0'
                bitmap[1] = '0'
                bitmap[2] = '1'
                bitmap[3] = '0'
            else:
                bitmap[0] = '0'
                bitmap[1] = '0'
                bitmap[2] = '0'
                bitmap[3] = '1'
            if int(line[1]) < 11:
                x = 4
            elif int(line[1]) < 21:
                x = 5
            elif int(line[1]) < 31:
                x = 6
            elif int(line[1]) < 41:
                x = 7
            elif int(line[1]) < 51:
                x = 8
            elif int(line[1]) < 61:
                x = 9
            elif int(line[1]) < 71:
                x = 10
            elif int(line[1]) < 81:
                x = 11
            elif int(line[1]) < 91:
                x = 12
            else:
                x = 13
            bitmap[x] = '1'
            for i in range(4,14):
                if i != x:
                    bitmap[i] = '0'
            if line[2] == "True":
                bitmap[14] = '1'
                bitmap[15] = '0'
            else:
                bitmap[14] = '0'
                bitmap[15] = '1'
            bitmap = ''.join(bitmap)
            bitmap_list.append(bitmap)

        print("expected is 1000000000010001")
        print("actual is %s" %bitmap_list[0])
        return bitmap







if __name__ == "__main__":
    b = BitmapIndex()
    with open(sys.argv[1]) as f:
        data = f.read().splitlines()

    data = [list(elem.split(",")) for elem in data]

    unsorted_bitmap = b.getBitmap(data)
