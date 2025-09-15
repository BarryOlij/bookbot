from stats import count_words
from stats import count_chars

def main():
    book_path = 'books/frankenstein.txt'
    book_text = get_book_text(book_path)
    book_wordcount = count_words(book_text)

    #print(count_chars(book_text))
    print(f"{book_wordcount} words found in the document")

def get_book_text(path):
    with open(path) as file:
        return file.read()

main()