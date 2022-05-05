import json
import requests
import sys


def main():
  # Check appropriate number of command-line arguments
  if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")
  elif len(sys.argv) > 2:
    sys.exit("Too many arguments\nUsage: python bitcoin.py n_bitcoins")
  
  # Convert command-line argument to float and check for error
  try:
    n_bitcoins = float(sys.argv[1])
  except ValueError:
    sys.exit("Command-line argument is not a number")

  response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

  rate = float(response.json()["bpi"]["USD"]["rate"].replace(",", "")) 
  
  cost = rate * n_bitcoins

  print(f"${cost:,.4f}")


if __name__ == "__main__":
    main()