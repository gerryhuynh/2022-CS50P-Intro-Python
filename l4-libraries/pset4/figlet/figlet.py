import random
import sys

from pyfiglet import Figlet


def main():
  # Check number of command-line arguments
  if len(sys.argv) not in [1, 3]:
    sys.exit("Invalid usage")

  figlet = Figlet()

  # Check -f/--font and assign font
  if len(sys.argv) == 1:
    f = random.choice(figlet.getFonts())
  elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
    f = sys.argv[2]
  else:
    sys.exit("Invalid usage")
  
  # Check valid font
  try:
    figlet.setFont(font=f)
  except:
    sys.exit("Invalid usage")

  text = input("Input: ")
  
  print("Output:")
  print(figlet.renderText(text))


if __name__ == "__main__":
  main()