import pandas as pd
from better_profanity import profanity
 
df = pd.read_csv("C:/Users/jboen/OneDrive/Desktop/AI Informatica/shortjokes.csv")

Jokes = df["Joke"].dropna()  
 
censor = input("\nDo you want to censor the jokes? (yes or no) ")
Subject = input("What subject do you want to hear a joke about? ").lower()
 
if censor == ("yes" or "Yes" or "yes." or "Yes." or "YES" or "YES."):
    profanity.load_censor_words()
    if profanity.contains_profanity(Subject):
        print("this subject is innapropriate 😬")
        exit()
 
resultaten = Jokes[Jokes.str.lower().str.contains(Subject)]
 
if not resultaten.empty:
    import random
    Joke = random.choice(resultaten.tolist())
    print("\nHere it comes:")
    print(Joke)
else:
    print("Sorry, no jokes found about that subject 😅")