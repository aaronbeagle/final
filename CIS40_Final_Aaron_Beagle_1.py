#CIS40 - Final program - Aaron Beagle
## Class program to order burgers from DeAnza burger joint.

import time
import datetime
class Order:
    Tax = 0.09
    def __init__(self):
        '''
        This is the initialization method.
        '''
        self._priceBtax = 0
        self._priceAtax = 0
        self._priceDict = {"De Anza Burger" : 5.25 , "Bacon Cheese" : 5.75, "Mushroom Swiss" : 5.95, "Western Burger" : 5.95, "Don Cali Burger" : 5.95}
        self._orderDict = {"De Anza Burger" : 0, "Bacon Cheese" : 0,"Mushroom Swiss" : 0, "Western Burger" : 0, "Don Cali Burger" : 0}

    def displayMenu(self):
        '''
        This function displays the menu at the DeAnza burger joint.
        '''
        print("\n-- De Anza Burger Joint --")
        number = 1
        for key in self._priceDict:
            print("{a}.{b:15s}{c:8.2f}".format(a= number, b= key, c=self._priceDict[key]))
            number +=1
            print("6. Exit")
    
    def getInputs(self):
        '''
        This method asks the customer to input their selection of burgers and quantity desired.
        '''
        count=0
        burgerOrder = int(input("Please enter the burger number you want(1 to 5 or 6 to complete order): "))
        burgetrQuantity = int(input("Enter the quantity:"))
        flag1 = True
        while flag1:
            flag2=True
            while flag2:
                try:
                    burgerOrder = int(input("Please enter the burger number you want(1 to 5 or 6 to complete order): "))
                    if burgerOrder <=0:
                        print ("Please choose between 1 and 6!")
                    elif burgerOrder >=7:
                        print ("Please choose between 1 and 6!")
                    else:
                        flag2=False
                except:
                    print("Please enter a number between 1 and 6!")
        flag3=True
        while flag3 and burgerOrder !=6:
            try:
                burgerQuantity = int(input("Please enter how many burgers you'd like: "))
                count +=1
                flag3=False
            except:
                print("Please enter a positive quantity for your burger selection!")
        if burgerOrder == 1:
            self._orderddict ["De Anza Burger"] = burgerQuantity
        elif order == 2:
            self._orderdict ["Bacon Cheese"] = burgerQuantity
        elif order == 3:
            self._orderdict ["Mushroom Swiss"] = burgerQuantity
        elif order == 4:
            self._orderdict ["Western Burger"] = burgerQuantity
        elif order == 5:
            self._orderdict ["Don Cali Burger"] = burgerQuantity
        elif order == 6:
            flag1=False

        flag4=True
        while flag4 and count !=0:
            try:
                tax = input("Please enter 1 for student or 2 for staff.")
                flag4=False 
            except:
                print("Please confirm if you are student or a staff member!")

    def calculate(self):

        '''
        The doc string for this method calculates the bill.
        '''

        for key in self.priceDict:
            self._priceBtax += self._orderDict[key] * self._priceDict[key]
            self._priceAtax = self._priceBtax + (self._priceBtax * self._tax)


    def printBill(self):

        '''

        The doc string for this method displays the bill

        '''


        print("\nYour bill:")

        print("Your bill:")
        for key in self._orderDict:
            print("%-20s Qty: %-10d Price: $%-10.2f Total: $%-10.2f"%(key,self._orderDict[key],self._priceDict[key], \ (self._orderDict[key]*self._priceDict[key])))          
        print("-"*50)
        print("Price before tax:", self.priceBtax)
        print("Price after tax:", self.priceAtax)

    def saveToFile(self):
        timeStamp = time.time()
        orderTimeStamp = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H-%M-%S')

        orderTimeStamp = orderTimeStamp + '.txt'

        fileHandleToSaveTheBill = open(orderTimeStamp, 'w')

        fileHnadleToSaveTheBill.write("Your bill:")
        for key in self._orderDict:
            if self._orderDict[key] !=0:
                #print(key, "\t\tQty:" , self.orderDict[key], "t\Price:", self._priceDict[key], "\tTotal:", self.OrderD
                fileHandleToSaveTheBill.write("\n %-20s Qty: %-10d Price: $%-10.2f" \
                    %(key, self._orderDict[key],self._priceDict[key], (self._orderDict[key]*self._priceDict[key])))
        fileHandleToSaveTheBill.write("\n" + "-"*70)
        fileHandleToSaveTheBill.write("\nPrice before tax:" + str(round(self.priceBtax,2)))
        fileHandleToSaveTheBill.write("\nTax:" + str(self.tax))
        fileHandleToSaveTheBill.write("\nPrice after tax:" + str(round(self.priceAtax,2)))
                


















                


































