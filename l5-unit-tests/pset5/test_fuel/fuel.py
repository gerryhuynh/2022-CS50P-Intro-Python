from multiprocessing.sharedctypes import Value


def main():
    fuel_fraction = input("Fraction: ")
    fuel = convert(fuel_fraction)

    print(gauge(fuel))


def convert(fraction):
    x, y = fraction.split("/")
    if not x.isdigit() or not y.isdigit():
        raise ValueError
    elif y == "0":
        raise ZeroDivisionError
    else:
        fuel = int(x) / int(y)
        return fuel * 100


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{int(percentage)}%"


if __name__ == "__main__":
    main()