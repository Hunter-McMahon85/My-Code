""" 
Mini-Exam 4, Question 5, CIS210

Name: Hunter McMahon
UO email: hmcmahon@uoregon.edu
"""
import csv
import re
import statistics as sts


def read_data(filename: str) -> list:
    """
    Reads a CSV file and returns a list of dictionaries (similar to Project 6), 
    using a csv.DictReader. All numerical values are converted to the 
    appropriate type (see examples in doctest). We assume that the first row of
    the file contains column names.

    Args:
        filename: The file name of the CSV file to read.

    Returns:
        A list of dictionaries, one for each row in the CSV file.

    Examples:
    >>> read_data('2021-Eugene-weather.csv')[:2]
    [{'DATE': '1/1/21', 'Wind': 12.08, 'Rain': 0.19, 'TempAvg': 49, 'TempMax': 55, 'TempMin': 46, 'Fog': 1},
    {'DATE': '1/2/21', 'Wind': 15.66, 'Rain': 0.38,
    'TempAvg': 48, 'TempMax': 51, 'TempMin': 45, 'Fog': 1}]


    >>> read_data('Lane-C19.csv')[:2]
    [{'Date': '1/1/21', 'Cases': 0, 'Deaths': 0}, {'Date': '1/2/21', 'Cases': 0, 'Deaths': 0}]
    """
    data = []
    floatnum_re = re.compile(r'^\d+\.\d+$')
    intnum_re = re.compile(r'^\d+$')
    with open(filename, 'r', encoding='utf-8') as the_file:
        reader = csv.DictReader(the_file)
        for row in reader:
            row_val = {}
            for key in row:
                if floatnum_re.match(row[key]):
                    row_val[key] = float(row[key])
                elif intnum_re.match(row[key]):
                    row_val[key] = int(row[key])
                else:
                    row_val[key] = str(row[key])
            data.append(row_val)
            pass

    return data


def extract_month(data: dict, month: int) -> list:
    """Extract the data for the given month.
    
    Args:
        data: The list of dictionaries created by read_data().
        month: The month number.
    
    Returns:
        A new list containing the data for the given month.
    """
    month_data = []
    match_month = re.compile('{month}')
    for i in range(len(data)):
        if match_month.match(str(data[i])):
            month_data.append(data[i])
    return month_data


def get_max(data: list, col: str) -> float:
    """Get the maximum value for the column.
    
    Args:
        data: The data dictionary.
        col: The column name.
    
    Returns:
        The maximum value for the column.
    """
    date_list = []
    for i in range(len(data)):
        date_list.append(data[i][col])
    return max(date_list)


def get_total(data: list, col: str) -> float:
    """Get the total value for the column.
    
    Args:
        data: The data dictionary.
        col: The column name.
    
    Returns:
        The total value for the column.
    """
    # TODO: Add your code here.
    date_list = []
    for i in range(len(data)):
        date_list.append(data[i][col])
    return sum(date_list)


def get_average(data: list, col: str) -> float:
    """Get the average value for the column.
    
    Args:
        data: The data dictionary.
        col: The column name.
    
    Returns:
        The average value for the column.
    """
    date_list = []
    for i in range(len(data)):
        date_list.append(data[i][col])
    return sts.mean(date_list)


# Optional: Extra-credit
def plot_trend(data: list, col: str, title: str) -> None:
    """Plot the trends for the given column in the given data.
    x-axis is the month, y-axis is the average value for the column.
    Save your figure in a file named f'{title}-{col}.png'
    
    Args:
        data: The data dictionary.
        col: The column name.
        ttle: The title for the dataset.
    """
    # TODO: Add your code here. (OPTIONAL, 80xp)
    pass


def debug():
    """Use for testing and debugging"""
    # TODO: Add your code here.
    pass


# ------- Do not modify print_stats(), use debug() instead. -------
def print_all_stats():
    """Main driver program."""
    MONTHS = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
              7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}

    weather_data = read_data('2021-Eugene-weather.csv')
    covid_data = read_data('Lane-C19.csv')

    if not weather_data or not covid_data:
        print('Error: read_data returned an empty list.')
        return

    for title, data in {'Weather': weather_data, 'COVID19': covid_data}.items():
        print(f'\n{24 * "-"} {title} data statistics {24 * "-"}')
        for month_num in range(1, 11):
            the_month_data = extract_month(data, month_num)
            for the_column in the_month_data[0].keys():
                if the_column == 'Date':
                    continue
                total = get_total(the_month_data, the_column)
                print(f'Total {the_column} in {MONTHS[month_num]}:'.rjust(24) \
                      + f'{total:>12.1f}')
                max = get_max(the_month_data, the_column)
                print(f'Max {the_column} in {MONTHS[month_num]}:'.rjust(24) \
                      + f'{max:>12.1f}')
                average = get_average(the_month_data, the_column)
                print(f'Average {the_column} in {MONTHS[month_num]}:'.rjust(24) \
                      + f'{average:>12.1f}\n')

        # Summary stats for all the months
        totals = {k: get_total(data, k) for k in data[0].keys() if k != 'Date'}
        averages = {k: get_average(data, k) for k in data[0].keys() if k != 'Date'}
        maxes = {k: get_max(data, k) for k in data[0].keys() if k != 'Date'}
        print(f"Summary:\n Totals: {totals}\n Averages: {averages}\n Max: {maxes}")
        print(f'\n{20 * "-"}  End of {title} statistics {20 * "-"}')

        # Plot the trends for the weather data (optional)
        for the_column in data[0].keys():
            if the_column == 'Date':
                continue
            plot_trend(data, the_column, title)


if __name__ == '__main__':
    debug()
    print_all_stats()
