def main():
  fuel = get_fuel()

  if fuel < 1:
    print("E")
  elif fuel > 99:
    print("F")
  else:
    print(f"{int(fuel)}%")


def get_fuel():
  while True:
    try:
      fuel_fraction = input("Fraction: ")
      x, y = fuel_fraction.split("/")
      fuel = int(x) / int(y)
    except (ValueError, ZeroDivisionError):
      pass
    else:
      if fuel > 1:
        pass
      else:
        return fuel * 100


if __name__ == "__main__":
  main()