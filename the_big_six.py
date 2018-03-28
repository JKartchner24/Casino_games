import random

print("Step right up and test your luck on, The Big Six Wheel!")
spin_wheel = input("Would you like to take a chance at the wheel? Type yes or no. ")

balance = int(100)

  
def wheel_chance():
  global balance
  wheel_pc = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'D', 'D', 'D', 'D', 'E', 'E', 'F', 'G']
  rand_item = random.choice(wheel_pc)
  if rand_item == "A":
    print("congratulations you just won $1!!")
    balance= balance + 1
    print('You have', balance, 'dollars')
    play_again()
      
  elif rand_item == "B":
    print("congratulations you just won $2!!")
    balance= balance + 2
    print('You have',balance, 'dollars')
    play_again()
      
  elif rand_item == "C":
    print("congratulations you just won $5!!")
    balance= balance + 5
    print('You have',balance, 'dollars')
    play_again()
      
  elif rand_item == "D":
    print("congratulations you just won $10!!")
    balance= balance + 10
    print('You have',balance, 'dollars')
    play_again()
      
  elif rand_item == "E":
    print("congratulations you just won $20!!")
    balance= balance + 20
    print('You have',balance, 'dollars')
    play_again()
      
  elif rand_item == "F":
    print("You landed on the robber you lost $100 ....")
    balance= balance -100
    print('You have',balance, 'dollars')
    play_again()
      
  elif rand_item == "G":
    print("You hit the JACKPOT!!!!!!")
    balance= balance + 100
    print('You have',balance, 'dollars')
    play_again()
      
def play_again():
  spin_wheel_again = input("Would you like to take a chance at the wheel again? Type yes or no. ")
  if spin_wheel_again == "yes":
    wheel_chance()
    
  elif spin_wheel_again == "no":
    print("goodbye")
    exit()

      
if spin_wheel == "no":
  print("Have a nice day!")
      
elif spin_wheel == "yes":
  wheel_chance()
