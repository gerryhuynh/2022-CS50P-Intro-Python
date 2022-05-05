def main():
  grocery_list = {}

  while True:
    try:
      grocery = input().upper().strip()
      grocery_list[grocery] += 1
    except EOFError:
      print("")
      for item in sorted(grocery_list):
        print(grocery_list[item], item)
      break
    except KeyError:
        grocery_list[grocery] = 1


if __name__ == "__main__":
  main()