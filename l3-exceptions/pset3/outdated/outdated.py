def main():
  months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
  ]

  while True:
    try:
      date = input("Date: ")
      
      if date.find("/") != -1:
        m, d, y = date.split("/")
        m = int(m)

      else:
        m, d, y = date.split()

        if m.isalpha():
          m = months.index(m) + 1
        
        if d.find(","):
          d = d.rstrip(",")
      
      d = int(d)

    except ValueError:
      pass
    else:
      if m < 0 or m > 12 or d < 0 or d > 31:
        pass
      else:
        break

  print(f"{y}-{m:02}-{d:02}")

if __name__ == "__main__":
  main()