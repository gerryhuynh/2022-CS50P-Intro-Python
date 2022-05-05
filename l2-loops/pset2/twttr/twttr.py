from operator import lshift
from os import lseek

def main():
  text = input("Input: ")

  for letter in text:
    if letter.strip("aeiouAEIOU"):
      print(letter, end="")
  print()


main()