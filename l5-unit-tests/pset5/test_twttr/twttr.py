def main():
    text = input("Input: ")
    print(shorten(text))


def shorten(word):
    new_text = []
    for letter in word:
        if letter.strip("aeiouAEIOU"):
            new_text.append(letter)
    return "".join(new_text)


if __name__ == "__main__":
    main()