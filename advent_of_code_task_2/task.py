def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.readlines()


submarine_commands_unclean = read_input('input.txt')


submarine_commands = []
for item in submarine_commands_unclean:
    submarine_commands.append(item.replace('\n', ''))


# practice_list = ['down 3', 'down 6', 'down 9', 'up 6', 'up 6', 'forward 9', 'forward 7', 'forward 7', 'down 3', 'down 6', 'down 9',
#                  'down 4', 'forward 7', 'forward 3', 'forward 3', 'down 7', 'up 5', 'down 3', 'forward 6', 'forward 3', 'forward 5', 'up 3',]
empty_list = []

# empty_list.append(practice_list[0].lower(), practice_list[1])


def clean_submarine_list(dirty_list):
    clean_list = []
    for item in dirty_list:
        string_to_list = item.strip().split()
        clean_list.append((string_to_list[0].lower(), int(string_to_list[1])))
    return clean_list


def horizontal_value(instructions):
    count = 0
    for item in instructions:
        if item[0] == "forward":
            count += item[1]
    return count


def aim_value(instructions):
    count = 0
    for item in instructions:
        if item[0] == "down":
            count += item[1]
        elif item[0] == "up":
            count -= item[1]
    return count


practice_list = ["forward 5", "down 5",
                 "forward 8", "up 3", "down 8", "forward 2"]


def depth_calculator(instructions: list[tuple]) -> str:
    horizontal_value = 0
    aim = 0
    depth = 0
    for instruction in instructions:
        if instruction[0] == "forward":
            horizontal_value += instruction[1]
            if aim != 0:
                depth += instruction[1] * aim
        elif instruction[0] == "down":
            aim += instruction[1]
        elif instruction[0] == "up":
            aim -= instruction[1]

    return f"Horizontal: {horizontal_value}, aim: {aim}, depth: {depth}"


if __name__ == "__main__":
    cleaned_list = clean_submarine_list(submarine_commands)
    print(depth_calculator(cleaned_list))

    # horizontal_value = horizontal_value(cleaned_list)
    # depth_value = depth_value(cleaned_list)
    # print(horizontal_value * depth_value)

    print(1002964*2083)
