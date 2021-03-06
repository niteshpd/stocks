#  Get names of all stocks in the CSV file as a list(Location passed as a parameter)
#  The names must be in the first column of the CSV
import csv


def _list(csv_path="tickers.csv"):
    names_list = []
    with open(csv_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for rows in csv_reader:
            names_list.append(rows[0] + '.NS')  # <Name>.NS is the format Yahoo finance follows instead of plain <Name>
    return names_list


def _string():
    names_list = _list()
    names_string = ""
    return names_string + ' '.join(names_list)


if __name__ == "__main__":
    print(_string())  # Testing the _string() function

