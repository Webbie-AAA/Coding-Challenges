from task import clean_submarine_list, horizontal_value, depth_value, depth_calculator


def test_cleaning_list():
    practice_list = ['down 3', 'down 6', 'down 9', 'up 6', 'up 6', 'forward 9', 'forward 7', 'forward 7', 'down 3', 'down 6', 'down 9',
                     'down 4', 'forward 7', 'forward 3', 'forward 3', 'down 7', 'up 5', 'down 3', 'forward 6', 'forward 3', 'forward 5', 'up 3',]
    assert clean_submarine_list(practice_list) == [('down', 3), ('down', 6), ('down', 9), ('up', 6), ('up', 6), ('forward', 9), ('forward', 7), ('forward', 7), ('down', 3), (
        'down', 6), ('down', 9), ('down', 4), ('forward', 7), ('forward', 3), ('forward', 3), ('down', 7), ('up', 5), ('down', 3), ('forward', 6), ('forward', 3), ('forward', 5), ('up', 3)]


def test_horizontal_value():
    list_of_tuple_instructions = [('down', 3), ('down', 6), ('down', 9), ('up', 6), ('up', 6), ('forward', 9), ('forward', 7), ('forward', 7), ('down', 3), (
        'down', 6), ('down', 9), ('down', 4), ('forward', 7), ('forward', 3), ('forward', 3), ('down', 7), ('up', 5), ('down', 3), ('forward', 6), ('forward', 3), ('forward', 5), ('up', 3)]
    assert horizontal_value(list_of_tuple_instructions) == 50


def test_depth_value():
    list_of_tuple_instructions = [('down', 3), ('down', 6), ('down', 9), ('up', 6), ('up', 6), ('forward', 9), ('forward', 7), ('forward', 7), ('down', 3), (
        'down', 6), ('down', 9), ('down', 4), ('forward', 7), ('forward', 3), ('forward', 3), ('down', 7), ('up', 5), ('down', 3), ('forward', 6), ('forward', 3), ('forward', 5), ('up', 3)]
    assert depth_value(list_of_tuple_instructions) == 30


def test_depth_calculator():
    list_of_tuple_instructions = [('down', 3), ('down', 6), ('down', 9), ('up', 6), ('up', 6), ('forward', 9), ('forward', 7), ('forward', 7), ('down', 3), (
        'down', 6), ('down', 9), ('down', 4), ('forward', 7), ('forward', 3), ('forward', 3), ('down', 7), ('up', 5), ('down', 3), ('forward', 6), ('forward', 3), ('forward', 5), ('up', 3)]
    # assert depth_calculator() ==
    pass
