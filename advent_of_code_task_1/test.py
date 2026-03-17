from part1 import count_increase_in_measurements
from part2 import sum_of_three_sliding_window


def test_increases_count():
    measurements = [1, 2, 3, 4, 5]
    assert count_increase_in_measurements(measurements) == 4


def test_sums_3_sliding_window():

    measurements = [1, 2, 3, 4, 5]
    assert sum_of_three_sliding_window(measurements) == [6, 9, 12]
