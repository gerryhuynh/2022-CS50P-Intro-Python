import emoji

def main():
  text = input("Input: ")
  icon = emoji.emojize(text, language="alias")

  print(f"Output: {icon}")


if __name__ == "__main__":
  main()