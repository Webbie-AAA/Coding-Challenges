def user_input():
    return input("Please enter your word or sentence: ")


def cleaning_string(text: str) -> str:
    return "".join(char.lower() for char in text if char.isalpha())


def palindrome_checker(cleaned_text: str) -> bool:
    if cleaned_text[::-1] == cleaned_text:
        return True
    return False


if __name__ == "__main__":
    raw = user_input()
    cleaning = cleaning_string(raw)
    palindrome_checker(cleaning)
