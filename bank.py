class Account:
    def __init__(self,account_name,account_number):
            self.account_name=account_name
            self.account_number=account_number
            self.balance=0
            self.deposits=[]
            self.withdrawals=[]
            self.transaction=100

    def deposit(self,amount):
        if amount<=0:
           return f'Depost must be positive amount'
        else:
           self.balance+=amount
           self.deposits.append(amount)
        return f'Hello {self.account_name} you balance is {self.balance} and your deposits{self.deposits}'
    def withdraw(self,amount):
        if amount<=0:
            
          return f"your balance is {self.balance},you can't withdraw{amount}" 
        else:
            self.balance-=amount+self.transaction
            self.withdrawals.append(amount)
            return f"Hello {self.account_name}, you have withdrwan {amount}. Your balance is {self.withdrawals}"  
    def deposits_statements(self):
        for statements in self.deposits:
            print(statements)

    def withdrawals_statement(self):
        for statements in self.withdrawals:
            print(statements)
    def current_balance(self):
        balance=self.balance
        print(balance)

