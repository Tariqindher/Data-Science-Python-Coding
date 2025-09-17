#Conditions if else, nested if , else if, 
x=3
if x>5:
   print("x is greater than 5")
else:
      print("X is not greater than 5")

#if  .... elif..... else
marks=1000
if marks>=87 and marks<=100:
   print("Grade A")
elif marks>=77 and marks<=87:
   print("Garde B")
elif marks>=67 and marks<=77:
    print("Garde C")
else:
    print("FAIL")

#Nested IF
age=20
citizen=True
if age>18:
    if citizen:
        print("You can Vote")
    else:
        print("You must be Citizen")
else:
      print("You are too young ")


x=13
if x>10:
    print("Above 10")
    if x>20:
       print("and also above 20")
    else:
        print("but not above 20")
else: 
     print("X is less than or equal 10")


#Loops use break with if
for i in range(1,6):
     if i==3:
      	break
     print(i)

print("Continue Use")
#Continue in loop
for i in range(1,6):
      if i==3:
                continue
      print(i)

x=10
if x>5:
   pass
else: 
     print("X is not greater than 5")

#Loops
for i in range(1,6):
      print(i, end=" ")
print()
#loops with custom start and stop and step
for i in range(2, 11,2):
     print(i, end=" ")
print()
#Looping through a lists
fruits=["apple", "Banana", "mango"]
for frt in fruits:
            print(frt)

x=1
while x<=5:
   print(x, end=" ")
   x=x+1

