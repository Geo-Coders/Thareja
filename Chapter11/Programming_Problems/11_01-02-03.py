# Write a class Money with attributes Rupees and Paise. Overload operators  +=  ,  -= , and  >=  
# so that they may be used on two objects. Also write functions so that a desired amount 
# of money can be either added or subtracted from Money.

print('--- This is a Money Program for No 1 - 3 ---')
print()

class Money:
    def __init__(self,R,P):
        self.rupee = R
        self.paise = P

    def __iadd__(self,B):
        self.rupee +=  B.rupee
        self.paise +=  B.paise
        Money.simplify(self)
        return self
       
    def __mul__(self,num):
        Temp = Money(0,0)
        Temp.rupee = self.rupee*num
        Temp.paise = self.paise*num
        Temp.simplify()
        return Temp
    
    def convert(self):
        self.simplify()
        self.simplify()
        total = self.rupee + (self.paise/100)
        total = round(total,2)
        usd = total/71.14
        usd = round(usd,2)
        return usd
     
    def items(self,unit):
        self.simplify()
        total = self.rupee+(self.paise/100)
        total = round(total,2)
        item_price = total/unit
        item_price = round(item_price,2)
        return item_price

    def __isub__(self,B):
        self.rupee -= B.rupee
        self.paise -= B.paise
        while self.paise<0:
            self.rupee -= 1
            self.paise +=  100
        Money.simplify(self)
        return self

    def simplify(self):
        if self.paise >= 100:
            self.rupee = self.rupee+int(self.paise/100)
            self.paise = int(self.paise%100)
            
    def __ge__(self,B):
        Money.simplify(self)
        Money.simplify(B)
        Flag = False
        if self.rupee >= B.rupee:
            if self.paise >= B.paise:
                Flag = True
        return Flag
    
    def display(self):
        print(self.rupee,"Rupees",self.paise,"paise")

M1 = Money(56,544)
M2 = Money(25,256)
M1 +=  M2
M1.display()
M1 -= M2
M1.display()
print("M1 >= M2: ",M1 >= M2)
M3 = Money(0,0)
M3 = M2*2
M3.display()

Total = Money(0,0)
Total.rupee = int(input("Enter the total rupee: "))
Total.paise = int(input("Enter the total paise: "))
unit = int(input("Enter the units of item bought: "))
print("Price of each item:",Total.items(unit))

indian = Money(0,0)
indian.rupee = int(input("Enter the rupee: "))
indian.paise = int(input("Enter the paise:"))
usd = indian.convert()

print("DOLLARS: ",int((usd*100)/100))
print("CENTS : ",(usd*100)%100)