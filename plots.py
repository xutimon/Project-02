
import json
paths = ['data/nobel.json']
with open('data/nobel.json','r') as json_file:
    tweets=json.load(json_file)
gender = {'male':0,'female':0}
print(list(gender.keys()))
for tweet in tweets["laureates"]:
    for key in list(gender.keys()):
        if key in tweet['gender']: 
            gender[key]+=1
print('gender=', gender)
lab_dict=list(gender)
terms = list(gender.keys())
counts = list(gender.values())
terms.sort()
accumulator=[]
for term in terms:
    accumulator.append(gender[term])
counts=accumulator
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.bar(terms, counts)
plt.xlabel("Gender of Nobel Laureates")
plt.ylabel("Number of Nobel Laureates")
plt.title("Figure 1: Gender Breakdown of all Nobel Laureates")
plt.show()



import matplotlib.pyplot as plt
import csv 
import pandas as pd
df = pd.read_csv('cereal.csv')
x = df["sugars"]
y = df["calories"]
z = df["rating"]
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
temp1 = df["calories"]
temp2=df["rating"]
green=ax1.scatter(x, y, s=temp1, color='g')
red=ax2.scatter(x, z,s=temp2, color='r')
ax1.set_xlabel('Grams of Sugar per Serving')
ax1.set_ylabel('Calories per Serving')
ax2.set_ylabel('Consumer Rating')
plt.legend((green, red),
           ('Calories per Serving', 'Consumer Rating'),
           scatterpoints=1,
           loc='lower left',
           ncol=2,
           fontsize=8)
plt.title("Figure 2: Relationship Between Different Key Metrics Among Major Cereal Brands")
plt.show()
