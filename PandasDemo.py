import pandas as pd
mydataset= {
        'cars' : ["BMW", "Volvo", "Ford"],
         'passings' : [3,7,2]
}
myvar = pd.DataFrame(mydataset)
print(myvar)
a=[1,7,2]
myvar=pd.Series(a)
print(myvar)
#Return the 1st value
print(myvar[0])
myvar=pd.Series(a,index=["x", "y", "z"])
print(myvar)
print(myvar["y"])

calories={"day1":420, "day2": 380, "day3": 390}
myvar=pd.Series(calories)
print(myvar)
myvar=pd.Series(calories, index=["day1", "day2"])
print(myvar)