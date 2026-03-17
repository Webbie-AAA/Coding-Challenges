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


if __name__ == "__main__":
    print(break_num_into_unit_values(1989))
