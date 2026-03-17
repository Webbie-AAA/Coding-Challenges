# TODO: Break a number of 4 digits of less into its constituent parts

def break_num_into_unit_values(number: int) -> list[int]:
    """Takes a number that's composed of 4 or less digits and returns a list of its unit values
    For example, 1829 returns [1000,800,20,9]"""
    number = str(number)
    length_to_zeros_dict = {4: '000', 3: '00', 2: '0', 1: ''}
    unit_list = []
    word_length = len(number)
    for i in range(len(number)):
        unit_list.append(int(number[i] + length_to_zeros_dict[word_length]))
        word_length -= 1
    return unit_list
    ...

# TODO: Create a helper function that finds out the sum of all integers in a list
# TODO: Create a function that create component roman numbers in a unique thousand unit


def convert_thousandth_num_to_numeral_breakdown(th_num: int) -> list[int]:
    thousandth_components = []
    range_count = int((str(th_num)[0]))
    for i in range(range_count):
        if th_num >= 1000:
            thousandth_components.append(1000)
    return thousandth_components

    # TODO: Create a function that checks component roman numbers in a unique hundred unit


def convert_hundredth_num_to_numeral_breakdown(hun_num: int) -> list[int]:
    hundredth_components = []
    total = 0

    if hun_num < 500:
        while total != hun_num:
            total += 100
            hundredth_components.append(100)
        return hundredth_components
    if hun_num > 500:
        total += 500
        hundredth_components.append(500)
        while total != hun_num:
            total += 100
            hundredth_components.append(100)
        return hundredth_components
    if hun_num == 500:
        hundredth_components.append(500)
    return hundredth_components

    ...

    # TODO: Create a function that component roman numbers in a unique ten unit


    # To make up 8000 in roman numerals you need 8 1000s because there's no 8.
if __name__ == "__main__":
    print(break_num_into_unit_values(1989))
    print(convert_thousandth_num_to_numeral_breakdown(4000))
    print(convert_hundredth_num_to_numeral_breakdown(100))
