from validator_collection import validators


def main():
    email = input("What's your email address? ")

    try:
        validators.email(email)
    except ValueError:
        print("Invalid")
    else:
        print("Valid")


if __name__ == "__main__":
    main()