import matplotlib.pyplot as plt

x = [1,2,3,4,5]   # x-axis values
y = [2,4,8,10]  # y-axis values

plt.plot(x, y) # make a line graph
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("My First Graph")
plt.show()
plt.bar(x,y)
plt.show(x,y)