def ques(sql,col,df,sher_pred):
    from gingerit.gingerit import GingerIt
    import matplotlib.pyplot as plt
    import random
    import seaborn as sns
    #print(sql)
    name = sql[5]
    #print(name)
    x = col[col["Column"] == name]
    #print(x)
    des = x["Description1"].tolist()[0]
    #print(des)
    col1 = list(df.columns)

    if "*" in sql:
        print("Show all the records where", des, "are", sql[6],sql[7],"?")
        if(sql[6] == "Equal to"):
            ans = df[df[name] == sql[7]]
        elif (sql[6] == "Not Equal to"):
            ans = df[df[name] != sql[7]]
        elif (sql[6] == "Lesser than"):
            ans = df[df[name] < sql[7]]
        else:
            ans = df[df[name] > sql[7]]
    else:
        name1 = sql[1]
        #print(name1)
        x1 = col[col["Column"] == name1]
        #print(x1)
        des1 = x1["Description1"].tolist()[0]
        #print(des1)
        if 'year' in sher_pred:
            if 'year' in sql[5]:
                a3 = random.randint(0,3)
                if a3 == 0:
                    print('In which year', des1, 'was maximum')
                elif a3 == 1:
                    print('In which year', des1, 'was minimum')
                elif a3 == 2:
                    print('In which year', des1, 'was below average')
                else:
                    print('In which year', des1, 'was above average')
        else:
            if (sql[6] == "Minimum"):
                a1 = random.randint(0,1)
                if a1 == 1:
                    ques = "What is the minimum " + des + " among all " + des1 + " ?"
                    ques = GingerIt().parse(ques)
                    print(ques['result'])
                    ask = input('Do you want to see viz or just answer (v for viz and a for answer)')
                    if ask == 'a':
                        ind = df[name].idxmin()
                        ans = df.iloc[ind,:]
                        print(ans)
                    elif ask == 'v':
                        df_sorted = df.sort_values(name)
                        plt.figure(figsize=(10,6))
                        plt.bar(name1,name, data = df_sorted.iloc[0:5])
                        plt.xlabel(name1,size = 15)
                        plt.ylabel(name,size = 15)
                        plt.show()
                else:
                    ques = "Which "+ des1 + " has the least "+ des + " ?"
                    ques = GingerIt().parse(ques)
                    print(ques['result'])
                    ask = input('Do you want to see viz or just answer (v for viz and a for answer)')
                    if ask == 'a':
                        ind = df[name].idxmin()
                        ans = df.iloc[ind,:]
                        print(ans)
                    elif ask == 'v':
                        df_sorted = df.sort_values(name)
                        plt.figure(figsize=(10,6))
                        plt.bar(name1,name, data = df_sorted.iloc[0:5])
                        plt.xlabel(name1,size = 15)
                        plt.ylabel(name,size = 15)
                        plt.show()
            elif (sql[6] == "Maximum"):
                a2 = random.randint(0,1)
                if a2 == 1:
                    ques = "What is the maximum "+des+" among all "+des1
                    ques = GingerIt().parse(ques)
                    print(ques['result'])
                    ask = input('Do you want to see viz or just answer (v for viz and a for answer)')
                    if ask == 'a':
                        ind = df[name].idxmax()
                        ans = df.iloc[ind,:]
                        print(ans)
                    elif ask == 'v':
                        df_sorted = df.sort_values(name,ascending = False)
                        plt.figure(figsize=(10,6))
                        plt.bar(name1,name, data = df_sorted.iloc[0:5])
                        plt.xlabel(name1,size = 15)
                        plt.ylabel(name,size = 15)
                        plt.show()
                else:
                    ques = "Which "+des1+" has the highest "+des+" ?"
                    ques = GingerIt().parse(ques)
                    print(ques['result'])
                    ask = input('Do you want to see viz or just answer (v for viz and a for answer)')
                    if ask == 'a':
                        ind = df[name].idxmax()
                        ans = df.iloc[ind,:]
                        print(ans)
                    elif ask == 'v':
                        df_sorted = df.sort_values(name,ascending = False)
                        plt.figure(figsize=(10,6))
                        plt.bar(name1,name, data = df_sorted.iloc[0:5])
                        plt.xlabel(name1,size = 15)
                        plt.ylabel(name,size = 15)
                        plt.show()
            elif (sql[6] == "Average "):
                
                r1 = random.randint(0,1)
                if r1 == 0:
                    print("What is the average",des,"among all",des1)
                    ans = df[name].mean()
                else:
                    guess = random.randint(0,len(df[sql[1]])-1)
                    value = df[sql[1]].iloc[guess]
                    guess1 = random.randint(0,len(df[sql[1]])-1)
                    value1 = df[sql[1]].iloc[guess1]
                    print("What is the average",des,"where",des1,"is",value,"and",value1)
                    res = df[df[name1] == value][name].values[0]
                    res1 = df[df[name1] == value1][name].values[0]
                   # ans = (res + res1)/2
            elif (sql[6] == "COUNT"):
                import random
                guess = random.randint(0,len(df[sql[1]])-1)
                value = df[sql[1]].iloc[guess]
                print("How many instances in the record has",des1,"equal to",value)
                ans = df[name1].value_counts()[value]
            elif (sql[6] == "sum of"):
                import random
                guess = random.randint(0,len(df[sql[1]])-1)
                value = df[sql[1]].iloc[guess]
                guess1 = random.randint(0,len(df[sql[1]])-1)
                value1 = df[sql[1]].iloc[guess1]
                print("What is the Sum of",des,"in",des1,value,"and",value1)
                res = df[df[name1] == value][name].values[0]
                res1 = df[df[name1] == value1][name].values[0]
                ans = res + res1
            else:
                import random
                r = random.randint(0,1)
                if r == 0:
                    print("Which",des1, "has",des ,sql[6],sql[7], "?")
                    if(sql[6] == "Equal to"):
                        ans = df[df[name] == sql[7]][name1]
                    elif (sql[6] == "Not Equal to"):
                        ans = df[df[name] != sql[7]][name1]
                    elif (sql[6] == "Lesser than"):
                        ans = df[df[name] < sql[7]][name1]
                    else:
                        ans = df[df[name] > sql[7]][name1]
                else:
                    print("What is the", des1 , "where", des  ,sql[6], sql[7], "?")
                    if(sql[6] == "Equal to"):
                        ans = df[df[name] == sql[7]][name1]
                    elif (sql[6] == "Not Equal to"):
                        ans = df[df[name] != sql[7]][name1]
                    elif (sql[6] == "Lesser than"):
                        ans = df[df[name] < sql[7]][name1]
                    else:
                        ans = df[df[name] > sql[7]][name1]

    #inp = input("Enter y for result: ")
    #if inp == 'y':
        #print(ans)
        #import time
        #time.sleep(3)
    #else:
        #print("")
    
            

