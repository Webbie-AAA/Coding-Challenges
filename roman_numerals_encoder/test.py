from main import break_num_into_unit_values, convert_thousandth_num_to_numeral_breakdown, convert_hundredth_num_to_numeral_breakdown


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


def test_convert_a_big_thousandth_to_thousand_components():
    # Arrange
    number = 8000
    answer = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
    # Act
    result = convert_thousandth_num_to_numeral_breakdown(number)
    # Assert
    assert result == answer


def test_convert_a_single_thousand_to_thousand_components():
    # Arrange
    number = 1000
    answer = [1000]
    # Act
    result = convert_thousandth_num_to_numeral_breakdown(number)
    # Assert
    assert result == answer


def test_break_down_hundreds_larger_than_500_to_components():
    # Arrange
    number = 800
    answer = [500, 100, 100, 100]
    # Act
    result = convert_hundredth_num_to_numeral_breakdown(number)
    # Assert
    assert result == answer


def test_break_down_hundreds_less_than_500_to_components():
    # Arrange
    number = 400
    answer = [100, 100, 100, 100]
    # Act
    result = convert_hundredth_num_to_numeral_breakdown(number)
    # Assert
    assert result == answer


def test_break_down_hundreds_equal_to_500():
    # Arrange
    number = 500
    answer = [500]
    # Act
    result = convert_hundredth_num_to_numeral_breakdown(number)
    # Assert
    assert result == answer


def test_break_down_tens_greater_than_50_to_components():
    # Arrange
    number = 80
    answer = [50, 10, 10, 10]
    # Act
    result = convert_hundredth_num_to_numeral_breakdown(number)
    # Assert
    assert result == answer


def test_break_down_tens_less_than_50_to_components():
    # Arrange
    number = 30
    answer = [10, 10, 10]
    # Act
    result = convert_hundredth_num_to_numeral_breakdown(number)
    # Assert
    assert result == answer


def test_break_down_tens_equal_to_50():
    # Arrange
    number = 50
    answer = [50]
    # Act
    result = convert_hundredth_num_to_numeral_breakdown(number)
    # Assert
    assert result == answer
