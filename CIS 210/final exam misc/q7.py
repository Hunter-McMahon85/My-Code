"""
Final Exam Question 7
CIS 210
Hunter McMahon
Desc: its the final countdown *epic horns blaring* pt 2
"""
import csv


# take our extract data function from q6
def extract_data(file_name: str) -> list:
    """
    loads our data into dictionaries for each row then puts them into a list
    Args:
        file_name:
            (str) the file containing our raw data
    Returns:
        (list) the data as a list of dictionaries representing each row

    """
    list_o_data = []
    with open(file_name, 'r', encoding="utf-8") as data:
        read_data = csv.DictReader(data)
        for line in read_data:
            list_o_data.append(line)
    return list_o_data


def expense_data_sort_cat(input_list: list) -> dict:
    """
    takes our data list and sorts the data into a dict categorizing expense types
    Args:
        input_list:
            (list) our list of dictionaries of raw data
    Returns:
        cat:
            (dict) the sorted dict with our expenses data
    """
    cat = {}
    for i in range(len(input_list)):
        if input_list[i]['Category'] not in cat:
            cat[input_list[i]['Category']] = []
    if 'income' in cat:
        cat.pop('income')
    for key in cat:
        for i in range(len(input_list)):
            if input_list[i]['Category'] == key:
                cat[key].append(float(input_list[i]['Expense']))
    return cat


def main():
    expense_in = extract_data('expenses_and_income.csv')
    income = 0
    expenses = 0
    expense_sorted = expense_data_sort_cat(expense_in)
    print('EXPENSE TOTALS:'.rjust(25))
    for key in expense_sorted:
        print(key.rjust(24) + ':' + '$'.rjust(11) + str(round(sum(expense_sorted[key]), 2)))



if __name__ == "__main__":
    main()
