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
    
def key_by_count(item):
    return item["num"]

def sorted_chars(book):
    sorted_chars = []
    raw_chars = count_chars(book)

    for ch, n in raw_chars.items():
        sorted_chars.append({"char": ch, "num": n})
    

    sorted_chars.sort(reverse=True, key=key_by_count)

    return sorted_chars