import streamlit as st
import random
from datetime import datetime

# Установка темы
st.set_page_config(
    page_title="BioPathways",
    page_icon=":dna:",  # Иконка, если нужна
    layout="centered",  # Выравнивание содержимого
    initial_sidebar_state="expanded",  # Состояние боковой панели по умолчанию
)

def main():

    # Определение цветов
    class Theme:
        primaryColor = "#05f1c9"
        backgroundColor = "#c8e3e8"
        secondaryBackgroundColor = "#82bad2"
        textColor = "#0f1212"

    theme = Theme()

    # Применение темы
    st.markdown(
        f"""
        <style>
        .reportview-container.main.block-container {{
            color: {theme.primaryColor};
            background-color: {theme.backgroundColor};
            font-family: Arial, sans-serif;
        }}
        .reportview-container.main {{
            color: {theme.primaryColor};
            background-color: {theme.backgroundColor};
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

    if 'page' not in st.session_state:
        st.session_state.page = 'Home'

    # Anzeige der entsprechenden Seite
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

    # Центрированное и оформленное в светло-голубых оттенках цитата
    quote = get_daily_quote()
    st.markdown(f"""
        <div style="background-color: #e0f7fa; padding: 20px; border-radius: 15px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); margin: 20px;">
            <h2 style="text-align: center; color: #00796b; font-family: 'Arial', sans-serif;">{quote}</h2>
        </div>
    """, unsafe_allow_html=True)

# Funktion zur Anzeige der Home-Seite
def show_home():
    st.title("Willkommen zu BioChem Pathways!")
 
    col1, col2, col3, col4 = st.columns(4)
 
    with col1:
        if st.button("Pathways", key='pathways_button'):
            st.switch_page('pages/pathways.py')
        st.image("images/pathways.jpeg", caption="Pathways")
 
    with col2:
        if st.button("Eselsbrücken", key='eselsbrücken_button'):
            st.switch_page('pages/eselsbrücken.py')
        st.image("images/eselsbrücke.jpeg", caption="Eselsbrücken")
 
    with col3:
        if st.button("Memes", key='memes_button'):
            st.switch_page('pages/memes.py')
        st.image("images/memes.jpeg", caption="Memes")
 
    with col4:
        if st.button("Quiz", key='quiz_button'):
            st.switch_page('pages/quiz.py')
        st.image("images/quiz.jpeg", caption="Quiz")
 
# Funktion zur Anzeige der Pathways-Seite
def show_pathways():
    st.title("Pathways")
    st.write("Hier sind die Inhalte zu Pathways.")
 
# Funktion zur Anzeige der Eselsbrücken-Seite
def show_eselsbrücken():
    st.title("Eselsbrücken")
    st.write("Hier sind die Inhalte zu Eselsbrücken.")
 
# Funktion zur Anzeige der Memes-Seite
def show_memes():
    st.title("Memes")
    st.write("Hier sind die Inhalte zu Memes.")
 
# Funktion zur Anzeige der Quiz-Seite
def show_quiz():
    st.title("Quiz")
    st.write("Hier sind die Inhalte zu Quiz.")
 
# List of motivational quotes
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

# Получение случайной цитаты, закешированной на день
@st.cache_data(ttl=86400)
def get_daily_quote():
    return random.choice(quotes)

if __name__ == "__main__":
    main()


