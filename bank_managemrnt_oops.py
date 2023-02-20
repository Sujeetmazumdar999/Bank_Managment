class User:
    def __init__(self,name,age,gender,accnumber):
        self.name= ["Rahul","Sujeet","Akansha"]
        self.age=['23','34','18']
        self.gender=['M','M','F']
        self.balance = [0,0,0,0,0,0]
        self.accnumber=['4334','4343','6566','6777','9087','4343']
        self.newname=[]
        self.newage = []
        self.newgender = []





    def showDetails(self,name):
        self.name=name
        print("====PERSONAL DETAILS====")
        print(self.newname)

        if name == "Rahul":
            print("Name=",name,'\n',"Age=",self.age[0],'\n',"Gender=",self.gender[0],'\n',"Account Number=",self.accnumber[0])

        elif name == "Sujeet":
                print("Name=",name,'\n',"Age=",self.age[1],'\n',"Gender=",self.gender[1],'\n',"Account Number=",self.accnumber[1])

        elif name == "Akansha":
                print("Name=",name,'\n',"Age=",self.age[2],'\n',"Gender=",self.gender[2],'\n',"Account Number=",self.accnumber[2])

        elif name == self.newname[0]:
            print("Name=",name,'\n',"Age=",self.newage[0],'\n',"Gender=",self.newgender[0],'\n',"Account Number=",self.accnumber[3])


        elif name == self.newname[1]:
            print("Name=",name,'\n',"Age=",self.newage[1],'\n',"Gender=",self.newgender[1],'\n',"Account Number=",self.accnumber[4])


        elif name == self.newname[2]:
            print("Name=",name,'\n',"Age=",self.newage[2],'\n',"Gender=",self.newgender[2],'\n',"Account Number=",self.accnumber[5])

        else:
            print("User not found")


    def openacc(self,name,age,gender):
        self.newname.append(name)
        self.newage.append(age)
        self.newgender.append(gender)
        print("Bank account open successfully:")



class Bank(User):
    def __init__(self, name, age, gender,accnumber):
        super().__init__(name, age, gender,accnumber)

    def deposit(self, amount,name):
        self.name=name
        if name == "Rahul":
            self.amount = int(amount)
            self.balance [0]= self.balance [0]+ self.amount
            print("Account Balance Has Been Updated : ", self.balance[0])

        elif name == "Sujeet":
            self.amount = int(amount)
            self.balance[1] = self.balance[1] + self.amount
            print("Account Balance Has Been Updated : ", self.balance[1])

        elif name == "Akansha":
            self.amount = int(amount)
            self.balance[2] = self.balance[2] + self.amount
            print("Account Balance Has Been Updated : ", self.balance[2])

        elif name == self.newname[0]:
            self.amount = int(amount)
            self.balance[3] = self.balance[3] + self.amount
            print("Account Balance Has Been Updated : ", self.balance[3])

        elif name == self.newname[1]:
            self.amount = int(amount)
            self.balance[4] = self.balance[4] + self.amount
            print("Account Balance Has Been Updated : ", self.balance[4])

        elif name == self.newname[2]:
            self.amount = int(amount)
            self.balance[5] = self.balance[5] + self.amount
            print("Account Balance Has Been Updated : ", self.balance[5])

        else:
            print("User not found")


    def withdraw(self, amount,name):
        self.name=name
        if name == "Rahul":
            self.amount = int(amount)
            if self.amount > self.balance[0]:
                print("Insuficiant fund", self.balance[0])
            else:
                self.balance[0] = self.balance[0] - self.amount
                print("Account Balance Has Been Updated : ", self.balance[0])

        elif name == "Sujeet":
            self.amount = int(amount)
            if self.amount > self.balance[1]:
                print("Insuficiant fund", self.balance[1])
            else:
                self.balance[1] = self.balance[1] - self.amount
                print("Account Balance Has Been Updated : ", self.balance[1])

        elif name == "Akansha":
            self.amount= int(amount)
            if self.amount > self.balance[2]:
                print("Insuficiant fund", self.balance[2])
            else:
                self.balance[2] = self.balance[2]- self.amount
                print("Account Balance Has Been Updated : ", self.balance[2])

        elif name == self.newname[0]:
            self.amount = int(amount)
            if self.amount > self.balance[3]:
                print("Insuficiant fund", self.balance[3])
            else:
                self.balance[3] = self.balance[3] - self.amount
                print("Account Balance Has Been Updated : ", self.balance[3])

        elif name == self.newname[1]:
            self.amount = int(amount)
            if self.amount > self.balance[4]:
                print("Insuficiant fund", self.balance[4])
            else:
                self.balance[4] = self.balance[4] - self.amount
                print("Account Balance Has Been Updated : ", self.balance[4])

        elif name == self.newname[2]:
            self.amount = int(amount)
            if self.amount > self.balance[5]:
                print("Insuficiant fund", self.balance[5])
            else:
                self.balance[5] = self.balance[5] - self.amount
                print("Account Balance Has Been Updated : ", self.balance[5])


        else:
            print("User not found")

    def viewbalance(self,name):
        self.name=name
        print("====PERSONAL DETAILS====")
        if name == "Rahul":
            print("Name=",name,'\n',"Age=",self.age[0],'\n',"Gender=",self.gender[0],'\n',"Account Number=",self.accnumber[0],'\n',"Account Balance",self.balance[0])

        elif name == "Sujeet":
            print("Name=",name,'\n',"Age=",self.age[1],'\n',"Gender=",self.gender[1],'\n',"Account Number=",self.accnumber[1],'\n',"Account Balance",self.balance[1])

        elif name == "Akansha":
            print("Name=",name,'\n',"Age=",self.age[2],'\n',"Gender=",self.gender[2],'\n',"Account Number=",self.accnumber[2],'\n',"Account Balance",self.balance[2])

        elif name == self.newname[0]:
            print("Name=",name,'\n',"Age=",self.newage[0],'\n',"Gender=",self.newgender[0],'\n',"Account Number=",self.accnumber[3],'\n',"Account Balance",self.balance[3])

        elif name == self.newname[1]:
            print("Name=",name,'\n',"Age=",self.newage[1],'\n',"Gender=",self.newgender[1],'\n',"Account Number=",self.accnumber[4],'\n',"Account Balance",self.balance[4])

        elif name == self.newname[2]:
            print("Name=",name,'\n',"Age=",self.newage[2],'\n',"Gender=",self.newgender[2],'\n',"Account Number=",self.accnumber[5],'\n',"Account Balance",self.balance[5])

        else:
            print("User not found")


if __name__ == '__main__':
    users = User(name=[], age=[], gender=[],accnumber=[])
    acc = Bank(name=[], age=[], gender=[],accnumber=[])

    while (True):


        print(f"Welcome to the HDFC Bank Enter your choice to continue")
        print("1. Show Acc Details")
        print("2. To Open Acc")
        print("3. To Deposit Bal")
        print("4. To Withdraw Bal")
        print("5. To View Bal")
        user_choice = input()

        if user_choice not in ['1','2','3','4','5']:
            print("Please inter a valid input given abobe:")
            continue

        else:
            user_choice = int(user_choice)



        if user_choice == 1:
            name=input("Enter your name")
            acc.showDetails(name)


        elif user_choice==2:
            name=input("Enter your name")
            age = input("Enter your age")
            gender = input("Enter your gender")
            acc.openacc(name,age,gender)



        elif user_choice == 3:
            name = input("Enter your name")
            amount = input("Enter the amount:")
            acc.deposit(amount,name)



        elif user_choice == 4:
            amount = input("Enter the amount:")
            name=input("Enter your name")
            acc.withdraw(amount,name)


        elif  user_choice == 5:
            name=input("Enter your name:")
            acc.viewbalance(name)





        else:
            print("Not a valid option")

        print("Press Q to quit and C to continue")
        user_choice2 = ""
        while (user_choice2 != "C" and user_choice2 != "Q"):
            user_choice2 = input()
            if user_choice2 == "Q":
                exit()

            elif user_choice2 == "C":
                continue
