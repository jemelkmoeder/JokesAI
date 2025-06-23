import streamlit as st
import pandas as pd
import random
from better_profanity import profanity

# Laad dataset
df = pd.read_csv("shortjokes.csv")
jokes = df["Joke"].dropna()

# Initieer session state voor joke
if "joke" not in st.session_state:
    st.session_state.joke = ""
if "error" not in st.session_state:
    st.session_state.error = ""

# Streamlit interface
st.title("Joke Generator (English Version)")

censor = st.checkbox("Do you want to censor dark jokes? (These can be hurtful to some people) ")
subject = st.text_input("What subject do you want to hear a joke about? ")
generate = st.button("Generate Joke")

if generate:
    if subject:
        lower_subject = subject.lower()
        profanity.load_censor_words()

        if censor and profanity.contains_profanity(lower_subject):
            st.session_state.error = "This subject is inappropriate 😬"
            st.session_state.joke = ""
        else:
            results = jokes[jokes.str.lower().str.contains(lower_subject)]
            if not results.empty:
                selected_joke = random.choice(results.tolist())
                if censor:
                    st.session_state.joke = profanity.censor(selected_joke)
                else:
                    st.session_state.joke = selected_joke
                st.session_state.error = ""
            else:
                st.session_state.error = "Sorry, no jokes found about that subject 🌚"
                st.session_state.joke = ""
    else:
        st.session_state.error = "Please enter a subject first 😊"
        st.session_state.joke = ""

# Laat de joke of foutmelding zien als die er is
if st.session_state.error:
    st.error(st.session_state.error)
elif st.session_state.joke:
    st.success("Here it comes:")
    st.write(st.session_state.joke)
