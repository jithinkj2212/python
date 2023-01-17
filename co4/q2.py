class Bank:
    def __init__(self,acNumber,name,acType,balance):
        self.acNumber=acNumber
        self.name=name
        self.acType=acType
        self.balance=balance
    def deposit(self):
        amount=int(input("Enter the amount to deposit:"))
        self.balance+=amount
        print("current balance: ",self.balance)
    def withDraw(self):
        amount=int(input("Enter the amount to withdraw:"))
        if self.balance<amount:
            print("ERROR...!")
        else:
            self.balance-=amount
            print("Remaining balance: ",self.balance)
    def __str__(self):
        print("A/C Number:",self.acNumber,"\nName:",self.name)
        print("your account type:",self.acType,"\ncurrent balance:",self.balance)

flag=1
print("OPTION\n1.To Enter the details\n2.To deposit\n3.To withdraw\n4.To display")
while flag!=0:
    flag=int(input("Enter your choice:"))
    match flag:
        case 1:
            acNumber=int(input("Enter your account number:"))
            name=input("Enter your name:")
            acType=input("Enter your account type:")
            balance=int(input("Enter your current balance:"))
            user1=Bank(acNumber,name,acType,balance)

        case 2:
            user1.deposit()
        case 3:
            user1.withDraw()
        case 4:
            print(user1.__str__())
        case _:
            print("invalid option")
            
