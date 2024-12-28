def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    num_characters = get_chars_dict(text)
    print(f"{num_words} words found in the document")
    print(num_characters)


def word_count(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    characters = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
