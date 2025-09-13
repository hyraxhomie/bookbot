import sys

from stats import get_word_count, get_character_count, sort_dict
def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}")
    text = get_book_text(path_to_book)
    print("----------- Word Count ----------")
    num_words = get_word_count(text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_count = get_character_count(text)
    sorted_count = sort_dict(char_count)
    for item in sorted_count:
        print(F"{item['char']}: {item['num']}")
    print("============= END ===============")

main()