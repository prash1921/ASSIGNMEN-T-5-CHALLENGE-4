import sys
class account:
 bank ="canara bank"
def __init__(self,title=none,balance=0):
  self.title=title
  self.balance=balance
print("welcome to",account.bank)

def deposit(self,deposit):
    self.balance= self.balance+deposit
    print("balance after deposit:",self.balance)
    return self.balance

    def withdraw(self,withdraw):
        if self.balance<withdraw:
          print("insufficient balance")
          sys.exit()
        else:
           self.balance=self.balance-withdraw
    print("balance after withdraw :",self.balance)
    return self.balance

def get_balance(self):
    return self.balance


class savingsaccount(account):
 def __init__(self,title=none,balance=0,interestrate=0):
  super().__init__(title,balance)
self.interestrate=interestrate
def interestamount(self):
    print("interestrate :",self.interestrate)
    return self.interestrate

a=savingsaccount("prashansha",5000,5)
print(a.deposit(600))
a.withdraw(500)
print(a.withdraw(1500))
print(a.get_balance())
print(a.interestamount())