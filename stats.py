def count_words(text):
    words = text.split()
    return len(words)

def count_char(text):
    text = text.lower()
    chars = {}
    for ch in text:
        if ch in chars:
            chars[ch] += 1
        else:
            chars[ch] = 1
    return chars


def list_chars(chars):
    char_list =[]
    for ch in chars:
            if ch.isalpha():
                char_list.append({"char": ch, "num": chars[ch]})
                for dict in char_list:
                    def sort_on(dict):
                        return dict["num"]
                char_list.sort(reverse=True, key=sort_on)
    return char_list


    