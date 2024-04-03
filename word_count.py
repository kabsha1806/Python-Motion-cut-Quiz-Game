def count_words(text):
    """
    Function to count the number of words in a given text.
    """
    # Split the text into words based on spaces
    words = text.split()
    # Return the count of words
    return len(words)

def main():
    """
    Main function to prompt user input and display word count.
    """
    print("Welcome to the Word Counter program!")
    while True:
        # Prompt user to enter a sentence or paragraph
        user_input = input("Please enter a sentence or paragraph (or type 'exit' to quit): ")
        
        # Check if the user wants to exit
        if user_input.lower() == 'exit':
            print("Thank you for using the Word Counter program. Goodbye!")
            break
        
        # Check for empty input
        if not user_input.strip():
            print("Error: Please enter some text.")
            continue
        
        # Call the count_words function to get the word count
        word_count = count_words(user_input)
        # Display the word count
        print(f"The number of words in your text is: {word_count}")

# Entry point of the program
if __name__ == "__main__":
    main()
