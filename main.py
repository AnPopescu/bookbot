

BOOK_PATH = "books/frankenstein.txt" 

def count_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_each_letter(text):
    ch_dict = {}
    lower_text = text.lower()
    for ch in lower_text:
        if(ch_dict.get(ch) == None):
            ch_dict[ch] = 1
        else:
            ch_dict[ch] = ch_dict[ch] + 1
            
    #return list of dicts
    return [{key: value} for key,value in ch_dict.items()]

def sort_on_letter(dict):
    return next(iter(dict.values()))

def print_letter_count(list_of_dicts):
    list_of_dicts.sort(reverse = True, key=sort_on_letter)
    for dict in list_of_dicts:
        for key in dict:
            if(key.isalpha()):
                print(f"The {key} character was found {dict[key]} times ")

def print_report(book_path):
    book_text = get_book_text(book_path)
    number_of_words = count_words(book_text)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{number_of_words} words found in the document\n")
    print_letter_count(count_each_letter(book_text))
    print(f"--- End report ---")
    
    

def main():
    print_report(BOOK_PATH)
    


main()