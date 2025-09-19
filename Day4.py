fruits=["apple", "banana", "Cherry"]
for x in fruits:
   print(x, end=" ")
   if x=="banana":
            break

print()
for x in range(6):
     print(x, end=" ")
print()
for x in range(2,6):
     print(x, end=" ")

print()
for x in range(2,10,2):
     print(x, end=" ")

print()
for x in range(6):
     print(x, end=" ")
else:
        print("Finally Finished")

#after break the else will not run
for x in range(6):
     print(x, end=" ")
     if x==3:
        break
else:
        print("Finally Finished")


#Pass : Do Nothing
for x in range(6):
     pass
else: 
        print(x)

#Nested Loop
for i in range(5): #OuterLoop
     for j in range(5):  #InnerLoop
             print((i, j), end=" ")
     print()


for i in range(1,5): #OuterLoop
     for j in range(1,5):  #InnerLoop
             print((i*j), end=" ")
     print()



