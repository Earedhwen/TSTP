import os
import csv

###Challenge 1
##
##mypath = os.path.join("C:\\","Users","Hannah","Documents","Stuff","songs.txt")
##
##with open(mypath,"r") as f:
##    print(f.read())
##
###Challenge 2
##
##answer = input("What is your favourite colour? ")
##
##with open('colour.txt','w') as f:
##    f.write(answer)

#Challenge 3

listoflists = [['Top Gun','Risky Business','Minority Report'],\
               ['Titanic','The Revenant','Inception'],\
               ['Training Day','Man on Fire','Flight']]

with open('challenge.csv','w',newline = '') as f:
    w = csv.writer(f, delimiter = ',')
    for i in range(len(listoflists)):
        w.writerow(listoflists[i])
