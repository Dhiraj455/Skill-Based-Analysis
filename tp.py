# import json
# import matplotlib.pyplot as plt
# import numpy as np

# y = np.array([35, 25, 25, 15])
# mylabels = ["App Development", "Game Development", "Web Development", "Graphic Designer"]

# plt.pie(y, labels = mylabels)
# plt.show() 

# f = open('user.json','r')
# x = json.load(f)
# dict = {
#     1:2,
#     2:3,
#     3:4
# }
# print(dict.__contains__(1))
# print(x.__contains__('Userinfo'))
# print(x)

# update Csv file
from sys import _xoptions
import pandas as pd
import csv
import matplotlib.pyplot as plt

df = pd.read_csv('./Data/UserData/user0.csv',usecols=["Skill","Score"])
print(df)
print(len(df))
plt.plot(df.Skill, df.Score)
plt.show()
print(type(df))
x = str(df)
print(x)
print(type(x))