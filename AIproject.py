import streamlit as st
import pandas as pd
import random
from better_profanity import profanity

# Laad dataset
df = pd.read_csv("shortjokes.csv")
jokes = df["Joke"].dropna()

# Streamlit interface
st.title("Joke Generator (English Version)")

censor = st.checkbox("Do you want to censor dark jokes? (These can be hurtful to some people) ")

with st.form("joke_form"):
    subject = st.text_input("What subject do you want to hear a joke about?")
    submit = st.form_submit_button("Generate Joke")

if submit:
    if not subject.strip():
        st.error("Please enter a subject first 😊")
    else:
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
                else:
                    st.error("Sorry, no jokes found about that subject 🌚")
        else:
            results = jokes[jokes.str.lower().str.contains(lower_subject)]
            if not results.empty:
                selected_joke = random.choice(results.tolist())
                st.success("Here it comes:")
                st.write(selected_joke)
            else:
                st.error("Sorry, no jokes found about that subject 🌚")
