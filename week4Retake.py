 #problem 1
nameInput=input("Enter your name: ")
ageInput=input("Enter your age: ")
print(f"{nameInput} is {ageInput} years old!")

#Problem 2
user_age_Input=int(input("Enter your age: "))
if user_age_Input>=0 and user_age_Input<=125:
    print("Real Age")
else:
    print("Not a real age")

 #Problem 3
for x in range(-50,50-1,4):
    print(x)

# #Problem 4 #not getting running total

numberInput=int(input("Enter a number: "))
total=20
while numberInput!=0:
    total=total+numberInput
    numberInput=int(input("Enter a number: "))
    print(total)
numberInput=int(input("Enter a number: "))


# #Problem 5
names=["Jordon","Jalen","Janiya","Gail"]
print(f"{names[0]}, {names[1]}, {names[2]},{names[3]}")

# #Problem 6
def numberFunc(num1,num2,num3):
        sum=num1+num2
        print(sum)
        sum2=num2*num3
        return sum2
print(numberFunc(2,4,6))
#
# #Problem 7
class Boardgame:
    def __init__(self,name,price,pricecount,publisher):
        self.name=name
        self.price=price
        self.pricecount=pricecount
        self.publisher=publisher
    def priceChange(self):
        newPrice=int(input("Enter a new Price: "))
        self.price=newPrice
    def __str__(self):
        return f"{self.name},{self.price},{self.pricecount},{self.publisher}"

game1= Boardgame("Life",6.99,2,"hasboro")
game2= Boardgame("Chess",8.99,5,"old school")
game3= Boardgame("Scrabble",10,7,"hasboro")
gamelist=[game1,game2,game3]

for g in range(0,len(gamelist)):
    print(gamelist[g])

#Problem 8:
def arrayFunction():
    array1=["A","B","C"] #not getting s to append
    for a in range(0,len(array1)):
        print(array1[a] + ("s"))


print(arrayFunction())

#Problem 9
def newFunc(anArray): #positive numbers not printing
    for q in range(0,len(anArray)):
      if q>0:
          return(anArray[q])

anArray=[-2,4,0,-9,8,10]
print(newFunc(anArray))

# #Problem 10
class Puppy:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def __str__(self):
        return f"{self.name},{self.color}"

puppylist=[]
puppyEntry=input("Enter name of puppy: ")
while puppyEntry !="q":
    puppyEntry=input("Enter name of puppy: ")
    puppyColor=input("Enter color of puppy:")
    puppylist.append(puppyEntry)
    puppylist.append(puppyColor)
    puppyEntry=input("Enter name of puppy: ")
    print(puppylist)
