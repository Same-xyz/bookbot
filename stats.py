def split_words(words: str) -> int:
    words.split(",")
    return len(words.split())
    pass

def count_chars(words: str) -> dict[str, int]:
    word_dict = {}
    for char in words.lower():
        if char not in word_dict:
            word_dict[char] = 1
        else:
            word_dict[char] += 1
    return word_dict
pass

def sort_out(words_dict: dict[str, int]) -> list:
    #Did it unpythonic firstly.
    # result_list=[]
    # for k in words_dict:
    #     result_list.append({"name":k, "value":words_dict[k]})
    # print(result_list)
    result_list = [{"char": k, "num": n} for k,n in words_dict.items()]
    # lambda here is similar to anonmymous functions in js
    result_list.sort(key= lambda item: item["num"], reverse= True)
    return result_list
    