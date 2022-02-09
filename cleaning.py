def clean(df):
    col = list(df.columns)
    #Check for gargabe string in numerical column
    import numpy as np
    import pandas as pd
    
    #for i in range(0,len(col)):
     #   df = df[np.isfinite(pd.to_numeric(df[col[i]], errors="coerce"))]
    
    
    #Checking and Dropping null values
    if df.isnull().values.any() == 'True':
        df = df.dropna()
   
    #Dropping duplicate columns
    df.drop_duplicates()
    
    #Checking for stop words in columns
    col = list(df.columns)
    from nltk.corpus import stopwords
    filtered_words = [word for word in col if word not in stopwords.words('english')]
    df.columns = filtered_words
    
    return df
