"""
Final Exam Question 6
CIS 210
Hunter McMahon
Desc: its the final countdown *epic horns blaring*
"""
import csv


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


def main():
    expense_in = extract_data('expenses_and_income.csv')
    income = 0
    expenses = 0
    for i in range(len(expense_in)):
        income += float(expense_in[i]['Income'])
        expenses += float(expense_in[i]['Expense'])
    print("Income:" + str(round(income, 2)).rjust(13) + '\n' +
          "Expenses:" + str(round(expenses, 2)).rjust(11))


if __name__ == "__main__":
    main()
