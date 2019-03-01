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
                x = 0
            elif line[0] == "dog":
                x = 1
            elif line[0] == "turtle":
                x = 2
            else:
                x = 3
            bitmap[x] = '1'
            for i in range(0, 4):
                if i != x:
                    bitmap[i] = '0'
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
        bitmap_list = ''.join(bitmap_list)
        return bitmap_list

    def compress(self,bitmap, size):
        # grab 31 bit words at a time
        # initialize compressed list
        # if not all 1s or all 0s, store a literal in compressed list
        # if all 0s, increment count, check next 31 until there is a 1
        # store 0 run word
        # same if all 1s
        # store leftover bits as a literal
        compressed = ''
        i = 0
        bitmap = list(bitmap)

        while(i < len(bitmap)):
            # case 1: runs of 0s
            result1 = self.get_runs(bitmap,i,'0', size)
            if result1[0] != False:
                compressed += result1[0]
                i = result1[1]
                if i >= len(bitmap):
                    break

            # case 2: runs of 1s
            result2 = self.get_runs(bitmap, i, '1', size)
            if result2[0] != False:
                compressed += result2[0]
                i = result2[1]
                if i >= len(bitmap):
                    break

            # case 3: literal
            if result1[0] == False and result2[0] == False:
                if (len(bitmap) - i) < (size - 1):
                    word = '0'
                    word += ''.join(bitmap[i:])
                    compressed += word
                    i += len(bitmap) - i
                else:
                    word = '0'
                    word += ''.join(bitmap[i:i+(size - 1)])
                    compressed += word
                    i += (size - 1)

        return compressed




    """if there is a run, returns compressed word
        if not, returns False"""
    def get_runs(self,bitmap,i, x, size):
        save = i
        run_count = 0
        bit_count = 0
        word = list('0' * size)
        while (bitmap[i] == x):
            bit_count += 1
            if bit_count == (size - 1):
                run_count += 1
                bit_count = 0
            i += 1
            if i >= len(bitmap):
                break
        if run_count != 0:
            runs = "{0:b}".format(run_count)
            start = size - len(runs)
            word[start:] = runs
            word[0] = '1'
            if x == '1':
                word[1] = '1'
            word = ''.join(word)
            save += run_count * (size - 1)
            return word, save
        else:
            return False, save


if __name__ == "__main__":
    b = BitmapIndex()
    with open(sys.argv[1]) as f:
        data = f.read().splitlines()

    data = [list(elem.split(",")) for elem in data]

    unsorted_bitmap = b.getBitmap(data)
    sorted_data = sorted(data)
    sorted_bitmap = b.getBitmap(sorted_data)
    #print(unsorted_bitmap)
    #compressed_bitmap32 = b.compress(unsorted_bitmap)
    #print("{0:b}".format(5))
    #print(type(unsorted_bitmap.split()))
    #test = '0000000000000000000000000000000'
    test = '1111111111111111111111111111111' \
           '1010101010100101010111110000101' \
           '0000000000000000000000000000000' \
           '0000000000000000000000000000000' \
           '0000000000000000000000000000000' \
           '0000000000000000000000000000000' \
           '1111111111111111111111111111111' \
           '1111111111111111111111111111111' \
           '0000000000000000000000000000000' \

    #test = '10011001'


    #test = test.split()
    print(b.compress(test, 32))
