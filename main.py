def word_count(text):
    return len(text.split())

def char_count(text):
    text_norm = text.lower()
    total_chars = [char for char in (list(set(text_norm))) if char.isalpha()]
    char_counts = dict.fromkeys(total_chars, 0)

    for char in text_norm:
        if char in total_chars:
            char_counts[char] += 1
    
    count_lst = []

    for key, value in char_counts.items():
        count_lst.append({"name" : key, "num" : value})
    
    count_lst.sort(reverse=True, key=sort_on)

    return count_lst

def sort_on(dict):
    return dict["num"]

if __name__ == "__main__":
    with open("books/frankenstein.txt") as f:
        content = f.read()

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count(content)} words found in the document")
    print()
    char_counts = char_count(content)
    for record in char_counts:
        print(f"The {record["name"]} character was found {record["num"]} times")
    
    print("--- End Report ---")

