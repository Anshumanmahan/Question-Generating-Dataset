def fips(df,dfcold):
    import re
    import numpy as np
    import random
    import pandas as pd
    import os
    from parrot import Parrot
    import torch
    import warnings
    warnings.filterwarnings("ignore")

    from bs4 import BeautifulSoup
    import urllib.request
    import sys
    import os
    import selenium.webdriver
    import time
    from selenium import webdriver
    options = webdriver.FirefoxOptions()
    options.set_preference("browser.download.folderList", 2)
    options.set_preference("browser.download.dir", "/N/u/anshdixi/Carbonate/Sherlock/sherlock-project-master/QGD/download")
    options.set_preference("browser.download.useDownloadDir", True)
    options.set_preference("browser.download.viewableInternally.enabledTypes", "")
    options.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv")
    options.set_preference("pdfjs.disabled", True)

    linkword = "https://www.wordtune.com/" #my_url

    

    def random_state(seed):
        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)
    
    random_state(1234)

    parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5",use_gpu=False)
   # pip install transformers sentencepiece
    
    def to_str(var):
        return str(list(np.reshape(np.asarray(var), (1, np.size(var)))[0]))[1:-1]
    check = 0

    df_state = pd.read_csv("/N/u/anshdixi/Carbonate/Sherlock/sherlock-project-master/QGD/countyfipstool20190120.csv")

    state_code = df_state['sfips'].unique()
    state_name = df_state['sname'].unique()
    dict_state = dict(zip(state_code,state_name))

    df_county = pd.read_csv("/N/u/anshdixi/Carbonate/Sherlock/sherlock-project-master/QGD/county.csv")
    df_county = df_county[['GEO_ID','NAME']]
    df_county['GEO_ID']=df_county['GEO_ID'].str[-5:]
    dict_county = dict(zip(df_county['GEO_ID'],df_county['NAME']))
    df_Tract = pd.read_csv("/N/u/anshdixi/Carbonate/Sherlock/sherlock-project-master/QGD/Tract.csv")
    df_Tract = df_Tract[['GEO_ID','NAME']]
    df_Tract['GEO_ID']=df_Tract['GEO_ID'].str[-11:]
    dict_Tract= dict(zip(df_Tract['GEO_ID'],df_Tract['NAME']))
    
    #print(df.head())
    li = list(df.columns)
##Putting checks to see if the data contains fips code
    #if 'GEO_ID' in li:
     #   check = 1
      #  s = 'GEO_ID'
    if 'fips' in li:
        check = 1
        s = 'fips'
    elif 'FIPS' in li:
        check = 1
        s = 'FIPS'
    elif 'fips_code' in li:
        check = 1
        s = 'fips_code'
    elif 'fips code' in li:
        check = 1
        s = 'fips code'
    elif 'FIPS CODE' in li:
        check = 1
        s = 'FIPS CODE'
    elif 'county_fips' in li:
        check = 1
        s = 'county_fips'
    else:
        check = 0
    
#Regex check
    if check == 0:
        r = re.compile(r'.*(US).*')
        regmatch = np.vectorize(lambda x: bool(r.match(x)))
        for i in li:
            temp = regmatch(df[i].values)
            sav = i
            arr = np.array(temp)
            if (np.count_nonzero(arr) == (len(df) - 1)):
                check = 2
                break

    if check == 0:
        return check
    elif check == 2:
        columndes = pd.read_csv(dfcold,header = None)
        columndes.columns = ['ColumnName','ColumnDes']
        columndes['ColumnDes'] = columndes['ColumnDes'].str.replace(r'[^\w\s]+',' ')
        
        print(columndes.head())

        
        
        

        #guess = random.randint(0,len(df)-1)
        #value = df[sav].iloc[guess]
        li.remove(sav)
        #guess1 = random.randint(0,len(li) - 1)
        #value1 = li[guess1]
        #a = columndes[columndes['ColumnName'] == value1]
        #des = a["ColumnDes"].tolist()[0]
        os.system('cls' if os.name == 'nt' else 'clear')
        
        #print(value)
        #value = value.partition('US')[2]
        #if len(str(value)) in [2]:
         #   name = dict_state.get(value)
        #elif len(str(value)) in [5]:
         #   name = dict_county.get(value)
        #else:
         #   name = dict_Tract.get(value)
        
        #print(name)

        res = 'y'

        while res == 'y':
            guess = random.randint(0,len(df)-1)
            value = df[sav].iloc[guess]
            guess1 = random.randint(0,len(df)-1)
            value1 = df[sav].iloc[guess1]
            guess2 = random.randint(0,len(li) - 1)
            value2 = li[guess2]
            a = columndes[columndes['ColumnName'] == value2]
            des = a["ColumnDes"].tolist()[0]

            value = value.partition('US')[2]
            value1 = value1.partition('US')[2]
            if len(str(value)) in [2]:
                name = dict_state.get(value)
                name1 = dict_state.get(value1) 
            elif len(str(value)) in [5]:
                name = dict_county.get(value)
                name1 = dict_county.get(value1)
            else:
                name = dict_Tract.get(value)
                name1 = dict_Tract.get(value1)
            
            guess3 = random.randint(0,5)
            #print(guess3)
            if guess3 == 0:
                
                ques = "What is the average "+ des+ " in areas "+ name + " and " + name1
                print(ques)
                
                
            elif guess3 == 1:
                print("Which area has more "+ des+ " between "+ name+" and "+ name1)
            elif guess3 == 2:
                print("Which area has less "+des+" between "+name+" and " + name1)
            elif guess3 == 3:
                print("What is the sum of "+des+" in areas "+ name + " and " + name1)
            elif guess3 == 4:
                print("Which has the least "+ des+ " among all regions")
            elif guess3 == 5:
                print("Which has the most "+ des + " among all regions")
            
            
            
            res = input("Next Question?(y/n)")
        
    else:
        if len(to_str(df.iloc[1][s])) > 3 and len(to_str(df.iloc[1][s] < 6)):
            df[s] = df[s].apply(lambda x: '{0:0>5}'.format(x))
            print(df[s].head(20))
        elif len(to_str(df.iloc[1][s])) > 0 and len(to_str(df.iloc[1][s] < 3)):
            df[s] = df[s].apply(lambda x: '{0:0>2}'.format(x))
            print(df[s].head(20))
        elif len(to_str(df.iloc[1][s])) > 9 and len(to_str(df.iloc[1][s] < 12)):
            df[s] = df[s].apply(lambda x: '{0:0>11}'.format(x))
            print(df[s].head(20))
        
        li.remove(s)

        res = 'y'

        while res == 'y':
            guess = random.randint(0,len(df)-1)
            value = df[s].iloc[guess]
            guess1 = random.randint(0,len(df)-1)
            value1 = df[s].iloc[guess1]
            guess2 = random.randint(0,len(li) - 1)
            value2 = li[guess2]

            if len(str(value)) in [2]:
                name = dict_state.get(value)
                name1 = dict_state.get(value1) 
            elif len(str(value)) in [5]:
                name = dict_county.get(value)
                name1 = dict_county.get(value1)
            else:
                name = dict_Tract.get(value)
                name1 = dict_Tract.get(value1)
            
            guess3 = random.randint(0,5)
            #print(guess3)
            if guess3 == 0:
                
                #paraphrases = parrot.augment(input_phrase=value2)
                #for paraphrase in paraphrases:
                 #   print(paraphrase)
                ques = "What is the average "+ value2+ " in areas "+ name + " and " + name1
                
            elif guess3 == 1:
                ques = "Which area has more "+ value2+ " between "+ name+" and "+ name1
            elif guess3 == 2:
                ques = "Which area has less "+value2+" between "+name+" and " + name1
            elif guess3 == 3:
                guess = "What is the sum of "+value2+" in areas "+ name + " and " + name1
            elif guess3 == 4:
                guess = "Which has the least "+ value2+ " among all regions"
            elif guess3 == 5:
                guess = "Which has the most "+ value2 + " among all regions"
            
            driver = webdriver.Firefox(executable_path = '/N/u/anshdixi/Carbonate/geckodriver',options=options)
            driver.get(linkword)
            driver.find_element_by_xpath('/html/body/div[4]/header/div/div/div/div[3]/a/span[2]').click()
            main_window = driver.current_window_handle
            driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div/div[2]/button[1]/span[1]').click()
            
            gmailId = 'anshumandixit1996@gmail.com'
            passWord = 'barha455193'
            print(main_window)

            time.sleep(10)
            print(driver.window_handles[1])
            driver.switch_to.window(driver.window_handles[1])
            print(driver.title)

            loginBox = driver.find_element_by_xpath('//*[@id="identifierId"]')
            loginBox.send_keys(gmailId)
  
            nextButton = driver.find_elements_by_xpath('//*[@id ="identifierNext"]')
            nextButton[0].click()
  
            passWordBox = driver.find_element_by_xpath('//*[@id ="password"]/div[1]/div / div[1]/input')
            passWordBox.send_keys(passWord)
  
            nextButton = driver.find_elements_by_xpath('//*[@id ="passwordNext"]')
            nextButton[0].click()
            
            res = input("Next Question?(y/n)")
        


            
