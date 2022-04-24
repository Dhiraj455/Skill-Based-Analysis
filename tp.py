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
# import numpy as np
# import pandas as pd
# import csv
# import matplotlib.pyplot as plt

# df = pd.read_csv('./Data/UserData/user0.csv',usecols=["Skill","Score"])
# print(df["Skill"])
# l = len(df["Skill"])
# print(l)
# sum = 0
# skill = []
# score = []
# for i in range(0,l):
#     if skill.__contains__(df.iloc[i]["Skill"]):
#             continue
#     else:
#         print(skill)
#         skill.append(df.iloc[i]["Skill"])
# print(skill)
# for i in skill:
#     for j in range(0,l):
#         if i == df.iloc[j]["Skill"]:
#             sum += df.iloc[j]["Score"]
#     score.append(sum)
#     sum = 0
# print(score)
# df1 = pd.DataFrame({"Skill":skill,"Score":score})
# print(df1)
# x = np.array(df1["Skill"])
# y = np.array(df1["Score"])
# plt.pie(y, labels = x)
# plt.show()

# print(df)
# print(len(df))
# plt.plot(df.Skill, df.Score)
# plt.show()
# print(type(df))
# x = str(df)
# print(x)
# print(type(x))

# df = pd.read_csv('./Data/Questions/quiz1.csv')
# print(df)
# print(df.iloc[5])
# x = len(df)
# for i in range(0,x):
#     print(df.iloc[i]["question"])
#     print(df.iloc[i]["option1"])
#     print(df.iloc[i]["option2"])
#     print(df.iloc[i]["option3"])
#     print(df.iloc[i]["option4"])
#     print(df.iloc[i]["answer"])
# skill = ["Python","C++","Java"]
# score = [20,13,45]
# res = dict(zip(skill, score))
# print(res)
# print(max(res.values()))

x = "Hello\nWorld"                                                                                                                                                                                                                  
print(x)