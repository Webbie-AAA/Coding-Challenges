def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.readlines()


list_of_measurements = read_input("input.txt")


measurements = []
for char in list_of_measurements:
    measurements.append(int(char))

print(measurements)


def count_increase_in_measurements(measurements: list[int]) -> int:
    number = measurements[0]
    count = 0
    for num in measurements[1:]:
        if num > number:
            count += 1
        number = num
    return count


print(count_increase_in_measurements(measurements))
