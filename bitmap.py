"""
    Jala Alamin
    CS 351
    Assignment 4
    Due: February 28
    Instructor Ben McCamish"""

import sys
import os
import shutil


class BitmapIndex():
    def getBitmap(self, data):
        bitmap_list = list()
        bitmap = ['0'] * 16
        x = 0
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
            for i in range(4, 14):
                if i != x:
                    bitmap[i] = '0'
            if line[2] == "True":
                bitmap[14] = '1'
                bitmap[15] = '0'
            else:
                bitmap[14] = '0'
                bitmap[15] = '1'
            bitmap = ''.join(bitmap)
            bitmap += '\n'
            bitmap_list.append(bitmap)
        bitmap_list = ''.join(bitmap_list)
        return bitmap_list

    def compress(self, bitmap, size):
        compressed = ''
        result = []
        i = 0
        num0runs = 0
        num1runs = 0
        num_literals = 0
        bitmap = self.get_columns(bitmap)

        for column in bitmap:
            i = 0
            while (i < len(column)):
                # case 1: runs of 0s
                result1 = self.get_runs(column, i, '0', size)
                if result1[0] != False:
                    compressed += result1[0]
                    i = result1[1]
                    num0runs += result1[2]
                    if i >= len(column):
                        break

                # case 2: runs of 1s
                result2 = self.get_runs(column, i, '1', size)
                if result2[0] != False:
                    compressed += result2[0]
                    i = result2[1]
                    num1runs += result2[2]
                    if i >= len(column):
                        break

                # case 3: literal
                if result1[0] == False and result2[0] == False:
                    if (len(column) - i) < (size - 1):
                        word = '0'
                        word += ''.join(column[i:])
                        compressed += word
                        i += len(column) - i
                        num_literals += 1
                    else:
                        word = '0'
                        word += ''.join(column[i:i + (size - 1)])
                        compressed += word
                        i += (size - 1)
                        num_literals += 1
            compressed += '\n'
            result.append(compressed)
            compressed = ''
        result = ''.join(result)
        return result, num0runs, num1runs, num_literals

    """ returns a list of strings where each 
    string is a column of the given bitmap"""

    def get_columns(self, bitmap):
        string = []
        column = ''

        col = 0
        bitmap = bitmap.split('\n')

        for col in range(16):
            for row in bitmap:
                if row != '':
                    column += row[col]
            string.append(column)
            column = ''
        return string

    """if there is a run, returns compressed word
        if not, returns False"""

    def get_runs(self, bitmap, i, x, size):
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
            return word, save, run_count
        else:
            return False, save, 0


if __name__ == "__main__":
    b = BitmapIndex()
    with open('animals.txt') as f:
        data = f.read().splitlines()

    data = [list(elem.split(",")) for elem in data]

    unsorted_bitmap = b.getBitmap(data)
    sorted_data = sorted(data)
    sorted_bitmap = b.getBitmap(sorted_data)

    compressed_bitmap32 = b.compress(unsorted_bitmap, 32)
    compressed_bitmap32_sorted = b.compress(sorted_bitmap, 32)

    compressed_bitmap64 = b.compress(unsorted_bitmap, 64)
    compressed_bitmap64_sorted = b.compress(sorted_bitmap, 64)

    print("compressed_bitmap32 num of 0 runs: %d" % compressed_bitmap32[1])
    print("compressed_bitmap32 num of 1 runs: %d" % compressed_bitmap32[2])
    print("compressed_bitmap32 num of literals: %d" % compressed_bitmap32[3])
    print('\n')
    print("compressed_bitmap32_sorted num of 0 runs: %d" % compressed_bitmap32_sorted[1])
    print("compressed_bitmap32_sorted num of 1 runs: %d" % compressed_bitmap32_sorted[2])
    print("compressed_bitmap32_sorted num of literals: %d" % compressed_bitmap32_sorted[3])
    print('\n')
    print("compressed_bitmap64 num of 0 runs: %d" % compressed_bitmap64[1])
    print("compressed_bitmap64 num of 1 runs: %d" % compressed_bitmap64[2])
    print("compressed_bitmap64 num of literals: %d" % compressed_bitmap64[3])
    print('\n')
    print("compressed_bitmap64_sorted num of 0 runs: %d" % compressed_bitmap64_sorted[1])
    print("compressed_bitmap64_sorted num of 1 runs: %d" % compressed_bitmap64_sorted[2])
    print("compressed_bitmap64_sorted num of literals: %d" % compressed_bitmap64_sorted[3])
"""
    os.mkdir('Indexes')
    sys.stdout = open('Indexes/File1_Unsorted_Bitmap.txt', 'w+')
    print(unsorted_bitmap[0])

    sys.stdout = open('Indexes/File2_Sorted_Bitmap.txt', 'w+')
    print(sorted_bitmap[0])

    sys.stdout = open('Indexes/File3_Compressed_Bitmap_32.txt', 'w+')
    print(compressed_bitmap32[0])

    sys.stdout = open('Indexes/File4_Sorted_Compressed_Bitmap_32.txt', 'w+')
    print(compressed_bitmap32_sorted[0])

    sys.stdout = open('Indexes/File5_Compressed_Bitmap_64.txt', 'w+')
    print(compressed_bitmap64[0])

    sys.stdout = open('Indexes/File6_Sorted_Compressed_Bitmap_64.txt', 'w+')
    print(compressed_bitmap64_sorted[0])

"""

# shutil.rmtree('Indexes')
