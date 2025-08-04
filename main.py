import sys  # Import sys to handle command line arguments

from stats import get_num_words
from stats import get_book_text
from stats import get_character_amount


def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) # Exit if no book path is provided
    
    path = sys.argv[1]  # Get the first command line argument as the book path
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(get_book_text(path))} total words")
    print("------- Character Count --------")
    for character, amount in get_character_amount(get_book_text(path)).items():
        print(f"{character}: {amount}")

main()
