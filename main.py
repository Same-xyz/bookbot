from stats import split_words, count_chars, sort_out
def get_books_text(file_path:str) -> str: 
    with open(file_path) as f:
        file_contents= f.read()
    return file_contents

def main() -> str:
    contents = get_books_text("./books/frankenstein.txt")
    word_count: str = split_words(contents)
    print(f"{word_count} words found in the document")
    
    character_count = count_chars(contents)
    sorted_list = sort_out(character_count)
    
    for item in sorted_list:
        if item["char"].isalpha():
            print(item)



main()