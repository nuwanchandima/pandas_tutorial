import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
myvar = pd.DataFrame(mydataset)
print(myvar)
#     cars  passings
# 0    BMW         3
# 1  Volvo         7
# 2   Ford         2

print(pd.__version__)
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)
# 0    1
# 1    7
# 2    2

print(myvar[0])
# 1

a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)
# x    1
# y    7
# z    2
print(myvar["y"])
# 7

