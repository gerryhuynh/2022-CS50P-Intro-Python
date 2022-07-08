import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"(1?\d):?(\d\d)? (AM|PM) to (1?\d):?(\d\d)? (AM|PM)", s.strip()):
        time_1 = {}
        time_1["h"] = int(matches.group(1))

        time_2 = {}
        time_2["h"] = int(matches.group(4))
        
        if matches.group(2) and matches.group(5):
            time_1["m"] = int(matches.group(2))
            time_2["m"] = int(matches.group(5))
        else:
            time_1["m"] = 0
            time_2["m"] = 0
        
        time_1["ap"] = matches.group(3)
        time_2["ap"] = matches.group(6)

    else:
        raise ValueError("Incorrect format")

    if not 0 <= time_1["m"] < 60 or not 0 <= time_2["m"] < 60:
        raise ValueError("Invalid minutes")
    
    if not 1 <= time_1["h"] <= 12 or not 1 <= time_2["h"] <= 12:
        raise ValueError("Invalid hours")

    time_1 = convert_ap(time_1)
    time_2 = convert_ap(time_2)

    return f"{time_1['h']:02}:{time_1['m']:02} to {time_2['h']:02}:{time_2['m']:02}"


def convert_ap(time):
    if time["ap"] == "PM" and 1 <= time["h"] < 12:
        time["h"] += 12
    elif time["ap"] == "AM" and time["h"] == 12:
        time["h"] = 0
    
    return time


if __name__ == "__main__":
    main()