import streamlit as st
import pandas as pd
import random
from better_profanity import profanity

df = pd.read_csv("shortjokes.csv")
jokes = df["Joke"].dropna()

st.title("Joke Generator (English Version)")

censor = st.checkbox("Do you want to censor dark jokes? (These can be hurtful to some people) ")
subject = st.text_input("What subject do you want to hear a joke about?")
generate = st.button("Generate Joke")

if generate and subject.strip():
    lower_subject = subject.lower()

    if censor:
        profanity.load_censor_words()
        if profanity.contains_profanity(lower_subject):
            st.warning("This subject is inappropriate 😬")
        else:
            results = jokes[jokes.str.lower().str.contains(lower_subject)]
            if not results.empty:
                selected_joke = random.choice(results.tolist())
                st.success("Here it comes:")
                st.write(profanity.censor(selected_joke))
                st.image("https://1000logos.net/wp-content/uploads/2023/05/Laughing-Emoji.png", use_column_width=True)
            else:
                st.error("Sorry, no jokes found about that subject 🌚")
    else:
        results = jokes[jokes.str.lower().str.contains(lower_subject)]
        if not results.empty:
            selected_joke = random.choice(results.tolist())
            st.success("Here it comes:")
            st.write(selected_joke)
            st.image("https://1000logos.net/wp-content/uploads/2023/05/Laughing-Emoji.png", use_column_width=True)
        else:
            st.error("Sorry, no jokes found about that subject 🌚")

elif generate and not subject.strip():
    st.error("Please enter a subject first 😊")
