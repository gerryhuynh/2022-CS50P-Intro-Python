def main():
  camel_text = input("camelCase: ")

  print("snake_case: ", end="")

  for letter in camel_text:
    if letter.isupper():
      letter = letter.replace(letter, "_" + letter.lower())
    
    print(letter, end="")
  
  print()


main()