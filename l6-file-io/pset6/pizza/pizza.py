import csv
import sys
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")
else:
    file_name = sys.argv[1]

menu = []

try:
    with open(file_name) as file:
        reader = csv.reader(file)
        for row in reader:
            menu.append(row)
except FileNotFoundError:
    sys.exit("File does not exist")

print(tabulate(menu, headers="firstrow", tablefmt="grid"))