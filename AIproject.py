import streamlit as st
import pandas as pd
import random
from better_profanity import profanity
 
df = pd.read_csv("shortjokes.csv")
jokes = df["Joke"].dropna()
blocked_words = ["black", "lack people", "lack person", "ack", "ck people", "ck person", "k people", "k person", "farming equipment", "terrorist", "knee", "grow", "snickers", "nickers", "nicker", "sickness", "sick", "cancer", "diabetes", "butt", "die", "dying", "death", "dead", "jerking"]
 
st.title("Joke Generator (English Version)")

st.markdown("""<style>.stApp {background-image: url("https://img.freepik.com/free-vector/flat-comic-style-background-copy-space_52683-54924.jpg?semt=ais_hybrid&w=740");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;}</style>""",unsafe_allow_html=True)

censor = st.checkbox("Do you want to censor dark jokes? (These can be hurtful to some people) ")
subject = st.text_input("What subject do you want to hear a joke about?")
generate = st.button("Generate Joke")
 
if generate and subject.strip():
    lower_subject = subject.lower()
 
    if censor:
        profanity.load_censor_words()
        if profanity.contains_profanity(lower_subject) or any(word in lower_subject for word in blocked_words):
            st.warning("This subject is inappropriate 😬")
        else:
            results = jokes[jokes.str.lower().str.contains(lower_subject)]
            if not results.empty:
                selected_joke = random.choice(results.tolist())
                st.success("Here it comes:")
                st.markdown(f"*****{profanity.censor(selected_joke)}*****")
                st.image("https://static.vecteezy.com/system/resources/thumbnails/048/560/668/small_2x/cheerful-cute-emoji-png.png", use_container_width =True)
            else:
                st.error("Sorry, no jokes found about that subject 🌚")
    else:
        results = jokes[jokes.str.lower().str.contains(lower_subject)]
        if not results.empty:
            selected_joke = random.choice(results.tolist())
            st.success("Here it comes:")
            st.markdown(f"*****{selected_joke}*****")
            st.image("https://static.vecteezy.com/system/resources/thumbnails/048/560/668/small_2x/cheerful-cute-emoji-png.png", use_container_width =True)
        else:
            st.error("Sorry, no jokes found about that subject 🌚")
 
elif generate and not subject.strip():
    st.error("Please enter a subject first 😊")
