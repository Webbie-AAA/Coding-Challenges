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


def convert_tens_num_to_numeral_breakdown(tens_num: int) -> list[int]:
    tens_components = []
    total = 0

    if tens_num < 50:
        while total != tens_num:
            total += 10
            tens_components.append(10)
        return tens_components
    if tens_num > 50:
        total += 50
        tens_components.append(50)
        while total != tens_num:
            total += 10
            tens_components.append(10)
        return tens_components
    if tens_num == 50:
        tens_components.append(50)
    return tens_components

    ...


#  The thousandth/hundredth/tens/units can all be done in a single function. Change later.


def convert_under_ten_to_numeral(num: int) -> list[int]:
    unit_components = []
    total = 0

    if num < 5:
        while total != num:
            total += 1
            unit_components.append(1)
        return unit_components
    if num > 5:
        total += 5
        unit_components.append(5)
        while total != num:
            total += 1
            unit_components.append(1)
        return unit_components
    if num == 5:
        unit_components.append(5)
    return unit_components


def combine_unit_breakdown_components(num: int) -> list[int]:
    unit_value_of_input = break_num_into_unit_values(user_input)
    number_breakdown = []
    for num in unit_value_of_input:
        if len(str(num)) == 4:
            number_breakdown += convert_thousandth_num_to_numeral_breakdown(
                num)
        elif len(str(num)) == 3:
            number_breakdown += convert_hundredth_num_to_numeral_breakdown(
                num)
        elif len(str(num)) == 2:
            number_breakdown += convert_tens_num_to_numeral_breakdown(num)
        elif len(str(num)) == 1:
            number_breakdown += convert_under_ten_to_numeral(num)
    return number_breakdown


def convert_units_to_roman_numerals(nums: list[int]) -> str:
    numerals_dict = {1: 'I', 5: 'V', 10: 'X',
                     50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    roman_numerals = ''
    for num in nums:
        roman_numerals += numerals_dict[num]
    return roman_numerals


if __name__ == "__main__":
    user_input = input("Provide a number between 1 and 3999: ")
    number_breakdown = combine_unit_breakdown_components(user_input)
    print(convert_units_to_roman_numerals(number_breakdown))

    ...
