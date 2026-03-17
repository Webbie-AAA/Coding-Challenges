from palindrome import cleaning_string, palindrome_checker


def test_returns_no_whitespace():
    # Arrange
    user_input = "hello  friend"
    expected_result = "hellofriend"
    # Act
    actual_output = cleaning_string(user_input)
    # Assert
    assert actual_output == expected_result


def test_returns_no_non_alpha_chars():
    # Arrange
    user_input = "he-llo12.frie/nd"
    expected_result = "hellofriend"
    # Act
    actual_output = cleaning_string(user_input)
    # Assert
    assert actual_output == expected_result


def test_returns_all_lower_case():
    # Arrange
    user_input = "hello  friend"
    expected_result = "hellofriend"
    # Act
    actual_output = cleaning_string(user_input)
    # Assert
    assert actual_output == expected_result


def test_true_if_palindrome():
    # Arrange
    user_input = "racecar"
    expected_result = True
    # Act
    actual_output = palindrome_checker(user_input)
    # Assert
    assert actual_output == expected_result


def test_false_if_not_palindrome():
    # Arrange
    user_input = "racecarf"
    expected_result = False
    # Act
    actual_output = palindrome_checker(user_input)
    # Assert
    assert actual_output == expected_result
    pass
