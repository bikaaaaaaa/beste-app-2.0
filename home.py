import streamlit as st
import random

# Seitenkonfiguration
st.set_page_config(
    page_title="BioPathways",
    page_icon=":dna:",  # Symbol, falls benötigt
    layout="centered",  # Ausrichtung des Inhalts
    initial_sidebar_state="expanded",  # Standardzustand der Seitenleiste
)

# Liste der motivierenden Zitate
quotes = [
    "Your chemistry teacher WILL find you and lecture you, if you still dont know how H2O is loaded.",
    "Drink water, your organs are failing!",
    "I 🐝 🍃 in you!!",
    "JUST DO IT!",
    "🦄",
    "Never back down never what? – never give up – NEVER BACK DOWN NEVER WHAT? – Never give up!!",
    "„Do or do not. There is no try.“ – Yoda",
    "Never gonna give you up 🕺 Never gonna let you down 💃 Never gonna run around and desert you 🕺Never gonna make you cry 💃 Never gonna say goodbye 🕺Never gonna tell a lie and hurt you 💃",
    "„It is not our abilities that show what we truly are … it is our choices.“ – Dumbledore",
    "“Just keep swimming. Just keep swimming. Just keep swimming, swimming, swimming. What do we do? We swim, swim.” – Dory",
    "You dropped this 👑",
    "In this world you either crank that soulja boy or it cranks you",
    "Sorry i’m too thicc to do anything half-assed",
    "Do literally whatever makes you happy",
    "You know what it takes to make a star shine? A shitload of fucking darkness",
    "Be kind to ya mind",
    "Don‘t let idiots ruin your day",
    "Don‘t be ashamed of who you are. That’s your parents' job",
    "Don’t be a whiny little shit",
    "Logic will get you from A to B. Imagination will take you everywhere – Albert Einstein"
]

# Abrufen eines zufälligen Zitats, das für einen Tag zwischengespeichert wird
@st.cache_data(ttl=86400)
def get_daily_quote():
    return random.choice(quotes)

# Funktion zur Anzeige der Startseite
def show_home():
    st.title("Willkommen zu BioChem Pathways!")
    
    # Anzeige der Debugging-Nachricht
    st.write("Überprüfung der Bildpfade:")
    st.image("images/pathways.jpeg", caption="Pathways")
    st.image("images/eselsbrücke.jpeg", caption="Eselsbrücken")
    st.image("images/memes.jpeg", caption="Memes")
    st.image("images/quiz.jpeg", caption="Quiz")
    
    # Anzeige der Buttons
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("Pathways"):
            st.session_state.page = 'Pathways'

    with col2:
        if st.button("Eselsbrücken"):
            st.session_state.page = 'Eselsbrücken'

    with col3:
        if st.button("Memes"):
            st.session_state.page = 'Memes'

    with col4:
        if st.button("Quiz"):
            st.session_state.page = 'Quiz'

    # Zitat des Tages, zentriert und gestaltet
    quote = get_daily_quote()
    st.markdown(f"""
        <div style="background-color: #e0f7fa; padding: 20px; border-radius: 15px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); margin: 20px;">
            <h2 style="text-align: center; color: #00796b; font-family: 'Arial', sans-serif;">{quote}</h2>
        </div>
    """, unsafe_allow_html=True)

# Funktionen zur Anzeige der anderen Seiten
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
    if 'page' not in st.session_state:
        st.session_state.page = 'Home'

    if st.session_state.page == 'Home':
        show_home()
    elif st.session_state.page == 'Pathways':
        show_pathways()
    elif st.session_state.page == 'Eselsbrücken':
        show_eselsbrücken()
    elif st.session_state.page == 'Memes':
        show_memes()
    elif st.session_state.page == 'Quiz':
        show_quiz()

if __name__ == "__main__":
    main()
