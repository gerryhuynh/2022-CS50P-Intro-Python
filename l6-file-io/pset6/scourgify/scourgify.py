import csv
import sys

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        file_1 = sys.argv[1]
        file_2 = sys.argv[2]

    characters = []

    try:
        with open(file_1) as file:
            reader = csv.reader(file)
            for row in reader:
                characters.append(row)
    except FileNotFoundError:
        sys.exit(f"Could not read {file_1}")

    with open(file_2, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        
        for character in characters[1:]:
            last_name, first_name = character[0].split(", ")
            house = character[1]

            writer.writerow({"first": first_name, "last": last_name, "house": house})

if __name__ == "__main__":
    main()