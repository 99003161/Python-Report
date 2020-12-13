d = []


class Customer:
    def __init__(self, cust_id, cust_name, cust_num, cust_init):
        self.cust_id = cust_id
        self.cust_name = cust_name
        self.cust_num = cust_num
        self.cust_init = cust_init

    def payment(self, upd_amt, n):
        if(n == 1):
            self.cust_init = self.cust_init - upd_amt
        elif(n == 2):
            upd_amt = int(input("Enter the amount"))
            self.cust_init = self.cust_init + upd_amt

    def edit_customer(self, n):
        if(n == 1):
            upd_name = input("Enter the new name")
            self.cust_name = upd_name
        elif(n == 2):
            upd_num = input("Enter the new number")
            self.cust_num = upd_num


class loyal_Customer(Customer):
    def __init__(self, cust_id, cust_name, cust_num, cust_init, bonus):
        Customer.__init__(self, cust_id, cust_name, cust_num, cust_init)
        self.cust_init = self.cust_init - bonus


class late_Customer(Customer):
    def __init__(self, cust_id, cust_name, cust_num, cust_init, penalty):
        Customer.__init__(self, cust_id, cust_name, cust_num, cust_init)
        self.cust_init = self.cust_init + penalty


print(" Deepak's Grocery Stores Customer Accounting System")
print("1.Add a customer")
print("2.Payment by Customer")
print("3.Edit customer details")
print("4.View all customers")

while(1):
    f = open(r"C:\Users\TRAINING\Desktop\input.txt", 'w+')
    n = int(input())
    if(n == 1):
        l = int(input("1. Regular\n2. Loyal\n3.Late\n"))
        cust_id = input("enter the id number")
        cust_name = input("enter the customer name")
        cust_num = input("enter the customer number")
        cust_init = int(input("enter the initial amount"))
        if(l == 1):
            c = Customer(cust_id, cust_name, cust_num, cust_init)

        elif(l == 2):
            c = loyal_Customer(cust_id, cust_name, cust_num, cust_init, 500)

        else:
            c = late_Customer(cust_id, cust_name, cust_num, cust_init, 500)
        d.append(c)
    elif(n == 2):
        ci = input("enter the id number of the customer")
        t = 0
        for i in d:
            if(i.cust_id == ci):
                t = t + 1
                x = int(input("1.Consumer pay\n2.Consumer Credit"))
                upd_amt = int(input("Enter the amount"))
                i.payment(upd_amt, x)
        if(t == 0):
            print("No customers found")

    elif(n == 3):
        ci = input("enter the id number of the customer")
        t = 0
        for i in d:
            if(i.cust_id == ci):
                t = t + 1
                x = int(input("1.Change Name\n2.Change Number"))
                i.edit_customer(x)
        if(t == 0):
            print("No customers found")
    elif(n == 4):
        z = 0
        for i in d:
            z = z + 1
            print("Customer Id: " + i.cust_id)
            print("Customer Name: " + i.cust_name)
            print("Customer Number: " + i.cust_num)
            print("Amount to be paid: " + str(i.cust_init))
            print("\n")
        if(z == 0):
            print("No customers found")
    else:
        print("Enter a valid input")
        continue
    for i in d:
        f.writelines("Customer Id: " + i.cust_id)
        f.writelines("\n")
        f.writelines("Customer Name: " + i.cust_name)
        f.writelines("\n")
        f.writelines("Customer Number: " + i.cust_num)
        f.writelines("\n")
        f.writelines("Amount to be paid: " + str(i.cust_init))
        f.writelines("\n\n")
    f.close()
    t = input("Do you wish to continue ? (Y / N)")
    if(t == "N"):
        print(" Deepak's Grocery Stores Customer Accounting System")
        break
    elif(t == "Y"):
        print("1.Add a customer")
        print("2.Payment by Customer")
        print("3.Edit customer details\n4.View all customers")
        continue
