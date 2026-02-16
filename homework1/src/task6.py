def countWords(filename):
    #open file
    file = open(filename, 'r')
    #copy file
    text = file.read()
    #close file
    file.close()
    
    #split up the list into individual words based on spaces
    words = text.split()
    #count the words
    wordCount = len(words)
    
    return wordCount


if __name__ == "__main__":
    filename = "task6_read_me.txt"
    
    wordCount = countWords(filename)
    print(f"The file '{filename}' contains {wordCount} words.")