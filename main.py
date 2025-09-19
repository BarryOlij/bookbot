from stats import count_words
from stats import sorted_chars
import sys

def main():
    if(len(sys.argv) < 2):
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    book_wordcount = count_words(book_text)
    sorted_list = sorted_chars(book_text)

    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {book_path}...')
    print('----------- Word Count ----------')
    print(f'Found {book_wordcount} total words')
    print('--------- Character Count -------')    
    for item in sorted_list:
        ch = item["char"]
        if ch.isalpha():
            print(f"{ch}: {item['num']}")
    print('============= END ===============')

def get_book_text(path):
    with open(path) as file:
        return file.read()

main()