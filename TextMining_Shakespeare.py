import string
import os
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
analyzer = SentimentIntensityAnalyzer()
import glob

import matplotlib.pyplot as plt
import numpy as np

def act_separate(file_name):
    """
    cuts each play into individual acts
    returns Shakespeare works categorized by act number
    """
    list_of_all_plays=[]
    act_one=[]
    act_two=[]
    act_three=[]
    act_four=[]
    act_five=[]

    for file_name in glob.glob('*.txt'):
        with open(file_name, "r") as f:
            play= f.read()
            play= play.lower().split("ACT")
        list_of_all_plays.append(play) #this works! it makes a huge list of all acts

    for play in list_of_all_plays:
        for act in play:
            if "act i" in act:
                act_one.append(act)
            if "act ii" in act:
                act_two.append(act)
            if "act iii" in act:
                act_three.append(act)
            if "act iv" in act:
                act_four.append(act)
            if "act v" in act:
                act_five.append(act) #this works! it groups only by act numbers
    return [act_one, act_two, act_three, act_four, act_five] #this works! it categorizes all works by act number
# print(act_separate("Hamlet.txt"))
savethebees = act_separate('*.txt')

def vadering_acts(savethebees):
    """
    sentiment analysis by act number
    """
    dict={}
    dalist=[]
    for i in savethebees:
        for s in i:
            dict = analyzer.polarity_scores(s)
            x = dict["compound"]
            dalist.append(x)
    print(dalist)
    return dalist #something for y value
vadering_acts(savethebees) #y=savethebees





#Note: I tried to do matplotlib for data visualization
#for my code, but the tinkering as seen below is not perfect.
#Thus I left the code as is, and just graphed data on
#Google spreadsheets because it's past my bedtime.

# plaid=vadering_acts(savethebees)
# x= [i for i in 50]
# y1=plaid[0:9]
# y2=plaid[10:19]
# y3=plaid[20:29]
# y4=plaid[30:39]
# y5=plaid[40:49]
# plt.scatter(x,y, marker="o")
#
# # pt.figure(figsize=(15,5)) #?????? what is this
# plt.plot(x,y1, color="blue", marker="o")
# plt.plot(x,y2, color="red", marker="o")
# plt.plot(x,y3, color="yellow", marker="o")
# plt.plot(x,y4, color="green", marker="o")
# plt.plot(x,y5, color="purple", marker="o")
# plt.title("Sentiment in Shakespeare Tragedies Over Time")
# plt.xlabel("Time in Play")
# ply.ylabel("Sentiment in Play")
# plt.show()
