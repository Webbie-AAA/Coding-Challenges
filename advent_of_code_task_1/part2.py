
# shift = 0
# for num in measurements:
from part1 import measurements, count_increase_in_measurements

nums = [1, 2, 3, 4, 5]
shift = 0

# So this would be in function with the sliding window


def sum_of_three_sliding_window(measurements: list) -> list:
    sum_of_trios_in_measurements = []
    shift = 0
    for i in range(len(measurements)):
        sum_of_3 = measurements[shift:shift+3]
        if len(sum_of_3) == 3:
            new_sum = sum(sum_of_3)

            shift += 1
            sum_of_trios_in_measurements.append(new_sum)
        else:
            break

    return sum_of_trios_in_measurements

    # It would be added to the function in part one to count number of increases.


if __name__ == "__main__":
    sums = sum_of_three_sliding_window(measurements)
    print(count_increase_in_measurements(sums))
