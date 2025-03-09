from stats import get_num_words, get_chars_dict

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict (text)
    print(f"{num_words} words found in the document")
    print(chars_dict)

def get_book_text(path):
    with open(path) as f:
        return f.read()





main()
