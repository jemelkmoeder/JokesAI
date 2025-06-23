import streamlit as st
import pandas as pd
import random
from better_profanity import profanity

# Verboden combinaties of gevoelige termen
blocked_phrases = ["black people", "terrorist", "blackperson", "black-person"]

# Laad dataset
df = pd.read_csv("shortjokes.csv")
jokes = df["Joke"].dropna()

# Streamlit interface
st.title("Joke Generator (English Version)")

censor = st.checkbox("Do you want to censor dark jokes? (These can be hurtful to some people) ")
subject = st.text_input("What subject do you want to hear a joke about?")
generate = st.button("Generate Joke")

if generate and subject.strip():
    lower_subject = subject.lower()
    profanity.load_censor_words()

    # Censuurcontrole op onderwerp
    if censor and (profanity.contains_profanity(lower_subject) or any(term in lower_subject for term in blocked_phrases)):
        st.warning("This subject is inappropriate 😬")

    else:
        results = jokes[jokes.str.lower().str.contains(lower_subject)]

        # Filter ook grappen die ongewenste termen bevatten
        if censor:
            results = results[~results.str.lower().str.contains("|".join(blocked_phrases))]

        if not results.empty:
            selected_joke = random.choice(results.tolist())
            st.success("Here it comes:")
            joke_to_display = profanity.censor(selected_joke) if censor else selected_joke
            st.markdown(f"***{joke_to_display}***")
            st.image("https://static.vecteezy.com/system/resources/thumbnails/048/560/668/small_2x/cheerful-cute-emoji-png.png", use_container_width=True)
        else:
            st.error("Sorry, no jokes found about that subject 🌚")

elif generate and not subject.strip():
    st.error("Please enter a subject first 😊")
