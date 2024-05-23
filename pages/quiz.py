import streamlit as st
 
def main():
    st.title("Quiz")
    st.write("Welcome to the Biochemistry Quiz!")
 
    # Choose difficulty level using radio buttons
    level = st.sidebar.radio("Choose the difficulty level:", ["Easy 🟢", "Medium 🟡", "Hard 🔴"])
 
    questions = []
    options = []
    correct_answers = []  # List of indices of correct answers
 
    # Generate questions, options, and indices of correct answers based on selected difficulty level
    if level.startswith("Easy"):
        questions = [
            "Wo wird Glykogen synthetisiert und gespeichert?",
            "Wo findet die Reaktion Citratzyklus statt?",
            "Was ist das Endprodukt der Glykolyse?",
            "Was ist das Hauptziel der Atmungskette?",
            "Welches Enzym katalysiert den ersten Schritt der Glykolyse?",
            "Welches Enzym katalysiert die letzte Reaktion der Glykolyse?",
            "Wie viele Moleküle CO₂ werden pro Glukosemolekül im Citratzyklus freigesetzt?",
            "Welches Molekül startet den Citratzyklus durch die Kondensation mit Oxalacetat?",
            "Was ist das Ausgangsmolekül der Glykolyse?",
            "Was entsteht am Ende Glykolyse?",
            "Welches Molekül wird im Citratzyklus direkt nach Citrat gebildet?",
            "Wo findet die Atmungskette statt?",
        ]
           
        options = [
            ["Milz & Colon", "Hepar & Muskel", "Derma & Fett", "Milz & Jejunum"],
            ["Zytosol", "Zellkern", "Raues Endoplasmatische Retikulum", "Mitochondrium"],
            ["Pyruvat", "Acetyl CoA", "GAP", "Fumarat"],
            ["Das Hauptziel der Atmungskette ist die Produktion von Sauerstoff für die Zelle", "Die Erzeugung von ATP durch oxidative Phosphorylierung", "Die Atmungskette erzeugt Wärme durch die Oxidation von Fetten", "Die Atmungskette verwendet Kohlenstoffdioxid um Sauerstoff zu erzeugen"],
            ["Aldolase", "Hexokinase", "Phosphofructokinase", "Phosphoglyceratkinase"],
            ["Pyruvatkinase", "Enolase", "Aldolase", "Phosphoplyceratkinase"],
            ["4 CO₂", "0 CO₂", "2 CO₂", "6 CO₂"],
            ["Glukose", "Acetyl-CoA", "Pyruvat", "ATP"],
            ["Pyruvat", "Glukose", "Acetyl-Coa", "Elektronen"],
            ["Elektronen & Protonen", "ADP & ELektronen", "H+ & ATP", "ATP & NADH"],
            ["Acetyl-CoA", "Oxalacetat","Isocitrat" ,"Succinyl-CoA"],
            ["Im Zytoplasma", "Im Zellkern", "In der äusseren Mitochondrienmembran", "Im innere Mitochondrienmembran"]
        ]
       
        correct_answers = [1, 3, 0, 1, 1, 0, 0, 1, 1, 3, 2, 3]  # Indices of correct answers for each question
 
 
    elif level.startswith("Medium"):
        questions = [
            "Was aktiviert das Citratzyklus?",
            "Im 1. Teil der Glykolyse entstehen aus Glucose -> Glycerinaldehyd-3-phosphat (GAP) und Dihydroxyacetonphosphat (DAP). Welches dieser Moleküle kann direkt im 2. Teil der Glykolyse weiter abgebaut werden und welches muss zuerst isomerisiert werden?",
            "Welche Verbindung wird durch die Hexokinase während der Glykolyse phosphoryliert?",
            "Welches Enzym katalysiert die Umwandlung von Fruktose-1,6-bisphosphat in Dihydroxyacetonphosphat und Glycerinaldehyd-3-phosphat?",
            "Welche Verbindung wird im Citratzyklus durch die Isocitrat-Dehydrogenase decarboxyliert?",
            "Wie viele Moleküle CO₂ werden pro Durchlauf des Citratzyklus freigesetzt?",
            "Wie viele ATP-Moleküle entstehen aus einem NADH-Molekül in der Atmungskette?",
            "Wie viele ATP-Moleküle entstehen aus einem FADH₂-Molekül in der Atmungskette?",
            "Welches Enzym katalysiert die Umwandlung von Pyruvat zu Acetyl-CoA?",
            "Was ist die Funktion der Fumarase im Citratzyklus?",
            "Welches Molekül ist der Hauptdonator von Elektronen für den Elektronentransport in der mitochondrialen Atmungskette?",
            "Welches Molekül wird im Citratzyklus direkt vor der Bildung von Succinyl-CoA gebildet?"
 
 
        ]
        options = [
            ["ATP & Reduzierte Elektronenträger", "ATP & Glukose", "Calcium & ADP", "Magnesium & AMP"],
            ["GAP wird ohne Umwege abgebaut, DAP muss zuvor zu GAP isomerisiert werden", "GAP wird zuerst zu DAP isomerisiert, bevor es weiter abgebaut wird", "Beide Moleküle werden direkt im zweiten Teil der Glykolyse abgebaut, ohne vorherige Isomerisierung", "DAP wird ohne Umwege abgebaut, während GAP zuerst isomerisiert werden muss, um weiter verarbeitet zu werden"],
            ["Glukose-6-phosphat zu Fructose-6-phosphat", "Glukose zu Glukose-6-Phosphat", "Glukose zu Fructose-6-phosphat", "Glukose-6-phosphat zu Glukose"],
            ["Enolase", "Carboxylase", "Aldolase", "Pyruvatkinase"],
            ["Citrat", "Acetyl-Citrat", "Citrus", "Isocitrat"],
            ["2 CO₂", "0 CO₂", "1 CO₂", "3 CO₂"],
            ["ca. 0.5 ATP", "ca. 1.5 ATP", "ca. 2.5 ATP", "ca. 3.5 ATP"],
            ["ca. 1.5 ATP", "ca. 0.5 ATP", "ca. 2.5 ATP", "ca. 3.5 ATP"],
            ["Enolase,", "Aldolase", "Pyruvatase", "Pyruvat-Dehydrogenase"],
            ["Hydratisierung von Fumarat zu Malat", "Die Fumarase katalysiert die Decarboxylierung von Isocitrat zu Alpha-Ketoglutarat", "Die Fumarase ist für die Synthese von Citrullin aus Ornithin und Carbamoylphosphat verantwortlich", "Die Fumarase spaltet das Citrat in Oxalacetat und Acetyl-CoA"],
            ["FAD", "NADH", "Acetyl-CoA", "Glucose"],
            ["Malat", "Fumarat", "a-Ketoglutarat", "Isocitrat"]
 
 
        ]
        correct_answers = [2, 0, 1, 2, 3, 0, 2, 0, 3, 0, 1, 2]  # Indices of correct answers for each question
 
    elif level.startswith("Hard"):
        questions = [
            "Welches Enzym des Citratzyklus, das FAD als Kofaktor enthält, ist gleichzeitig ein Bestandteil der mitochondrialen Atmungskette?",
            "Welches Intermediat des Citratzyklus kann zur Glukoneogenese genutzt werden?",
            "Wie viele Elektronen werden pro NADH in die Atmungskette eingespeist?",
            "Welches Enzym der Glykolyse katalysiert eine Reaktion, die auch in der Glukoneogenese vorkommt?",
            "Welche Verbindung entsteht bei der Decarboxylierung von a-Ketoglutarat im Citratzyklus?",
            "Welche Rolle spielt Ubiquinon (Coenzym Q) in der Atmungskette?"
 
        ]
        options = [
            ["Succinat-Dehydrogenase", "a-Ketoglutarat-Dehydrogenase", "Malat-Dehydrogenase", "Isocitrat-Dehydrogenase"],
            ["Isocitrat", "Oxalacetat", "Fumarat", "Succinat"],
            ["6 Elektronen", "2 Elektronen", "Keine Elektronen", "4 Elektronen"],
            ["Hexokinase", "Phosphofructokinase-1", "Pyruvatkinase", "Phosphoglycerat-Kinase"],
            ["Malat", "Fumarat", "Succinyl-CoA", "Acetyl-CoA"],
            ["Ubiquinon ist verantwortlich für die Produktion von Kohlendioxid in der Atmungskette", "Ubiquinon ist ein Enzym, das für die Umwandlung von Lichtenergie in ATP in der Atmungskette benötigt wird", "Ubiquinon dient dazu, Sauerstoff in der Atmungskette zu speichern", "Ubiquinon überträgt Elektronen von den Komplexen I und II zu Komplex III"]
 
        ]
        correct_answers = [0, 1, 1, 3, 2, 3]  # Indices of correct answers for each question
 
 
 
 
    # Rest of the code remains the same as yours
   
    user_answers = {}
    correct_count = 0
 
    # Display questions and radio buttons for selecting answers
    for index, (question, opts) in enumerate(zip(questions, options), start=1):
        st.subheader(f"{index}. {question}")
        selected_answer = st.radio("Choose the correct answer:", opts, key=index)
        user_answers[question] = selected_answer
 
    # Check answers button
    if st.button("Check answers"):
        correct_count = 0
        all_correct = True
        for i, (question, user_answer) in enumerate(user_answers.items()):
            correct_answer = options[i][correct_answers[i]]  # Get correct answer from options list
            st.subheader(f"{i+1}. {question}")
            if user_answer == correct_answer:
                st.write("Your answer is correct! ✅")
                correct_count += 1
            else:
                st.write("Your answer is incorrect. ❌")
                st.write(f"The correct answer is: {correct_answer}")
                all_correct = False
 
        if all_correct:
            st.balloons()
           
        st.write(f"You answered {correct_count} out of {len(questions)} questions correctly.")
 
if __name__ == "__main__":
         main()
