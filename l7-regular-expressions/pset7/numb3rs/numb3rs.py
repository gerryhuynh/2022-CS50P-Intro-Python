import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.match(r"^(\d+\.){3}\d+$", ip):
        for num in ip.split("."):
            if not 0 <= int(num) <= 255:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()