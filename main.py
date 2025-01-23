def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    for character in my_string:
        if "p" not in char_counts:

    # print(f"{num_words} words found in the document")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {} #creates empty dictionary
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] +=1
        else:
            chars[lowered] = 1
    return chars

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()