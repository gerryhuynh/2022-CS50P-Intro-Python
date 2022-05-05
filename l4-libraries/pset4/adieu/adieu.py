import inflect

def main():
  p = inflect.engine()
  names = []

  while True:
    try:
      new_name = input("Name: ")
      names.append(new_name)
    except EOFError:
      print(f"\nAdieu, adieu, to {p.join(names)}")
      break


if __name__ == "__main__":
  main()