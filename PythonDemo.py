#Variables
my_string = "Hello, World!"
x=10
a=b=c=10
print(a,b,c)
print(my_string)
print(x)
x,y,z=1,2.5,"Tariq"
print(x,y,z)

#Data Types
print(type(my_string))
print(type(x))
print(type(y))
print(type(z))      
print(type(a))

#Casting
x="10"
x=int(x)
cnt=5
f=float(cnt)
print(type(x))
print(type(f))
age=20
s2=str(age)
print(type(s2))

#String Methods
a= " Hello, World! "
print(a.strip())
print(a.lower())
print(a.upper())
print(a.replace("H","J"))
print(a.split(","))
print("Hello" in a)
print("Hello" not in a)
print(a[2:5])

#String Concatenation
a="Hello"
b="World"
c=a+" "+b
print(c)
age=36
txt="My name is Tariq, and I am {}".format(age)
print(txt)

#getting the type
x=5
print(type(x))
y=3.14
print(type(y))
z="Hello"
print(type(z))
a=1j
print(type(a))
b=True
print(type(b))
c=["apple","banana","cherry"]
print(type(c))
d=("apple","banana","cherry")
print(type(d))
e=range(6)
print(type(e))
f={"name":"Tariq","age":36}
print(type(f))
g={"apple","banana","cherry"}
print(type(g))
h=frozenset({"apple","banana","cherry"})
print(type(h))
i=bytes(5)
print(type(i))
j=bytearray(5)
print(type(j))
k=memoryview(bytes(5))
print(type(k))


# #input and output
# print("Enter your name:")
# name=input()
# print("Hello, " + name + "!")

# #take Multiple inputs
# x,y=input("Enter two values: ").split()
# print("x:",x)       
# print("y:",y)

# x,y,z=input("Enter three values: ").split(',')
# print("x:",x,"y:",y,"z:",z)
# price=float(input("Enter price: "))
# print("Price is:",price)

#Output Formatting
quantity=3
print(quantity) 
print("I have",quantity,"apples.")
print("I have {} apples.".format(quantity))
print(f"I have {quantity} apples.")     
print("I have %d apples." % quantity)
price=49
item="apple"
print("I have %d %s for $%.2f." % (quantity,item,price))        


#Output Formatting
amount=10.75
print("Amount: ${:.2f}".format(amount))
print(f"Amount: ${amount:.2f}")