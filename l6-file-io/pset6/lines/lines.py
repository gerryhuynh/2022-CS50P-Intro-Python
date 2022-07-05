import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")
else:
    file_name = sys.argv[1]

num_lines = 0

try:
    with open(file_name) as file:
        for line in file:
            line = line.strip()
            if line != "" and not line.startswith("#"):
                num_lines += 1
except FileNotFoundError:
    sys.exit("File does not exist")

print(num_lines)