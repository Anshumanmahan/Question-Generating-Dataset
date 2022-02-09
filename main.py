import sys
import os
import pandas as pd
from cleaning import clean
from keywords import key
from dataprep import convert
from sher import sher
from sql import sqlquery
from questions import ques
import random

filename = sys.argv[1]
datad = sys.argv[2]
cold = sys.argv[3]
filepath, file_extension = os.path.splitext(filename)

#Check the file extension for processing
if(file_extension == ".csv"):
    df = pd.read_csv(filename)
elif(file_extension == ".xlxs"):
    df = pd.read_excel(filepath)
elif(file_extension == ".xls"):
    df = pd.read_excel(filepath)
else:
    print("Wrong file type")



cleandf = clean(df)
keyw = key(datad)
if len(keyw) < 3:
    entity = keyw
else:
    entity = random.sample(keyw,3)

print(entity)
convert(cleandf)
ready = pd.read_csv("test.csv")
del ready['Unnamed: 0']
sher_pred = sher(ready)

columnd = pd.read_csv(cold)
num = columnd.columns.tolist()
if len(num) == 2:
    columnd.columns = ['Column','Description']
else:
    columnd.columns = ['ID','Column','Description']
sqlcheat = pd.read_csv('sqlcheatsheet3.csv')

os.system('cls' if os.name == 'nt' else 'clear')
print("########################################")
print(entity)
print("Question Generating dataset")
print("1. Generate Questions")
print("2. Read Data Description")
print("3. Check data keywords")
simind = []
import spacy
nlp = spacy.load('en_core_web_lg')
colcheck = list(cleandf.columns)
newcolcheck = []
for i in colcheck:
    #print(i)
    i = i.replace("_"," ")
    newcolcheck.append(i)
#print(colcheck)
for i in newcolcheck:
    sum = 0
    for j in entity:
        x = nlp(i)
        y = nlp(j)
        z = x[0].similarity(y[0])
        sum += z
    simind.append(sum)
            #print(simind)

maxv = max(simind)
maxind = simind.index(maxv)
print(sher_pred)
inp = int(input("Enter Choice: "))
if inp == 1:
    
    g = 'y'
    while g == 'y':
        counter = 0
        for f in range(0,20):
            
            
            sql = sqlquery(cleandf,sher_pred,sqlcheat)
           
            #print(maxind)
            #print(sql)

        
            
            if counter <2:
                if ((sql[1] == colcheck[maxind] or sql[5] == colcheck[maxind]) ):
                    ques(sql,columnd,cleandf,sher_pred)
                    counter += 1
                else:
                    counter += 0 
            else:
                ques(sql,columnd,cleandf,sher_pred)


        g = input("Generate another set of questions(y/n): ")
        os.system('cls' if os.name == 'nt' else 'clear')
    if g == 'n':
        print("Thank You!")
elif inp == 2:
    f = open(datad, 'r')
    file_contents = f.read()
    print(file_contents)
elif inp == 3:
    import random
    if len(keyw) >=3:
        print("Enter the number of words in theme <=", len(keyw))
        sel = int(input(""))
        if(sel <= len(keyw)):
            print(random.sample(keyw,sel))
        else:
            print("Wrong Entry")

    else:
        print(keyw)
else:
    print("Wrong Entry")
        
    










