class EmptyFileError(Exception):
    pass


fileNames = ["myFile.txt", "nonExistant", "emptyFile.txt"]
for file in fileNames:
    try:
        fileObj = open(file,"r")
        line = fileObj.readline()
        if line == "":
            fileObj.close()
            raise EmptyFileError("%s: is empty" % file)
    except IOError as error:
        print("%s: could not be opened %s" %(file, error.strerror))
    except EmptyFileError as error:
        print(error)
    else:
        print("%s:%s" % (file, line))
    finally:
        print("completed processing")
