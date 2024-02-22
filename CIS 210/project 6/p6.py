"""
Hunter McMahon
CIS 210
Project 6
description: why is the ground shaking?
"""

# Implement your solutions here. Remember to follow 210 Style and PEP8.
# Do not forget to click SUBMIT -- you can submit multiple times without penalty.
#
# Include doctests whenever appropriate. Feel free to delete these comments.
# To run doctests, at the "Console" below, type: python -m doctest p6.py -v
# (if you get an error that p6 cannot be found, click the round arrow "Reset Instance" button in the Console.)

import csv
import matplotlib.pyplot as plt


# todo: add doctest for extra credit
# 6.1, load the data from the CSV file
def load_data(file_name: str) -> list:
    """
    extracts the data from our file and returns it as a list of lines
    Args:
        file_name:
            (str) the name of the file we want to extract data from
    Returns:
        (list) a list of the data saved as dictionaries for each row
    >>> load_data('earthquakes-2020.csv')[0]['id'] == 'us70006t13')
    True
    """
    data_list = []
    with open(file_name, 'r', encoding="utf-8") as data_file:
        read_data = csv.DictReader(data_file)
        for line in read_data:
            data_list.append(line)
    print(data_list)
    return data_list


# 6.2 transform the data
def get_series(raw_data: list, col_name: str, col_type: type) -> list:
    """
    takes a "collum" of data from the list and extracts it
    Args:
        raw_data:
            (list) the raw data we are extracting things from
        col_name:
            (str) the dictionary key corresponding to the "collum" we want ti extract
        col_type:
            (function) the built in conversion function to convert our data to a desired type ie. float, int, str, etc.
    Returns:
        (list) a list with the extracted data
    >>> get_series([{'key1': 1.2, 'key2': 3.1}, {'key1': 2.1, 'key2': 4.9}],'key2', float)
    [3.1, 4.9]
    >>> get_series([], '', int)
    []
    """
    series = []
    for i in range(len(raw_data)):
        data_to_add = raw_data[i][col_name]
        data_converted = col_type(data_to_add)
        series.append(data_converted)
    return series


# 6.3 summarize the data
def get_categories(data: list, print_table=True) -> dict:
    """
    takes the data and sorts it by categorizing them
    Args:
        data:
            (list) the list of data we are putting into categories
        print_table:
            (boolean) True by default, determines if we print the data in a table
    Returns:
        (dict) a dictionary of the sorted/categorized earthquake magnitude data
    >>> get_categories([4.5, 5.6, 4.6, 6.5, 6.7, 7.9, 8.6, 4.7, 9.2, 9.6, 7])
    Light     :    3
    Moderate  :    1
    Major     :    2
    Strong    :    5
    {'light': 3, 'moderate': 1, 'major': 2, 'strong': 5}
    >>> get_categories([], False)
    {'light': 0, 'moderate': 0, 'major': 0, 'strong': 0}
    """
    mag_data = {'light': 0, 'moderate': 0, 'major': 0, 'strong': 0}
    for i in range(len(data)):
        if data[i] >= 4.5:
            if data[i] <= 4.9:
                mag_data['light'] += 1
            elif data[i] <= 5.9:
                mag_data['moderate'] += 1
            elif data[i] <= 6.9:
                mag_data['major'] += 1
            else:
                mag_data['strong'] += 1
    if print_table:
        mah_data_keys = list(mag_data.keys())
        for i in mah_data_keys:
            print(i.capitalize() + ":".rjust(11 - len(i)) + str(mag_data[i]).rjust(6 - len(str(mag_data[i]))))
    return mag_data


#  6.4 visualize the data
def plot_bar(x: list, y: list, title: str) -> plt.figure:
    """
    take some list of data and make a bar plot of it
    Args:
        x:
            (list) the data for the categories on the x axis
        y:
            (list) the quantities for the y axis
        title:
            (str)the title text for the top of the graph
    Returns:
        the bar graph object
    """
    fig = plt.figure()
    plt.bar(x=x, height=y)
    plt.title(title)
    plt.savefig(f'barplot-{title}.png')
    plt.show(block=False)
    return fig


def plot_scatter(x: list, y: list, title: str) -> plt.figure:
    """
    take some list of data and make a scatterplot of it
    Args:
        x:
            (list) the data for the quantities on the x axis
        y:
            (list) the data for the quantities on the y axis
        title:
            (str)the title text for the top of the graph
    Returns:
        the scatterplot object
    """
    fig = plt.figure()
    plt.scatter(x=x, y=y)
    plt.title(title)
    plt.savefig(f'scatterplot-{title}.png')
    plt.show(block=False)
    return fig


def main():
    """Perform all required steps for this project by calling other functions.
    """
    # Parts 6.1 and 6.2
    # 2020 data
    eq_data = load_data('earthquakes-2020.csv')
    magnitudes = get_series(eq_data, 'mag', float)
    print("2020 Earthquakes:")
    categories20 = get_categories(magnitudes)

    # 2021 data
    eq_data = load_data('earthquakes-2021.csv')
    magnitudes = get_series(eq_data, 'mag', float)
    print("\n2021 Earthquakes:")
    categories21 = get_categories(magnitudes)

    # Part 6.3
    diff21_20 = []
    for key in categories20.keys():
        diff21_20.append(categories21[key] - categories20[key])

    # Part 6.4
    fig = plot_bar(categories21.keys(), diff21_20, '2021 - 2020 Earthquakes')
    depths = get_series(eq_data, 'depth', float)
    fig = plot_scatter(depths, magnitudes, '2020 Depth vs Magnitude')


if __name__ == '__main__':
    main()
