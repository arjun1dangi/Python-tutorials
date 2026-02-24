# to remove a given word from a list ad strip it at the same time


def remove_and_strip(lst, word_to_remove):
    return [item.strip() for item in lst if item.strip() != word_to_remove]

words = ["  apple  ", " banana ", "  orange", "apple ", "grape"]
word_to_remove = "apple"

result = remove_and_strip(words, word_to_remove)
print(result)
