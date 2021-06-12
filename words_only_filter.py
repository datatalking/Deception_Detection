from nltk.corpus import words
nltkstems = [stemmer.stem(word) for word in words.words()] #stem the #words in the NLTK corpus so that they’re equivalent to the words in #the allwordsdf dataframe
nltkwords = pd.DataFrame() #make a new dataframe with the stemmed #NLTK words
nltkwords[‘words’] = nltkstems
allwordsdf = allwordsdf[allwordsdf[‘words’].isin(nltkwords[‘words’])] #keep only #those in the stemmed NLTK corpus


allwordsdf[allwordsdf[‘count’] == allwordsdf[‘count’].quantile(.4)][:10]

