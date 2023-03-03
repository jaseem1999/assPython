class account:
    def _init_(self,accno):
        self.account_no=accno
        

class employee(account):
    def _init_(self,name,amount):
        super()._init_(accno)
        self.name=name
        self.amount=amount

class customer(account):
    def _init_(self,name,amount):
        super()._init_(name,amount)
        self.name=name
        self.amount=amount

class bank(employee,customer):
    def _init_(self,name,amount,accno,):
        super()._init_(name,amount)
        self.name = name
        self.amount = amount
    def deposit(self):
        self.deposit_amount=int(input("enter the amount to deposit:"))
        
    def withdraw(self):
        self.withdraw_amount=int(input("enter the amount to withdraw:"))
        
    def balance(self):
        self.amount=self.amount+self.deposit_amount
        self.amount=self.amount-self.withdraw_amount
    def display(self):
        print("account number",self.account_no)
        print("name:",self.name)
        print("balance:",self.amount)
        

    
obj=bank("fathima",1500,321,"shereen",4322,432)
