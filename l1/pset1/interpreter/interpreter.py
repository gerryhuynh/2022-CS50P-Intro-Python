def main():
  expr = input("Expression: ").lower().strip()

  x, y, z, = expr.split()

  x = float(x)
  z = float(z)
  
  print(answer(x, y, z))

def answer(num1, operation, num2):
  if operation == "+":
    return num1 + num2
  elif operation == "-":
    return num1 - num2
  elif operation == "*":
    return num1 * num2
  elif operation == "/":
    return num1 / num2

main()