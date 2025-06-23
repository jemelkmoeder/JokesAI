import streamlit as st
import pandas as pd
import random
from better_profanity import profanity

# Laad dataset
df = pd.read_csv("shortjokes.csv")
jokes = df["Joke"].dropna()

# Streamlit interface
st.title("Joke generator")

censor = st.checkbox("Do you want to censor the jokes? (yes or no) ")
subject = st.text_input("What subject do you want to hear a joke about? ")

if subject:
    lower_subject = subject.lower()

    if censor:
        profanity.load_censor_words()
        if profanity.contains_profanity(lower_subject):
            st.warning("this subject is innapropriate 😬")
        else:
            results = jokes[jokes.str.lower().str.contains(lower_subject)]
            if not results.empty:
                selected_joke = random.choice(results.tolist())
                censored_joke = profanity.censor(selected_joke)
                st.success("Here it comes:")
                st.write(censored_joke)
            else:
                st.error("Sorry, no jokes found about that subject 😅")
    else:
        results = jokes[jokes.str.lower().str.contains(lower_subject)]
        if not results.empty:
            selected_joke = random.choice(results.tolist())
            st.success("Here it comes:")
            st.write(selected_joke)
        else:
            st.error("Sorry, no jokes found about that subject 😅")
