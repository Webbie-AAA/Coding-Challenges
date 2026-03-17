from main import break_num_into_unit_values


def test_given_a_4_digit_num_return_units():
    # Arrange
    number = 1992
    answer = [1000, 900, 90, 2]
    # Act
    result = break_num_into_unit_values(number)
    # Assert
    assert result == answer


def test_given_a_3_digit_num_return_units():
    # Arrange
    number = 199
    answer = [100, 90, 9]
    # Act
    result = break_num_into_unit_values(number)
    # Assert
    assert result == answer


def test_given_a_2_digit_num_return_units():
    # Arrange
    number = 25
    answer = [20, 5]
    # Act
    result = break_num_into_unit_values(number)
    # Assert
    assert result == answer


def test_given_a_1_digit_num_return_units():
    # Arrange
    number = 5
    answer = [5]
    # Act
    result = break_num_into_unit_values(number)
    # Assert
    assert result == answer
