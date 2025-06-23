import streamlit as st
import pandas as pd
import random
from better_profanity import profanity

# Laad dataset
df = pd.read_csv("shortjokes.csv")
jokes = df["Joke"].dropna()

# Streamlit interface
st.title("🎭 Grapgenerator")

censor = st.checkbox("Censureer ongepaste taal")
subject = st.text_input("Over welk onderwerp wil je een grap horen?")

if subject:
    lower_subject = subject.lower()

    if censor:
        profanity.load_censor_words()
        if profanity.contains_profanity(lower_subject):
            st.warning("Dat onderwerp is ongepast 😬")
        else:
            results = jokes[jokes.str.lower().str.contains(lower_subject)]
            if not results.empty:
                selected_joke = random.choice(results.tolist())
                censored_joke = profanity.censor(selected_joke)
                st.success("Hier komt 'ie:")
                st.write(censored_joke)
            else:
                st.error("Sorry, geen grappen gevonden over dat onderwerp 😅")
    else:
        results = jokes[jokes.str.lower().str.contains(lower_subject)]
        if not results.empty:
            selected_joke = random.choice(results.tolist())
            st.success("Hier komt 'ie:")
            st.write(selected_joke)
        else:
            st.error("Sorry, geen grappen gevonden over dat onderwerp 😅")
