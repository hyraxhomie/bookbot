def get_word_count(text):
    return len(text.split())

def get_character_count(text):
    char_dict = {}
    for char in text:
        if char.isalpha():
            if char.lower() in char_dict:
                char_dict[char.lower()] += 1
            else:
                char_dict[char.lower()] = 1
    return char_dict

def sort_on(item):
    return item['num']

def sort_dict(char_dict):
    char_count = []
    for key in char_dict:
        char_count.append({'char': key, 'num': char_dict[key]})
    char_count.sort(reverse=True, key=sort_on)
    return char_count


