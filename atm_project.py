# Show welcome message and ask user to insert ATM card
print("Welcome to MEST ATM! Kindly insert your atm card")
user_name = input("Enter your name>>> \n")
user_number = input("Enter your serial number>>> \n")
# Ask user to enter pin
user_pin = 1234
balance = 10000.00

def pin_authentication():
   while True:
      try:
         pin = int(input("Enter your pin>> \n"))
         if pin == user_pin:
           print("Authentication successful. ")
           return True 
         else:
           print("Authentication failed")
      except ValueError:
         print("Invalid pin - Try again! ")

# Display Options
def options():
   print("\n==== SERVICES AVAILABLE ====")
   print("1. Check Balance")
   print("2. Deposit")
   print("3. Withdraw")
   print("4. Exit")

def check_balance():
   print(f"Your current balance is: ${balance:.2f}")

def deposit():
   global balance
   try:
      amount = float(input("Enter amount to deposit: \n"))
      if amount <= 0:
         print("Please enter a positive amount. \n")
      else:
         balance += amount
         print(f"${amount:.2f} deposited successfully.")
         check_balance()
   except ValueError:
    print("Invalid input. Please enter a number.")

def withdraw():
   global balance
   try:
      amount = float(input("Enter amount to withdraw: \n"))
      if amount <= 0:
       print("Please enter a positive amount. \n")
      elif amount > balance:
       print("Insufficient balance.")
      else:
         balance -= amount
         print(f"${amount:.2f} withdrawn successfully.")
         check_balance()
   except ValueError:
    print("Invalid input. Please enter a number.")

def run():
   if not pin_authentication():
      return
   while True:
      options()
      choice = input("Select an option (1-4): \n")
      if choice == '1':
         check_balance()
      elif choice == '2':
         deposit()
      elif choice == '3':
         withdraw()
      elif choice == '4':
        break
   print("Thank you for using the ATM. Goodbye!")

if __name__ == '__main__':
  run()