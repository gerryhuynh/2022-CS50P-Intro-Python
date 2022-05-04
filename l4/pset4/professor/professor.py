import random


def main():
    level = get_level()

    problem_num = 0
    score = 0

    while problem_num < 10:
      x = generate_integer(level)
      y = generate_integer(level)

      tries = 0

      while tries < 3:
        try:
          answer = int(input(f"{x} + {y} = "))
        except ValueError:
          print("EEE")
        else:
          if answer == x + y:
            break
          else:
            print("EEE")
            tries += 1
      
      if tries == 0:
        score += 1
      elif tries == 3:
        print(f"{x} + {y} = {x + y}")

      problem_num += 1
    
    print(f"Score: {score}")


def get_level():
    while True:
      try:
        level = int(input("Level: "))
      except ValueError:
        pass
      else:
        if 0 < level < 4:
          return level


def generate_integer(level):
    if level == 1:
      return random.randint(0, 9)
    elif level == 2:
      return random.randint(10, 99)
    elif level == 3:
      return random.randint(100, 999)
    else:
      raise ValueError


if __name__ == "__main__":
    main()