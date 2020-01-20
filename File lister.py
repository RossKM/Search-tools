# Searches through a tree and looks for large files and tells the user where they are.

import os


def getsize():
    global showsize
    r_size = input("Size to filter? File size > x (in Kb)")
    showsize = int(r_size) * 1024  # Converts to Bytes


def search(folder):
    folder = os.path.abspath(folder)
    for foldername, subfolder, filenames in os.walk(folder):    # Searches folder
        for filename in filenames:
            fp = os.path.join(foldername, filename)     # Ensures the file sizes are found correctly
            size = os.path.getsize(fp)  # Gets the size

            if size >= int(showsize):
                if size >= 1000000000:    # GByte
                    readablesize = size / 1024 / 1024 / 1024
                    unit = 'Gb'
                elif size >= 1000000:  # MByte
                    readablesize = size / 1024 / 1024
                    unit = 'Mb'
                elif size >= 1000:  # KByte
                    readablesize = size / 1024
                    unit = 'Kb'
                else:   # Byte
                    readablesize = size
                    unit = 'B'

                print("file found in " + folder + '/ ' + filename + ' - ' + ("%.2f" % float(readablesize) + unit))


getsize()
search('/home/ross/PycharmProjects/Delete large files/')
print("Done")
