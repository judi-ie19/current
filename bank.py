from datetime import datetime

class Account:
    def __init__(self,account_name,account_number):
            self.account_name=account_name
            self.account_number=account_number
            self.balance=0
            self.deposits=[]
            self.withdrawals=[]
            self.date=datetime.now().strftime("%x %X")
            self.transaction=100
            self.total=[]
            self.loan=0

    def deposit(self,amount):
        C={'date':self.date,'amount':amount,'naration':"deposit"}
        self.total.append(C)
        print(C)
        print(self.total)
        if amount<=0:
           return f'Depost must be positive amount'
        else:
           self.balance+=amount
           self.deposits.append(amount)
           print(self.deposits)
           
        return f'Hello {self.account_name} you balance is {self.balance} and your deposits{self.deposits}'
    def withdraw(self,amount):
        a={"date":self.date,"amount":amount,"naration":"deposit"}
        self.total.append(a)
        print(a)
        print(self.total)
        total=amount+self.transaction
        if amount<=0:
            return f"withdraw should be greater than zero"
         
        elif amount>self.balance:
            return f"your balance is{self.balance}and you can't withdraw {amount}"
    
        else:
            self.balance-=total
            self.withdrawals.append(amount)
            return f"Hello {self.account_name}, you have withdrwan {amount}. Your new balance is {self.balance}"  
            
    def deposits_statements(self):
        for statements in self.deposits:
            print(statements)

    def withdrawals_statement(self):
        
        for statement in self.withdrawals:

            print(statement)
    def current_balance(self):
        balance=self.balance
        return f"Hello{self.account_name} your balance is {balance}"
    def full_statement(self):
        for item in self.total:
            date=item['date']
            amount=item['amount']
            narration=item['naration']
            print(f"{date}_________ {narration}______{amount}")
    def borrow(self,amount):
        count=sum(self.deposits)
        if len(self.deposits)<10:
            print("you need 10 deposits to access a loan")
        elif amount<100:
            print("you cannot get a loan of 100")
        elif  amount>(1/3 *count):
          print("you are liable")
            
        elif self.loan!=0:
            print(f"youu have no oustanding loan")

            interest= 3/100*(amount)
            self.loan_balance+=amount+interest
            return f"Hello, customer you have borrowed {amount} your loan is now at {self.loan_balance}"
    
    def loan_repayment(self,amount):
        
         if amount>self.loan_balance:
             self.balance+=amount-self.loan_balance
             self.loan_balance=0
             return f" thank you for paying the loan of {amount-self.loan_balance} your account balance is {self.balance}"      
         else:
             self.loan_balance-=amount
             return f"thank you"
            
         
    def transfer(self,amount,new_account):
        if amount<=0:
            return "invalid amount"
        if amount>=self.balance:
            return f"Dear customer you have insuficient funds to make a transfer"
        if isinstance(new_account,Account):
            self.balance-=amount
            new_account.balance+=amount
            return f" Hello,you have sent {amount} to {new_account} with the name {new_account.name}.your new balance is {self.balance}.thank you"

        

    
    

        

