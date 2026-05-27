#Benjamin Flores
#Influencer Stories

import pandas as pd

data = pd.read_csv("dev.csv")

level = data["Level"].tolist()
time = data["Time"].tolist()
rating = data["Rating"].tolist()
summary = data["Summary"].tolist()
feedback = data["Feedback"].tolist()
filter = []

def abnormal(ti, rate):
    for i in range(len(rating)):
        if time[i] > ti and rating[i] > rate:
            filter.append([i])
    print(filter)
    filter.clear()
abnormal(100,4.5)
print(data.loc[[79]])



def secret(word):
    for i in range(len(rating)):
        if word in feedback[i]:
            filter.append([i])
    print(filter)
    filter.clear()
secret("secret")
print(data.loc[[66]])

def problems(rate):
    for i in range(len(rating)):
        if rating[i] < rate:
            filter.append([i])
    print(filter)
    filter.clear()

problems(2)
print(data.loc[[14,33,77]])
