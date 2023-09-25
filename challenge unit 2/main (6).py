''' Implement a class called BankAccount that respresents a bank account . 
the class should have private attributes for account number, account holder name , 
and deposit money , withdraw money , and display the account balance. 
ensure that the account balance cannot be accessed directly from outside the class.
write a program to create an instance of the bankAccount class and test the deposit and withdrawal fuctionally.'''


class BankAccount:

  def __init__(self , account_number, account_holder_name,initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance

  def deposit(self , amount):
    if amount > 0:
      self.__account_balance += amount
      #sekf.__account_balance = self._account_balance+amount
      print("deposited ₹{}. New balance: ₹{}" .format(amount,self.__account_balance))
    else:
      print("invalid deposit amount.")
      
def withdraw(self , amount):
   if amount > 0 and amount <= self.__account_balance:
     self.__account_balance -= amount
     print("withdrew ₹{}. new balance: ₹{}" .format(amount,self.__account_balance))
   else:
     print("invalid withdrawal amount or insufficient balance.")

def display_balance(self):
  print("Account balance for {} (Account #{}): ₹{}".format(
        self.__account_holder_name, self.__account_number,
        self.__account_balance))


#create an instance of the BankAccount class
account= BankAccount(account_number="123456789",
                     account_holder_name="hari prabu",
                     initial_balance=5000.0)

#test deposit and withdrawal functionality
#account.display_balance()
account.deposit(500.0)
#account.withdraw(200.0)
#account.withdraw(20000.0)
#account.display_balance()

  