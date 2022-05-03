from random import randint

def main():
  level = get_num("Level: ")

  rand_num = randint(1, level)

  guess = 0

  while guess != rand_num:
    guess = get_num("Guess: ")

    if guess > rand_num:
      print("Too large!")
    elif guess < rand_num:
      print("Too small!!")

  print("Just right!")


def get_num(prompt):
  while True:
    try:
      num = int(input(prompt))
    except ValueError:
      pass
    else:
      if num > 0:
        return num


if __name__ == "__main__":
  main()