import streamlit as st
import random

# Definition der Farben
class Theme:
    primaryColor = "#05f1c9"
    backgroundColor = "#c8e3e8"
    secondaryBackgroundColor = "#82bad2"
    textColor = "#0f1212"

theme = Theme()

# Anwendung des Themes
st.markdown(
    f"""
    <style>
    .reportview-container {{
        color: {theme.textColor};
        background-color: {theme.backgroundColor};
        font-family: Arial, sans-serif;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Liste der motivierenden Zitate
quotes = [
    "Your chemistry teacher WILL find you and lecture you, if you still dont know how H2O is loaded.",
    "Drink water, your organs are failing!",
    "I 🐝 🍃 in you!!",
    # Weitere Zitate hier ...
]

# Abrufen eines zufälligen Zitats, das für einen Tag zwischengespeichert wird
@st.cache_data(ttl=86400)
def get_daily_quote():
    return random.choice(quotes)

# Funktion zur Anzeige der Startseite
def show_home():
    st.title("Willkommen zu BioChem Pathways!")
    # Hier Inhalte für die Startseite einfügen

# Funktionen zur Anzeige der verschiedenen Seiten
def show_pathways():
    st.title("Pathways")
    st.write("Hier sind die Inhalte zu Pathways.")

def show_eselsbrücken():
    st.title("Eselsbrücken")
    st.write("Hier sind die Inhalte zu Eselsbrücken.")

def show_memes():
    st.title("Memes")
    st.write("Hier sind die Inhalte zu Memes.")

def show_quiz():
    st.title("Quiz")
    st.write("Hier sind die Inhalte zu Quiz.")

# Hauptfunktion zur Anzeige der Seiten basierend auf der aktuellen Seite im Session State
def main():
    st.set_page_config(
        page_title="BioPathways",
        page_icon=":dna:",
        layout="centered",
        initial_sidebar_state="expanded"
    )

    page = st.sidebar.radio(
        "Navigation",
        ["Home", "Pathways", "Eselsbrücken", "Memes", "Quiz"]
    )

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

    # Zitat des Tages
    quote = get_daily_quote()
    st.markdown(f"""
        <div style="background-color: #e0f7fa; padding: 20px; border-radius: 15px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); margin: 20px;">
            <h2 style="text-align: center; color: #00796b; font-family: 'Arial', sans-serif;">{quote}</h2>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

