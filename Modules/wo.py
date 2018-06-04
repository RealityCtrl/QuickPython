"""wo module. Contains function: words_occur()"""
#interface functions
def words_occur():
    """words_occur: count the number of occurrences of words in a fil"""
    #prompt the user for the name of the file to use
    file_name = input("Enter the name of the file: ")
    #Open the file. read the file and store the words in the list.
    try:
        with open(file_name,"r") as file:
            word_list = file.read().split()
            #count the number of occurrences in the file
            occurs_dictionary = {}
            for words in word_list:
                occurs_dictionary[words] = occurs_dictionary.get(words, 0) + 1
            print("file %s has %d words (%d are unique)" % (file_name, len(word_list), len(occurs_dictionary)))
            print(occurs_dictionary)
    except IOError as error:
        print("%s: could not be opened: %s" % (file_name, error.strerror))


if __name__ == '__main__':
    words_occur()
