def count_words(book):
    words = book.split()
    return len(words)

def count_chars(book):
    char_lib = {}
    for char in book.lower():
        if(char in char_lib):
            char_lib[char] += 1
        else:
            char_lib[char] = 1
    return char_lib