class WithKeyword(Exception):
    pass


fileNames = ["myFile.txt", "nonExistant", "emptyFile.txt"]
for file in fileNames:
    try:
        with open(file, "r") as fileObj:
            for line in fileObj:
                print("read line: ", line)
    except IOError as error:
        print("%s: could not be opened %s" % (file, error.strerror))
    finally:
        print("completed processing")
