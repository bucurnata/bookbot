from stats import count_words, count_char, list_chars
import sys

if len(sys.argv) != 2:
    print(f"Usage: python3 main.py <path_to_book> ")
    sys.exit(1)

file_path = sys.argv[1]

def main():
    content = get_book_text(file_path)
    num_words = count_words(content)
    chars = count_char(content)
    list = list_chars(chars)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {file_path}...\n----------- Word Count ----------\nFound {num_words} total words\n--------- Character Count -------")
    for dict in list:
        print(f" {dict["char"]}: {dict["num"]}")
    print("============= END ===============")
   

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()