
def clean_palindrome_from_punctuation(contaminated_word: str) -> str:
    cleaned_word = ""
    for char in contaminated_word:
        if char.isalpha():
            cleaned_word += char
    return cleaned_word


def is_palindrome(word: str) -> bool:

    word = word.lower()
    word = clean_palindrome_from_punctuation(word)
    letters_mirrored = []
    for i in range(1, len(word)):
        print(word[i-1], word[-i])
        if word[i-1] == word[-i]:
            letters_mirrored.append(True)
        else:
            letters_mirrored.append(False)
    return all(letters_mirrored)


print(is_palindrome("RaceCar"))


def palindrome_in_list(list_of_palindromes):
    palindrome_list = []
    for item in list_of_palindromes:
        if is_palindrome(item) == True:
            palindrome_list.append(item)
    return palindrome_list


if __name__ == "__main__":
    print(palindrome_in_list(["oh", "hah", "yep", "mm"]))
