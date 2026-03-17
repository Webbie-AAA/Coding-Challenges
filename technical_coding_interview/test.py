from task import is_palindrome, clean_palindrome_from_punctuation


def test_is_palindrome():
    attempt = 'racecar'
    assert is_palindrome(attempt) == True


def test_is_not_palindrome():
    attempt = 'recar'
    assert is_palindrome(attempt) == False


def test_ignore_case_sensitivity():
    attempt = "RaceCar"
    assert is_palindrome(attempt) == True


def test_ignore_punctuation_in_plaindrome():
    attempt = "cror;c"
    assert is_palindrome(attempt) == True


def test_clean_word_palindrome():
    attempt = "cror;c"
    assert clean_palindrome_from_punctuation(attempt) == "crorc"
