import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from itertools import chain
from collections import Counter
import re
from statistics import mean, median
black = ("\u001b[30;1m")
red = ("\u001b[31;1m")
green = ("\u001b[32;1m")
yellow = ("\u001b[33;1m")
blue = ("\u001b[34;1m")
magenta = ("\u001b[35;1m")
cyan = ("\u001b[36;1m")
white = ("\u001b[37;1m")
emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
def listToString(s): 
    str1 = "" 
    for ele in s: 
        str1 += ele  
    return str1    

def stringToList(string):
    li = list(string.split(" "))
    return li
   

print(yellow,"\n", "Find out the frequency of each channel title and create a bar graph organized from highest frequency to lowest frequency",white)

f = pd.read_csv('trending.csv')
f.dropna(inplace = True)
frequency = f['channel_title'].value_counts()
frequency = pd.DataFrame(frequency)
print(frequency)
frequencyDict = frequency.to_dict()
emptyDict = {}
frequencyDict = frequencyDict["channel_title"]
dictionary_length = len(frequencyDict)
fillerList = []
print(yellow,"Find out the frequency of each category id and create a bar graph organized from highest frequency to lowest frequency",white)
for i in range (dictionary_length):
    fillerList.append(" ")
data_dict = frequencyDict
courses = list(data_dict.keys())
values = list(data_dict.values())
filler = (fillerList)
fig = plt.figure(figsize = (10, 5))
plt.bar(courses, values, color ='blue',
        width = 0.5)
plt.xlabel("Channel Titles")
plt.ylabel("Frequency")
plt.title("Frequency of Different Channel Titles From Highest to Lowest")
#plt.savefig('Frequency.png', bbox_inches='tight')
#plt.show()
plt.close()

print(yellow,"\n","Find out the top 10 most common tags amongst these videos",white)
tags = pd.read_csv("trending.csv", usecols = ['tags'])
tags = tags.dropna()
tags = tags.values.tolist()
tags = list(chain.from_iterable(tags))
tags = "".join(tags)
tags = re.sub('"',  '',   tags)  
tags = tags.replace(" ", "")
tags = tags.replace("|"," ")
split_it = tags.split()
tags = Counter(split_it)
most_occur = tags.most_common(10)
print(most_occur)

print(yellow,"\n","Create a csv data frame that takes the individual category id and analyze the maximum, minimum, mean, median values",white)
allCategories = []
for i in f["category_id"]: 
    if i not in allCategories:
        allCategories.append(i)
MaxViews,MinViews,MeanViews,MedianViews = [],[],[],[]
MaxLikes,MinLikes,MeanLikes,MedianLikes = [],[],[],[]
MaxDLikes,MinDLikes,MeanDLikes,MedianDLikes = [],[],[],[]
Maxcom,Mincom,Meancom,Mediancom = [],[],[],[]
for i in allCategories:
    cats = f.loc[f["category_id"] == i]
    Views = [i for i in cats["views"]]
    Likes = [i for i in cats["likes"]]
    Dislikes = [i for i in cats["dislikes"]]
    Comments = [i for i in cats["comment_count"]]
    MaxViews.append(max(Views)), MinViews.append(min(Views)), MeanViews.append(mean(Views)), MedianViews.append(median(Views))
    MaxLikes.append(max(Likes)), MinLikes.append(min(Likes)), MeanLikes.append(mean(Likes)), MedianLikes.append(median(Likes))
    MaxDLikes.append(max(Dislikes)), MinDLikes.append(min(Dislikes)), MeanDLikes.append(mean(Dislikes)), MedianDLikes.append(median(Dislikes))
    Maxcom.append(max(Comments)), Mincom.append(min(Comments)), Meancom.append(mean(Comments)), Mediancom.append(median(Comments))
allCategories.append("Average")
MaxViews.append(mean(MaxViews)),MinViews.append(mean(MinViews)),MeanViews.append(mean(MeanViews)),MedianViews.append(mean(MedianViews))
MaxLikes.append(mean(MaxLikes)),MinLikes.append(mean(MinLikes)),MeanLikes.append(mean(MeanLikes)),MedianLikes.append(mean(MedianLikes))
MaxDLikes.append(mean(MaxDLikes)),MinDLikes.append(mean(MinDLikes)),MeanDLikes.append(mean(MeanDLikes)),MedianDLikes.append(mean(MedianDLikes))
Maxcom.append(mean(Maxcom)),Mincom.append(mean(Mincom)),Meancom.append(mean(Meancom)),Mediancom.append(mean(Mediancom))
d1 = pd.Series(allCategories)
d2 = pd.Series(MaxViews) 
d3 = pd.Series(MinViews)
d4 = pd.Series(MeanViews)
d5 = pd.Series(MedianViews)
d6 = pd.Series(MaxLikes)
d7 = pd.Series(MinLikes)
d8 = pd.Series(MeanLikes)
d9 = pd.Series(MedianLikes)
d10 = pd.Series(Maxcom)
d11 = pd.Series(Mincom)
d12 = pd.Series(Meancom)
d13 = pd.Series(Mediancom)
d14 = pd.Series(MaxDLikes)
d15 = pd.Series(MinDLikes)
d16 = pd.Series(MeanDLikes)
d17 = pd.Series(MedianDLikes)

datanew = pd.DataFrame(d1)
dfnew = pd.DataFrame([d1, d2 ,d3 ,d4 ,d5 ,d6 ,d7 ,d8 ,d9 ,d10,d11,d2,d13, d14, d15, d16, d17], index = allCategories)
dfnew.sort_index(key=lambda x: x.str.lower())
dic = {0: 'Max Views', 
       1: 'Min Views',
       2: 'Mean Views',
       3: 'Median Views',
       4: 'Max Likes',
       5: 'Min likes',
       6: 'Mean likes',
       7: 'Median likes',
       8: 'Max com',
       9: 'Min com',
       10: 'Mean com',
       11: 'Median com',
       12: 'Max dlikes',
       13: 'Min dlikes',
       14: 'Mean dlikes',
       15: 'Median dlikes',
       16: ' ',
       }
dfnew.rename(columns = dic, inplace=True)
print(dfnew)
'''
catID = pd.read_csv("trending.csv", usecols = ['category_id'])
views = pd.read_csv("trending.csv", usecols = ['views'])
likes = pd.read_csv("trending.csv", usecols = ['likes'])
dislikes = pd.read_csv("trending.csv" , usecols = ['dislikes'])
comments = pd.read_csv("trending.csv" , usecols = ['comment_count'])
frames = [catID, views, likes, dislikes, comments]
result = pd.concat(frames, axis=1, join='inner')
sortedDataFrame = result.sort_values(by="category_id",ascending=True)
print(sortedDataFrame)
sorted_index = sortedDataFrame.reset_index(drop=True)
print(sorted_index)
'''
print(yellow,"\n","Go through every titles and descriptions and compile all the words used and print out the top 30 words",white)
title = pd.read_csv("trending.csv", usecols = ['title'])
title = title.dropna()
title = title.values.tolist()
title = list(chain.from_iterable(title))
title = "".join(title)

description = pd.read_csv("trending.csv", usecols = ['description'])
description = description.dropna()
description = description.values.tolist()
description = list(chain.from_iterable(description))
description = "".join(description)

title = title + description
title = title.lower()
title = re.sub(' \n' , ' ', title)
title = re.sub('\n' , ' ', title)
title = re.sub(r'[^a-zA-Z]', ' ', title)
title = re.sub(' the ', ' ', title)
title = re.sub(' a ', ' ', title)
title = re.sub(' he ', ' ', title)
title = re.sub(' she ', ' ', title)
title = re.sub(' n ', ' ', title)
title = re.sub(' of ', ' ', title)
title = re.sub(' https ', ' ', title)
title = re.sub(' in ', ' ', title)
title = re.sub(' www ', ' ', title)
title = re.sub(' and ', ' ', title)
title = re.sub(' http ', ' ', title)
title = re.sub(' s ', ' ', title)
title = re.sub(' i ', ' ', title)
title = re.sub(' to ', ' ', title)
title = re.sub(' nhttps ', ' ', title)
title = re.sub(' t ', ' ', title)
title = re.sub(' T ', ' ', title)
title = re.sub(' with ', ' ', title)
title = re.sub(' With ', ' ', title)
title = re.sub(' on ', ' ', title)
title = re.sub(' On ', ' ', title)
title = re.sub(' - ', ' ', title)
title = re.sub(' for ', ' ', title)
title = re.sub(' you ', ' ', title)
title = re.sub(' by ', ' ', title)
title = re.sub(' is ', ' ', title)
title = re.sub(' _ ', ' ', title)
title = re.sub(' at ', ' ', title)
title = re.sub(' | ', ' ', title)
title = re.sub(' from ', ' ', title)
title = re.sub(' & ', ' ', title)
title = re.sub(' this ', ' ', title)
title = re.sub(' that ', ' ', title)
title = re.sub(' it ', ' ', title)
title = re.sub(' my ', ' ', title)
title = re.sub(' your ', ' ', title)
title = re.sub(' are ', ' ', title)
title = re.sub(' out ', ' ', title)
title = re.sub(' as ', ' ', title)
title = re.sub(' me ', ' ', title)
title = re.sub(' we ', ' ', title)
title = re.sub(' our ', ' ', title)
title = re.sub(' all ', ' ', title)
title = re.sub(' an ', ' ', title)
title = re.sub(' com ', ' ', title)
title = re.sub(' new ', ' ', title)
title = re.sub(' i ', ' ', title)
title = re.sub(' v ', ' ', title)
title = re.sub(' ly ', ' ', title)
title = re.sub(' be ', ' ', title)
title = re.sub(' gl ', ' ', title)
title = re.sub(' smarturl ', ' ', title)
title = re.sub(' i ', ' ', title)
title = re.sub(' nhttp ', ' ', title)
title = re.sub(' c ', ' ', title)
title = re.sub(' n ', ' ', title)
title = re.sub(' can ', ' ', title)
title = re.sub(' m ', ' ', title)
title = re.sub(' can ', ' ', title)
title = re.sub(' get ', ' ', title)
title = re.sub(' or ', ' ', title)
title = re.sub(' nfacebook ', ' ', title)
title = re.sub(' here ', ' ', title)
title = re.sub(' nsubscribe ', ' ', title)
title = re.sub(' nfollow ', ' ', title)
title = re.sub(' ntwitter ', ' ', title)
title = re.sub(' so ', ' ', title)
title = re.sub(' how ', ' ', title)
title = re.sub(' his ', ' ', title)
title = re.sub(' up ', ' ', title)
title = re.sub(' more ', ' ', title)
title = re.sub(' ninstagram ', ' ', title)
title = re.sub(' his ', ' ', title)
title = re.sub(' was ', ' ', title)
title = re.sub(' have ', ' ', title)
title = re.sub(' now ', ' ', title)
title = re.sub(' us ', ' ', title)
title = re.sub(' not ', ' ', title)
title = re.sub(' but ', ' ', title)
title = re.sub(' if ', ' ', title)
title = " ".join(title.split())
split_it = title.split()
title = Counter(split_it)
most_occur = title.most_common(30)
print(most_occur)


df2 = pd.read_csv("test.csv")
counts3 = pd.read_csv("test.csv", usecols = ['likes' ])

counts4 = pd.read_csv("test.csv", usecols = ['dislikes' ])

counts5 = pd.read_csv("test.csv", usecols = ['views' ])

counts6 = pd.read_csv("test.csv", usecols = ['comment_count' ])

fnew = pd.concat([counts3, counts4], axis = 1)
#like to dislike ratio
likeratio = fnew["likes"]/fnew["dislikes"]
likeratio = pd.DataFrame(likeratio)

#views to comments ratio
fother = pd.concat([counts5, counts6], axis = 1)
engagementratio = fother["views"]/fother["comment_count"]
engagementratio = pd.DataFrame(engagementratio)


res = likeratio
res.columns =['trending']
res[res < 50] = "true"
res[res != "true"] = "false"
fnew = pd.concat([df2,res], axis = 1)
fnew.to_csv('new.csv')

x = print(fnew.shape[0])


y =res['trending'].value_counts()

percenttrending = (28198/40881) * 100
print(yellow,"Calculate the percentage of the videos in the test.csv that will be listed on the trending page and output the result in the terminal",white)

print ("The percentage of trending videos is", percenttrending)