def main():
  amount = 50

  while amount > 0:
    print(f"Amount due: {amount}")
    coin = int(input("Insert Coin: "))

    if coin == 25 or coin == 10 or coin == 5:
      amount -= coin
  
  if amount < 0:
    amount *= -1
  
  print(f"Change owed: {amount}")


main()