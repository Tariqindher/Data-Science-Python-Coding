print("Python", end="@") #it means no new line
print("Programming")
print('G','F','G', sep='') #it means no space between GFG

#forloop and wjhile loop and range function
for i in range(5):
    print(i, end=' ')

print()
i=0
while(i<5):
    print(i, end=' ')
    i+=1
print()
#loop with else
for i in range(5):
    print(i, end=' ')
else:
    print("\nFinally i is :",i)

#break statement
for i in range(5):
    if(i==3):
        break
    print(i, end=' ')
print()
#continue statement
for i in range(5):
    if(i==3):
        continue
    print(i, end=' ')                   
print()
#pass statement it is used when a statement is required syntactically but you do not want any command or code to execute
for i in range(5):
    pass
print("HellO")



print('a' is 'a')
print('a' is not 'b')
a=["aa","bb","cc"]
b=["Foo","Zoo","d"]
c=["aa","bb","cc"]

a==c
print(a==c)
print(a is c)
print (a is not b)
print(a in c)

a="Hello, World!"
print(a[1:5])
print(a[:5])
print(a[2:])
print(a[-5:-2])
print(a[-5:])

a=330
b=330

print("A") if a > b else print("B") if a<b else print("=")
print("A") if a > b else print("=") if a==b else print("B")

if not a > b:
    print("A is not greater than B")





