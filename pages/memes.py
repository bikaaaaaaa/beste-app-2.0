import streamlit as st
import random

memes = [
    "memes/1.jpeg",
    "memes/2.jpeg",
    "memes/3.jpeg",
    "memes.images/4.jpeg",
    "memes.images/5.jpeg",
    "memes.images/6.jpeg",
    "memes.images/7.jpeg",
    "memes.images/8.jpeg",
    "memes.images/9.jpeg",
    "memes.images/10.jpeg",
    "memes.images/11.jpeg",
    "memes.images/12.jpeg",
    "memes.images/13.jpeg",
    "memes.images/14.jpeg",
    "memes.images/15.jpeg",
    "memes.images/16.jpeg",
    "memes.images/17.jpeg",
    "memes.images/18.jpeg",
    "memes.images/19.jpeg",
    "memes.images/20.jpeg",
    "memes.images/21.jpeg",
    "memes.images/22.jpeg",
    "memes.images/23.jpeg",
    "memes.images/24.jpeg",
    "memes.images/25.jpeg",
    "memes.images/26.jpeg",
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

