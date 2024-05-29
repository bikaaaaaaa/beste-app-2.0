import streamlit as st
import random

def main():
    st.title("BioPathways")

    page = st.sidebar.selectbox("Select a page", ["Home", "Pathways", "Eselsbrücken", "Memes", "Quiz"])

    if page == "Home":
        show_home()
    elif page == "Pathways":
        show_pathways()
    elif page == "Eselsbrücken":
        show_eselsbrücken()
    elif page == "Memes":
        show_memes()
    elif page == "Quiz":
        show_quiz()

def show_home():
    st.write("Welcome to the BioPathways homepage!")

def show_pathways():
    st.title("Pathways")
    st.write("Here are the contents for Pathways.")
    st.image("pathways_image.jpg", use_column_width=True)
    st.button("Pathways Button")

def show_eselsbrücken():
    st.title("Eselsbrücken")
    st.write("Here are the contents for Eselsbrücken.")
    st.image("eselsbrücken_image.jpg", use_column_width=True)
    st.button("Eselsbrücken Button")

def show_memes():
    st.title("Memes")
    st.write("Here are the contents for Memes.")
    st.image("memes_image.jpg", use_column_width=True)
    st.button("Memes Button")

def show_quiz():
    st.title("Quiz")
    st.write("Here are the contents for Quiz.")
    st.image("quiz_image.jpg", use_column_width=True)
    st.button("Quiz Button")

if __name__ == "__main__":
    main()


