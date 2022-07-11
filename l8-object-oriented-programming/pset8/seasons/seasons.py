from datetime import date
import inflect
import re
import sys


def main():
    dob = input("Date of Birth: ").strip()

    print(age_in_minutes(dob))


def age_in_minutes(dob):
    if not re.search("^\d{4}-\d{2}-\d{2}$", dob):
        sys.exit("Invalid date")

    year, month, day = dob.split("-")

    dob = date(int(year), int(month), int(day))

    age_days = (date.today() - dob).days

    age_minutes = age_days * 24 * 60

    p = inflect.engine()

    return p.number_to_words(age_minutes, andword="").capitalize() + " minutes"


if __name__ == "__main__":
    main()