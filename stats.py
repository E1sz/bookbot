def get_num_words(book_text):
    return len(book_text.split())

def get_book_text(book_path):
    with open(book_path) as f:
        book_content = f.read()
    return book_content

def get_character_amount(book_text):
    book_text=book_text.lower()
    unique_characters = set(book_text)
    character_dict = {}
    for character in unique_characters:
        character_dict[character] = book_text.count(character)
    # Sort the dictionary by values (counts) in descending order
    return dict(sorted(character_dict.items(), key=lambda x: x[1], reverse=True))
