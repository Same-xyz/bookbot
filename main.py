from stats import split_words, count_chars, sort_out

file_path: str = "./books/frankenstein.txt"
def get_books_text(file_path:str) -> str: 
    with open(file_path) as f:
        file_contents= f.read()
    return file_contents

def main() -> str:
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