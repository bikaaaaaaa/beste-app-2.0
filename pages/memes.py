import streamlit as st
import random

memes = [
    "memes/1.jpeg",
    "memes/2.jpeg",
    "memes/3.jpeg",
    "memes/4.jpeg",
    "memes/5.jpeg",
    "memes/6.jpeg",
    "memes/7.jpeg",
    "memes/8.jpeg",
    "memes/9.jpeg",
    "memes/10.jpeg",
    "memes/11.jpeg",
    "memes/12.jpeg",
    "memes/13.jpeg",
    "memes/14.jpeg",
    "memes/15.jpeg",
    "memes/16.jpeg",
    "memes/17.jpeg",
    "memes/18.jpeg",
    "memes/19.jpeg",
    "memes/20.jpeg",
    "memes/21.jpeg",
    "memes/22.jpeg",
    "memes/23.jpeg",
    "memes/24.jpeg",
    "memes/25.jpeg",
    "memes/26.jpeg",
]

# Funktion, um ein Meme zu bekommen
def get_random_meme():
    meme = random.choice(memes)
    return meme

def main():
    st.title("Motivationsmemes")

    if st.button("Neues Meme bekommen"):
        meme = get_random_meme()
    else:
        meme = get_random_meme()

    st.image(meme, caption="Motivationsmeme", use_column_width=True)

if __name__ == "__main__":
    main()

