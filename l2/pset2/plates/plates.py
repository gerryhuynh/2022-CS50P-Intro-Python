def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    """
    - vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters
    - No periods, spaces, or punctuation marks are allowed
    - All vanity plates must start with at least two letters
    - Numbers cannot be used in the middle of a plate; they must come at the end
    - The first number used cannot be a ‘0’.
    """

    if 1 < len(s) < 7:
      if s.isalnum():
        if s[0:2].isalpha():
          if valid_num(s):
            return True

    return False


def valid_num(s):
  """
  - Check if the letter is a number
  - If it's the first number, it can't be 0; it would be invalid
  - If there are more letters after a number first appeared, then that would be invalid too
  """
  number = 0

  for letter in s:
    if letter.isdigit():
      if number == 0 and letter == "0":
        return False
      number = 1
    elif letter.isalpha() and number == 1:
      return False
  
  return True

main()