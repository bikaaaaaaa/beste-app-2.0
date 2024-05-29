import streamlit as st

def main():
    st.title("BioPathways")

    pathways = {
        "Atmungskette": {
            "main_image": "images/atmungskette_main.jpg", 
            "stages": {
                1: ("Die wichtigsten Elektronenträger sind NADH + H+ (Nadel + 2-Haar-Helferlein) und FADH2 (Fadenspule + 2-Haar-Helferlein). Sie bekommen ihre Elektronen wiederum aus den katabolen Stoffwechselvorgängen wie bspw. der Beta-Oxidation, Glykolyse und Pyruvat-Dehydrogenase-Reaktion.", "images/at1.jpg"),
                2: ("Die gebrachten e- werden durch 4 Proteinkomplexe transportiert. Dieser elektrische Strom wird dann gebraucht um das Enzymkomplex zu betreiben. Was passiert nun?: Die Elektronen folgen einer sogennanten Spannungsreihe (unter Spannung stehende Brücke). Sie entsteht dadurch, dass verschiedene Moleküle unterschiedliche Redoxpotentiale (“Elektronen-Anziehungskraft”) besitzen. NADH + H+ bzw. FADH2 haben das geringste Redoxpotential (geringste 'Elektronen-Anziehungskraf'), Sauerstoff (O2) das höchste. Ergo wandern die Elektronen von NADH + H+ und FADH2 zu O2. (Brücken führen zum sauren Stoffwesen nach unten).", "images/at2.jpg"),
                3: ("Der Elektronen-Strom setzt die nötige Energie frei, um Protonen aktiv in den Intermembranraum der Mitochondrien zu pumpen. Das geschieht mittels der Enzymkomplexe. Der Transport ist deshalb aktiv, weil im Intermembranraum des Mitochondriums bereits ein Protonenüberschuss (H+) besteht. Dieser Protonenüberschuss erzeugt eine Potentialdifferenz zum Matrixraum (Zytosol des Mitochondriums). Diese Potentialdifferenz ist schließlich die treibende Kraft für die ATP-Synthase.", "images/at3.jpg"),
                4: ("Im 4. Schritt synthetisiert die ATP-Synthase das wertvolle ATP, den wichtigsten Energieträger unseres Körpers. Wichtig: Die ATP-Synthase ist streng genommen nicht teil der Atmungskette. Die Atmungskette bereitet alles für die ATP-Synthase vor (Prononengradienten).", "images/at4.jpg"),
                5: ("Komplex I: NADH + H+ gibt in der Redoxreaktion seine Elektronen in „Begleitung” seiner Protonen an Flavinmononucleotid (FMN) ab. NADH + H+ wird dabei zu NAD+ oxidiert. Das FMN wird auch reduziert zu FMNH2. Nun werden die Elektronen vom FMNH2 auf das Coenzym Q (Ubichinon) übertragen. Das Ubichinon wird zu Ubichinol reduziert. Durch diese Reaktion vom Komplex I werden 4 H+ in der Intermembranraum rausgepumpt!", "images/at5.jpg"),
                6: ("Komplex II: Unsere Elektronenquelle hier ist der Succinat vom Citratzyklus. Succinat wird durch das Succinat-Dehydrogenase zu Fumarat oxidiert. Gleichzeitig werden 2 H+ vom Succinat entnommen und auf dem FAD übertragen -> FADH2. Dieser wiederum überträgt die 2 H+ aufs Coenzym Q. Komplex II hat keine Protonenpumpe, heisst das hier auch keine Protonen rausgepumpt werden.", "images/at6.jpg"),
                7: ("Komplex III: Das Ubichinol von den ersten zwei Komplexe übertragen nun 2 Elektronen an 2 Cytochrom C Moleküle. Wichtig: 1 Ubichinol überträgt 2 Elektronen! Durch die Reaktion vom Komplex III werden 4 Protonen raus gepumpt.", "images/at7.jpg"),
                8: ("Komplex IV: Schließt Knallgasreaktion ab. Formal gesehen wird ATP in einer Knallgas-Reaktion gewonnen (2 H2 + O2 → 2 H20). Jedoch würde dieser stark exotherme Prozess Zellen zerstören, wenn er ohne Modifizierung stattfinden würde. Er findet daher über einige Schritte der Atmungskette verteilt statt. Beim vierten Komplex ist die Knallgas-Reaktion komplett. Wie?: Das reduzierte Cytochrom C mit ihren erhaltenen e- von vorher, werden nun oxidiert (es gibt seine Elektronen aufs O2 ab.) Good to know: O2 hat das höchste Redoxpotential in dieser Reaktionsreihe, d.h. die Elektronen wandern zu O2. Durch die Reaktion vom Komplex IV, werden 2 Protonen rausgepumpt.", "images/at8.jpg"),
                9: ("Komplex V: Komplex V ist NICHT Teil der Elektronentransportkette und beinhaltet keine Redoxreaktionen. Er nutzt nur das durch die Komplexe I - IV entstandene Membranpotential, um ATP zu produzieren. Hier werden nur nicht mehr Protonen herausgepumpt, sondern durch das Protonenüberschuss im intermembran, werden die Protonen wieder ins Matrixinnenraum gedrängt. Mit dieser protonenmotorischen Kraft wird Energie erzeugt. Oxidative Phosphorylierung: ADP + Pi → ATP", "images/at9.jpg"),
                10: ("Energiebilanz: Es wird 3 Protonen pro ATP benötigt. Achtung! Die 3 gilt nur für die ATP-Synthase: Insgesamt sind 4 Protonen pro ATP-Synthese nötig. 1 Proton muss in den Transport von anorganischem Phosphat durch die innere Mitochondrienmembran investiert werden. Pro oxidiertem NADH + H+ fließen 10 Protonen in den Intermembranraum. Die Produktion eines ATP-Moleküls braucht 4 Protonen. Es entstehen also ca. 2,5 ATP pro Durchlauf.", "images/at10.jpg"),
            }
        },
        "Citratzyklus": {
            "main_image": None,
            "stages": {
                1: ("Coming soon", None)
            }
        }
    }

    selected_pathway = st.sidebar.selectbox("Wähle einen Pfad aus:", list(pathways.keys()))

    if selected_pathway == "Citratzyklus":
        st.image("images/soon.jpg", use_column_width=True)
        st.markdown("<h1 style='text-align: center; font-family: Arial, sans-serif; font-size: 36px;'>Coming soon</h1>", unsafe_allow_html=True)
    if selected_pathway == "Atmungskette":
        st.image(pathways[selected_pathway]["main_image"], caption=selected_pathway, use_column_width=True, width=1000)
        st.markdown("<p style='text-align: center; font-family: Arial, sans-serif; font-size: 14px; color: #666; position: fixed; bottom: 10px; left: 50%; transform: translateX(-50%);'>Inspired by <a href='https://meditricks.de' target='_blank' style='color: #666; text-decoration: none;'>meditricks.de</a></p>", unsafe_allow_html=True)

        current_stage_index = st.empty()
        stage_description = st.empty()
        stage_image = st.empty()

        if "current_stage" not in st.session_state:
            st.session_state.current_stage = 1

        def update_stage(action):
            if action == "next" and st.session_state.current_stage < len(pathways[selected_pathway]["stages"]):
                st.session_state.current_stage += 1
            elif action == "prev" and st.session_state.current_stage > 1:
                st.session_state.current_stage -= 1

            current_stage = pathways[selected_pathway]["stages"].get(st.session_state.current_stage)
            if current_stage:
                stage_image.image(current_stage[1], caption=f"Schritt {st.session_state.current_stage}", use_column_width=True)
                stage_description.write(current_stage[0])

        update_stage(None)

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Vorheriger Schritt", key="prev"):
                update_stage("prev")

        with col2:
            if st.button("Nächster Schritt", key="next"):
                update_stage("next")

    # Add images at the bottom in a row without captions
    if selected_pathway == "Atmungskette":
        additional_images = [
            "images/at.z1.jpg",
            "images/at.z2.jpg",
            "images/at.z3.jpg",
            "images/at.z4.jpg",
            "images/at.z5.jpg",
            "images/at.z6.jpg",
        ]

        # Divide the images into two rows
        row1, row2 = st.columns(2)

        # Populate the first row
        for img in additional_images[:3]:
            row1.image(img, use_column_width=True)

        # Populate the second row
        for img in additional_images[3:]:
            row2.image(img, use_column_width=True)

if __name__ == "__main__":
    main()











