def text_file():
    # Initialize counter
    unique_words = 0
    # Read in the text file name
    file = input("Enter the name of the input file: ")
    # Open the file in read mode
    file_object = open(file, "r")
    # Create a dictionary
    dictionary = dict()
    # Separate all the words
    for line in file_object:
        line = line.rstrip()
        words = line.split()
        for w in words:
            if w in dictionary:
                # print(w)
                dictionary[w] = dictionary[w] + 1
                # If the word is already in the dictionary +1 to
                # Indicate how many there are now in the dictionary
            else:
                dictionary[w] = 1
                # If its new then equal it to 1 to indicate
                # How many there are now in the dictionary
                unique_words = unique_words + 1

    # Write to the dictionary file
    dictionary = str(dictionary)
    dictionary_file = open("dictionary.txt", "w")
    dictionary_file.write(dictionary)
    
    # Print out the results
    print("There are", unique_words, "unique words in the text.")
    print("The dictionary was written to dictionary.txt.")
    

def main():
    # Call text file function
    text_file()

    # Keep the console window open
    input("\nProgram End. Press Enter to exit...")


# Call the main function
main()
