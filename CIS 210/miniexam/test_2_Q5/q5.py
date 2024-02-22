"""
Hunter McMahon
CIS 122
quiz 2 question 5
description: lets calculate some data
"""


# import some useful things
from me2_data import num_siblings, num_credits, hours_sleep
import statistics


def find_max(data):
    """
    uses the stats module to find the maximum value (rounded to 1 digit) of a given tuple
    Args:
        data:
            (tuple) the data we want to find the maximum value of the tuple
    Returns:
        (float) the rounded maximum value of the data tuple
    """
    max_val = max(data)
    return round(max_val, 1)


def find_min(data):
    """
    uses the stats module to find the minimum value (rounded to 1 digit) of a given tuple
    Args:
        data:
            (tuple) the data we want to find the minimum value of the tuple
    Returns:
        (float) the rounded minimum value of the data tuple
    """
    min_val = min(data)
    return round(min_val, 1)


def find_mean(data):
    """
    uses the stats module to find the mean value (rounded to 1 digit) of a given tuple
    Args:
        data:
            (tuple) the data we want to find the mean value of the tuple
    Returns:
        (float) the rounded mean value of the data tuple
    """
    mean_val = statistics.mean(data)
    return round(mean_val, 1)


def find_mode(data):
    """
    uses the stats module to find the mode (rounded to 1 digit) of a given tuple
    Args:
        data:
            (tuple) the data we want to find the mode of the tuple
    Returns:
        (float) the rounded mode of the data tuple
    """
    mode_val = statistics.mode(data)
    return round(mode_val)


def print_data(max_data, min_data, mean_data, mode_data):
    """
    prints out the data given based on user input
    Args:
        max_data:
            (int/float) max value of the data
        min_data:
            (int/float) min value of the data
        mean_data:
            (int/float) mean value of the data
        mode_data:
            (int/float) the mode value of the data
    Returns:
        (none) void function

    """
    prompt = True
    while prompt:
        user_request = input('What stats do you wish to compute (min, max, mode, mean, all)? ')
        user_request.lower()
        if user_request == 'min':
            print('Min= ', str(min_data).rjust(7))
            prompt = False
        elif user_request == 'max':
            print('Max= ', str(max_data).rjust(7))
            prompt = False
        elif user_request == 'mode':
            print('Mode= ', str(mode_data).rjust(6))
            prompt = False
        elif user_request == 'mean':
            print('Mean= ', str(mean_data).rjust(6))
            prompt = False
        elif user_request == 'all':
            print('Max= ', str(max_data).rjust(7))
            print('Min= ', str(min_data).rjust(7))
            print('Mean= ', str(mean_data).rjust(6))
            print('Mode= ', str(mode_data).rjust(6))
            prompt = False
        else:
            print('please enter a valid computation request')


def main():
    prompt = True
    while prompt:
        user_data = input('Pick a dataset (siblings, credits, sleep): ')
        user_data.lower()
        if user_data == "siblings":
            max_set = find_max(num_siblings)
            min_set = find_min(num_siblings)
            mean = find_mean(num_siblings)
            mode = find_mode(num_siblings)
            print_data(max_set, min_set, mean, mode)
            prompt = False
        elif user_data == "credits":
            max_set = find_max(num_credits)
            min_set = find_min(num_credits)
            mean = find_mean(num_credits)
            mode = find_mode(num_credits)
            print_data(max_set, min_set, mean, mode)
            prompt = False
        elif user_data == "sleep":
            max_set = find_max(hours_sleep)
            min_set = find_min(hours_sleep)
            mean = find_mean(hours_sleep)
            mode = find_mode(hours_sleep)
            print_data(max_set, min_set, mean, mode)
            prompt = False
        else:
            print('please enter a valid input')


if __name__ == "__main__":
    main()
