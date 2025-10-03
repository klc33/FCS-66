balance =1000
def checkBalance():
    return balance

def depositMoney(deposit):
    global balance
    print(f"balance = {balance}")
    balance +=deposit
    return balance

def withdrawMoney(amount):
    global balance
    if balance >=amount:
        balance -= amount
        return balance
    else:
        raise ("Insufficient funds!")


print("``````````````````````````````````````````````````````````Welcome to the ATM")
print(f"Your balance is {balance}")
i = 1
while i>0:
    print("\n")
    print("1.Check Balance")
    print("2.Deposit Money")
    print("3.Withdraw Money")
    print("4.Exit")
    option = input("Choose an option: ")
    if option not in ["1","2","3","4"]:
        print("please only select from available options 1=>4!! ")
        continue
    else:
        if option =="1":
            print(f"Your balance is {checkBalance()}")
        elif option =="2":
            try:
                print(f"my balance is {balance}")
                deposit = input("Enter amount to deposit:")
                deposit = int(deposit)
                if deposit <0:
                     raise ValueError("Input number cannot be negative.")
                newBalance = depositMoney(deposit)
                print(f"Deposit successful. New balance = {newBalance}")
            except:
                print("please enter a non negative number!!")
        elif option =="3":
            try:
                withdrawnAmount = input("Enter amount to withdraw:")
                withdrawnAmount = int(withdrawnAmount)
                newBalance = withdrawMoney(withdrawnAmount)
                print(f"Withdrawal successful. New balance = {newBalance}")
        
                
            except ValueError:
                print(f"Please enter a number!")
            except:
                print(f"Insufficient funds!")
        elif option == "4":
            print("Goodbye!")
            break
            
        
        
            
