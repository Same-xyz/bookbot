from stats import split_words, count_chars, sort_out
import sys

file_path:str = ""
# file_path: str = sys.argv[1]
# print(sys.argv[1], sys.argv[2])
# file_path: str = "books/frankenstein.txt"

def check_args():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return sys.argv[1]

def get_books_text(file_path:str) -> str: 
    with open(file_path) as f:
        file_contents= f.read()
    return file_contents

def main() -> str:
    file_path: str = check_args()
    print(file_path)
    contents = get_books_text(file_path)
    word_count: str = split_words(contents)

    print("============ BOOKBOT ============")
    print(f'''Analyzing books found at {file_path}...
----------- Word Count ----------
Found {word_count} total words''')
    print("--------- Character Count -------")
    
    character_count = count_chars(contents)
    sorted_list = sort_out(character_count)
    
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")

    # Used a generator below, trying pythonic syntax
    # result= (f"{item["char"]}: {item["num"]}" for item in sorted_list if item["char"].isalpha())
    # print(list(result))
    print("============= END ===============")




main()