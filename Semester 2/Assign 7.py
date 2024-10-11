def count():
    # Given paragraph
    paragraph = ("A Turing machine is a device that manipulates symbols on a strip of tape according to a table "
                "of rules. Despite its simplicity, a Turing machine can be adapted to simulate the logic of any "
                "computer algorithm, and is particularly useful in explaining the functions of a CPU inside a "
                "computer. The \"Turing\" machine was described by Alan Turing in 1936, who called it an "
                "\"a(utomatic)-machine\". The Turing machine is not intended as a practical computing "
                "technology, but rather as a hypothetical device representing a computing machine. Turing "
                "machines help computer scientists understand the limits of mechanical computation.")
    print(paragraph)
    # Initialize counters
    space_count = 0
    word_count = 0
    sen_count = 0
    # Iterate through the paragraph
    for character in paragraph:
        if character == " ":
            space_count = space_count + 1
        elif character == ".":
            # Always same number of fullstops as sentences
            sen_count = sen_count + 1
    # Always 1 more word than number of spaces
    word_count = space_count + 1
    print("\nThere are", word_count, "words contained in the paragraph")
    print("\nThere are", sen_count, "sentences contained in the paragraph")

def main():
    # Call the count function
    count()

    # Keep the console window open
    input("\nProgram End. Press Enter to exit...")


# Call the main function
main()
