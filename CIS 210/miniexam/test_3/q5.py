"""
Question 5, Mini-exam 3, CIS210.

Name: Hunter McMahon
UO email: hmcmahon@uoregon.edu
"""

import statistics as sts
import csv


def read_data(filename: str) -> dict:
    """
    Reads the data from the given file and returns a dictionary of lists of scores.

    The first line of the file is assumed to be a header line, e.g., Labs, Projects, Exams
    Each subsequent line is assumed to be a comma-separated list of integer numbers, 
    representing the average percentage score [0, 100]. 
    
    Args:
        filename: the name of the file to read
    Returns:
        A dictionary of lists of scores, with keys corresponding to the column names.
        Example:
        {'Labs': [100, 20, 100], 'Projects': [90, 100, 100], 'Exams': [87, 95, 100]}
    """
    data_value_list = []
    load_data = {}
    iterate = 0
    # extract the data
    with open(str(filename), 'r', encoding="utf-8", newline='') as data:
        lines = csv.reader(data)
        for line in lines:
            data_value_list.append(line)
    # sort it into a dict
    for key in data_value_list[0]:
        dict_value = []
        for i in range(1, len(data_value_list)):
            dict_value.append(float(data_value_list[i][iterate]))
        load_data[key] = dict_value
        iterate += 1
    # return it
    return load_data


def print_stats(data: dict):
    """Prints the statistics for the given scores data dictionary.

    Args:
        data: a dictionary of lists of scores, with keys corresponding 
        to the column names.
    
    
    """
    # iterates for each of our datasets
    for key in data:
        # finds the stats
        min_val = round(min(data[key]), 1)
        max_val = round(max(data[key]), 1)
        mean_val = round(sts.mean(data[key]), 1)
        median_val = round(sts.median(data[key]), 1)
        std_val = round(sts.stdev(data[key]), 1)
        # prints the stats
        print('Statistics for ' + key + ':\n' +
              'Minimum:'.rjust(11) + str(min_val).rjust(7) + '\n' +
              'Maximum:'.rjust(11) + str(max_val).rjust(7) + '\n' +
              'Mean:'.rjust(11) + str(mean_val).rjust(7) + '\n' +
              'Median:'.rjust(11) + str(median_val).rjust(7) + '\n' +
              'Std dev:'.rjust(11) + str(std_val).rjust(7))


def assign_letter_grades(data: dict) -> dict:
    """Computes the letter grades for the given data and returns a 
    dictionary of lists of letter grades. For example, given a data dictionary:
        {'Labs': [100, 80, 100], 'Projects': [75, 100, 100], 'Exams': [87, 78, 100]}
    this function should return:
        {'Labs': ['A', 'B', 'A'], 'Projects': ['C', 'A', 'A'], 'Exams': ['B', 'C', 'A']}

    Args:
        data: a dictionary of lists of scores.
    Returns:
        A dictionary of lists of letter grades.
    >>> assign_letter_grades({'Labs': [100, 80, 100], 'Projects': [75, 100, 100], 'Exams': [87, 78, 100]})
    {'Labs': ['A', 'B', 'A'], 'Projects': ['C', 'A', 'A'], 'Exams': ['B', 'C', 'A']}
    """
    letter_grades_by_type = {}
    for key in data:
        letter_grade = []
        for i in data[key]:
            if i < 60:
                letter_grade.append('F')
            elif i < 70:
                letter_grade.append('D')
            elif i < 80:
                letter_grade.append('C')
            elif i < 90:
                letter_grade.append('B')
            elif i >= 90:
                letter_grade.append('A')
        letter_grades_by_type[key] = letter_grade
    return letter_grades_by_type


def main():
    """
    This program reads a CSV file containing Lab, Project, and Exam scores,
    and prints the statistics for the data, as well as the number of different
    letter grades for each column.
    """

    # Read the data into a dictionary with keys 'Labs', 'Projects', and 'Exams', and values
    # as lists of scores (ints) for each student.
    data = read_data('cis210-scores.csv')

    # Print the statistics for the raw scores data
    print_stats(data)

    # Assign letter grades based on the raw scores data
    letter_grades = assign_letter_grades(data)

    return


if __name__ == '__main__':
    main()
