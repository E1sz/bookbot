# BookBot

BookBot is my first [Boot.dev](https://www.boot.dev) project! It's a Python application that analyzes text files and provides detailed statistics about word count and character frequency.

## Features

- **Word Count**: Counts the total number of words in a text file
- **Character Analysis**: Analyzes character frequency and displays results sorted by frequency (most common first)
- **Command Line Interface**: Easy to use with any text file

## Usage

```bash
python3 main.py <path_to_book>
```

### Example

```bash
python3 main.py books/frankenstein.txt
```

This will output:
- Total word count
- Character frequency analysis sorted from most to least common

## Project Structure

- `main.py` - Main application entry point
- `stats.py` - Contains text analysis functions
- `books/` - Directory containing sample text files
  - `frankenstein.txt` - Mary Shelley's Frankenstein
  - `mobydick.txt` - Herman Melville's Moby Dick
  - `prideandprejudice.txt` - Jane Austen's Pride and Prejudice

## Functions

- `get_book_text(book_path)` - Reads and returns the contents of a text file
- `get_num_words(book_text)` - Counts words in the text
- `get_character_amount(book_text)` - Returns character frequency dictionary sorted by count