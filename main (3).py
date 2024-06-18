from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2
  
def multiply(n1, n2):
  return n1 * n2
  
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add, 
  "-": subtract, 
  "*": multiply, 
  "/": divide
}

def calculator():

  print(logo)
  num1 = int(input("What's the first number?: \n"))
  #loop through the dictionary's keys
  for key in operations:
    print(key, end=" ")
    
  chosen_symbol = input("Pick an operation from the line above: \n")
  num2 = float(input("What's the second number?: \n"))
  calculation_function = operations[chosen_symbol]
  answer = calculation_function(num1, num2)
  
  print(f"{num1} {chosen_symbol} {num2} = {answer}")
  
  continue_or_exit = input(f"\nType 'y' to continue calculating with {answer}, or type 'n' to exit:")
  
  while continue_or_exit == "y":
    game = True
    if game is True:
        for key in operations:
          print(key, end=" ")
        chosen_symbol = input("Pick an operation from the line above: \n")
        num3 = float(input("What's the second number?: \n"))
        calculation_function = operations[chosen_symbol]
        last_answer = calculation_function(answer, num3)
        print(f"{answer} {chosen_symbol} {num3} = {last_answer}")
        continue_or_exit = input(f"\nType 'y' to continue calculating with {last_answer}, or type 'n' to exit:")
  if continue_or_exit == "n":
    calculator()

calculator()