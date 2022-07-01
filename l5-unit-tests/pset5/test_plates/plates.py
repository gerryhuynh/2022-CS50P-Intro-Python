def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 1 < len(s) < 7:
      if s.isalnum():
        if s[0:2].isalpha():
          if valid_num(s):
            return True

    return False


def valid_num(s):
  number = 0

  for letter in s:
    if letter.isdigit():
      if number == 0 and letter == "0":
        return False
      number = 1
    elif letter.isalpha() and number == 1:
      return False
  
  return True


if __name__ == "__main__":
    main()