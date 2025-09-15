def count_words(book):
    words = book.split()
    return len(words)

def count_chars(book):
    chars = list(book)
    return chars