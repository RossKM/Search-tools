# Searches through a direcotry tree for files larger than a specified amount and then gives the
# user option to delete them.
import os


def getsize():  # Gets the size of file to delete
    global delsize, r_size  # Allows these variables to be used in other functions
    r_size = input("Find files above how many MB? > ")
    delsize = int(r_size) * 1024 * 1024  # Converts to Bytes


def search(folder):
    folder = os.path.abspath(folder)
    print("Searching " + deldir + " for files above " + r_size + "Mb" + " ...")    # Tells user program is searching
    print("")
    for foldername, subfolder, filenames in os.walk(folder):    # Searches folder
        for filename in filenames:
            fp = os.path.join(foldername, filename)     # Ensures the file sizes are found correctly
            size = os.path.getsize(fp)  # Gets the size

            if size >= int(delsize):

                #   Ensures that file sizes show up as the correct unit.
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

                # Notes: '"%.2f"' ensures there is only 2 decimal places.
                option = input("found! " + filename + ' - ' + ("%.2f" % float(readablesize) + unit) +
                               ' - Permanently delete? Y/N > ')  # Tells user that files have been found.
                if option == "Y":
                    print(filename + ' - ' + ("%.2f" % float(readablesize) + unit) + ' - ERASED')
                    os.unlink(os.path.join(foldername, filename))    # Deletes file
                elif option == "N":
                    print("Nothing was deleted.")
                else:   # If Y or N is not typed
                    print("Input not recognised.")
                    continue    # Goes back to loop to try again/


print("WARNING: files deleted cannot be recovered!")    # Written warning for the user.
deldir = input("What directory would you like to search? > ")  # Asks user what directory to search and delete in
getsize()   # Calls function
search(deldir)
print("")
print("Done")
