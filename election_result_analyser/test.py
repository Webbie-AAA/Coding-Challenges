from analyser import count_votes, get_winner, get_vote_percentages, is_majority


def test_basic_case_vote_counting():
    """Basic case: vote counting."""
    # Arrange
    input_value = ["Alice", "Bob", "Alice"]

    # Act
    result = count_votes(input_value)

    # Assert
    assert result == {"Alice": 2, "Bob": 1}


def test_get_winner_counting():
    """Basic case: vote counting."""
    # Arrange
    input_value = ["Alice", "Bob", "Alice"]

    # Act
    result = get_winner(input_value)

    # Assert
    assert result == "Alice"


def test_get_winner_draw():
    """Basic case: vote counting."""
    # Arrange
    input_value = ["Alice", "Bob", "Alice", "Bob"]

    # Act
    result = get_winner(input_value)

    # Assert
    assert result == None


def test_get_vote_percentages():
    """Basic case: vote counting."""
    # Arrange
    input_value = ["Alice", "Bob", "Alice", "Bob"]

    # Act
    result = get_vote_percentages(input_value)

    # Assert
    assert result == {'Alice': 50.0, 'Bob': 50.0}


def test_is_majority():
    """Basic case: vote counting."""
    # Arrange
    input_votes = ["Alice", "Alice", "Bob"]
    input_candidate = "Alice"

    # Act
    result = is_majority(input_votes, input_candidate)

    # Assert
    assert result == True


def test_is_not_majority():
    """Basic case: vote counting."""
    # Arrange
    input_votes = ["Alice", "Alice", "Bob"]
    input_candidate = "Bob"

    # Act
    result = is_majority(input_votes, input_candidate)

    # Assert
    assert result == False
