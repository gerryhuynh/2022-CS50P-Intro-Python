def main():
  time = input("What time is it? ").lower().strip()

  hours = convert(time)

  if 7 <= hours <= 8:
    print("breakfast time")
  elif 12 <= hours <= 13:
    print("lunch time")
  elif 18 <= hours <= 19:
    print("dinner time")


def convert(time):
  hour, minute = time.split(":")

  hour = float(hour)

  if hour == 12 and minute.endswith("a.m."):
    hour = 0
  if hour != 12 and minute.endswith("p.m."):
    hour += 12

  minute = float(minute.strip("apm. "))

  return hour + minute / 60


if __name__ == "__main__":
  main()