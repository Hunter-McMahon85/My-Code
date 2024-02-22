"""
Hunter McMahon
CIS 210
P7
Description: there was room on the board for Jack too, he didnt have to die in the movie
"""
# import some helpful tools
import statistics as sts
import matplotlib.pyplot as plt
import csv


# 7.1 imports our data in a desirable format
def load_data(file_name: str, types: dict) -> dict:
    """
    loads our data into a dictionary with specified names/values
    Args:
        file_name:
            (str) the file with out raw data
        types:
            (dict) the keys that the data will be loaded/sorted under
    Returns:
        (dict) the data as a sorted dictionary
    >>> load_data('Titanic-clean.csv', {'PassengerId': int, 'Survived': int})
    """
    loaded_data = {}
    lines_info = []
    iteration = 0
    for key in types:
        loaded_data[tuple((key, types[key]))] = []
    # open our csv data
    with open(str(file_name), 'r', encoding="utf-8", newline='') as raw_data:
        interpret_data = csv.reader(raw_data)
        for line in interpret_data:
            lines_info.append(line)
    # get our CSV data sorted appropriately
    for key in loaded_data:
        new_value = []
        converter = key[1]
        for i in range(1, len(lines_info)):
            new_value.append(converter(lines_info[i][iteration]))
        loaded_data[key] = new_value
        iteration += 1
    return loaded_data


# 7.2 print a summary of the data
def summarize(data: dict):
    """
    takes a dictionary of data and summarizes it, printing the result
    Args:
        data:
            (dict) the input dictionary containing the data we intend to summarize
    Returns:
        (none) function is void, just prints results
    >>> summarize({('Col1',int): [1, 3, 2, 1], ('Col2', str): ['a','b','a']})
    Statistics for Col1:
        min:    1.0
        max:    3.0
       mean:    1.8
      stdev:    1.0
       mode:    1.0
    Statistics for Col2:
    Number of unique values: 2
          Most common value: a
    >>> summarize({})

    >>> summarize({('Col1',float): [1.3, 5.3, 102, 0.1]})
    Statistics for Col1:
        min:    0.1
        max:  102.0
       mean:   27.2
      stdev:   49.9
       mode:    1.3
    """
    for key in data:
        d_list = data[key]
        if key[1] == str:
            # find the stats
            most_used = ''
            occurance = 0
            unique_values = []
            for i in d_list:
                if d_list.count(i) > occurance:
                    most_used = i
                    occurance += d_list.count(i)
                if i not in unique_values:
                    unique_values.append(i)
            # print the stats
            print('Statistics for ' + key[0] + ':\n' +
                  'Number of unique values: ' + str(len(unique_values)) + '\n' +
                  'Most common value: '.rjust(25) + str(most_used))
        elif key[1] == int or float:
            # find the stats
            val_min = round(float(min(d_list)), 1)
            val_max = round(float(max(d_list)), 1)
            mean = round(float(sts.mean(d_list)), 1)
            mode = round(float(sts.mode(d_list)), 1)
            standard_deviation = round(float(sts.stdev(d_list)), 1)
            # print the stats
            print('Statistics for ' + key[0] + ':\n' +
                  'min:'.rjust(8) + str(val_min).rjust(7) + '\n' +
                  'max:'.rjust(8) + str(val_max).rjust(7) + '\n' +
                  'mean:'.rjust(8) + str(mean).rjust(7) + '\n' +
                  'stdev:'.rjust(8) + str(standard_deviation).rjust(7) + '\n' +
                  'mode:'.rjust(8) + str(mode).rjust(7))
        # end of summarize


# 7.3 get correlation
def pearson_corr(x: list, y: list) -> float:
    """
    calculate Pearsons correlation for two data sets with the stats module
    Args:
        x:
            (list) data to correlate with the theoretical x-axis
        y:
            (list) data to correlate with the theoretical y-axis

    Returns:
        (float) the value of the pearsons correlation for the two list rounded to 2 decimals
        >>> pearson_corr([1, 2, 3], [2, 3, 5])
        0.98
        >>> pearson_corr(['a', 'b'], [0, 1])
        Traceback (most recent call last):
        ...
        ValueError: pearson_corr only works with int or float lists.
        >>> pearson_corr([1, 2, 3], [2, 3])
        Traceback (most recent call last):
        ...
        ValueError: The list parameters must have the same number of elements.
    """
    # note that in python 3.10 this can be done in under 30 characters
    # as the statistics module in 3.10 has a built in correlation function
    # thus in 3.10 this code would be as simple as:
    # return sts.correlation(x, y)
    if isinstance(x[0], (int, float)) and isinstance(y[0], (int, float)):
        x_avg = sts.mean(x)
        y_avg = sts.mean(y)
        x_devi = sts.stdev(x)
        y_devi = sts.stdev(y)
        sum_xy = 0.0
        if len(x) == len(y):
            for i in range(len(x)):
                sum_xy += (x[i] - x_avg) * (y[i] - y_avg)
            pear = sum_xy / ((len(x) - 1) * x_devi * y_devi)
            return round(pear, 2)
        else:
            raise ValueError('The list parameters must have the same number of elements.')
    else:
        raise ValueError('pearson_corr only works with int or float lists.')


# 7.4

def survivor_vis(data: dict, col1: tuple, col2: tuple) -> plt.Figure:
    """
    visualizes the data on a scatter-plot of two parameters and shows who died/survived based on symbol and saves it
    Args:
        data:
            (dict) the full set of data
        col1:
            (tuple) 1 of 2 elements of data we want to use as one side of the scatter plot
        col2:
            (tuple) 1 of 2 elements of data we want to use as one side of the scatter plot
    Returns:
        the scatterplot object
    """
    deceased = []
    survived = []
    c1_survive = []
    c2_survive = []
    c1_dead = []
    c2_dead = []
    for i in range(len(data[('Survived', int)])):
        if 1 == data[('Survived', int)][i]:
            survived.append(i)
        else:
            deceased.append(i)
    for i in deceased:
        c1_dead.append(data[col1][i])
        c2_dead.append(data[col2][i])
    for i in survived:
        c1_survive.append(data[col1][i])
        c2_survive.append(data[col2][i])

    fig = plt.figure()
    plt.scatter(x=c1_survive, y=c2_survive, c='g')
    plt.scatter(x=c1_dead, y=c2_dead, marker='x', c='r')
    plt.title("Survival data of Titanic Passengers")
    plt.legend(labels=['Survived', 'Deceased'])
    plt.xlabel(col1[0]), plt.ylabel(col2[0])
    plt.savefig(f'scatter-{col1[0]}-{col2[0]}.png')
    plt.show(block=False)
    return fig


# ------ You shouldn't have to modify main --------
def main():
    """Main program driver for Project 7."""

    # 7.1 Load the dataset
    TITANIC_TYPES = {'PassengerId': int, 'Survived': int, 'Pclass': int,
                     'Sex': str, 'Age': float, 'SibSp': int, 'Parch': int,
                     'Fare': float, 'Embarked': str, 'FamilySize': int,
                     'age_group': str}
    data = load_data('Titanic-clean.csv', TITANIC_TYPES)
    # 7.2 Print informative summaries
    print("\nPart 7.2")
    summarize(data)

    print("\nPart 7.3")
    # 7.3 Compute correlations between age and survival
    corr_age_survived = pearson_corr(data[('Age', float)],
                                     data[('Survived', int)])
    print(f'Correlation between age and survival is {corr_age_survived:3.2f}')

    # 7.3 Correlation between fare and survival
    corr_fare_survived = pearson_corr(data[('Fare', float)],
                                      data[('Survived', int)])
    print(f'Correlation between fare and survival is {corr_fare_survived:3.2f}')

    # 7.3 Correlation between family size and survival
    corr_fare_survived = pearson_corr(data[('FamilySize', int)],
                                      data[('Survived', int)])
    print(f'Correlation between family size and survival is'
          f' {corr_fare_survived:3.2f}')

    # 7.4 Visualize results
    fig = survivor_vis(data, ('Age', float), ('Fare', float))
    fig = survivor_vis(data, ('Age', float), ('Pclass', int))
    fig = survivor_vis(data, ('Age', float), ('Parch', int))


if __name__ == "__main__":
    main()
