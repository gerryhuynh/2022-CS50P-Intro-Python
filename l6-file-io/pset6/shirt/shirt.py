from os.path import splitext
from PIL import Image, ImageOps
import sys

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].lower().endswith((".jpg", ".jpeg", ".png")) or not sys.argv[2].lower().endswith((".jpg", ".jpeg", ".png")):
        sys.exit("Invalid input")
    elif splitext(sys.argv[1])[1] != splitext(sys.argv[2])[1]:
        sys.exit("Input and output have different extensions")
    else:
        before = sys.argv[1]
        after = sys.argv[2]

    try:
        shirt = Image.open("shirt.png")
    except FileNotFoundError:
        sys.exit(f"Could not read shirt.png")
    
    shirt_size = shirt.size

    try:
        photo = Image.open(before)
    except FileNotFoundError:
        sys.exit(f"Could not read {before}")

    photo = ImageOps.fit(photo, shirt_size)
    photo.paste(shirt, shirt)
    photo.save(after)


if __name__ == "__main__":
    main()