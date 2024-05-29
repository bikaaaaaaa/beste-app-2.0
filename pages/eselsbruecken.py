import streamlit as st
 
def main():
    st.title('Eselsbrücken')
 
    thema = st.selectbox('Wählen Sie ein Thema', ['DNA/Zelle', 'Aminosäure', 'Citratzyklus', 'Bissl Chemie', 'Fette', 'Vitamine', 'Immunsystem', 'Blutzellen'])
 
    if thema == 'DNA/Zelle':
        st.subheader('Eselsbrücken für DNA/Zelle')
        st.markdown('<span style="color:black; font-weight:bold;">1. Basen Unterscheidung:</span>', unsafe_allow_html=True)
        st.markdown('   - Purine: Adenin + Guanin = <span style="color:blue; font-weight:bold;">AG</span> – Arbeitsgemeinschaft (Ehepaar) -> Zwei Ringe halten zusammen / <span style="color:blue; font-weight:bold;">A</span>dolf + <span style="color:blue; font-weight:bold;">G</span>andhi', unsafe_allow_html=True)
        st.markdown('   - Pyrimidine: <span style="color:blue; font-weight:bold;">C</span>ytosin + <span style="color:blue; font-weight:bold;">T</span>hymin + <span style="color:blue; font-weight:bold;">U</span>racil = <span style="color:blue; font-weight:bold;">CT</span>-<span style="color:blue; font-weight:bold;">U</span>ntersuchung an der <span style="color:blue; font-weight:bold;">Pyramide</span>', unsafe_allow_html=True)
        st.markdown('<span style="color:black; font-weight:bold;">2. Basenpaarung:</span>', unsafe_allow_html=True)
        st.markdown('   - Bei der Basenpaarung kann man sich ein Auto vorstellen mit 4 (A, G, C, T/U) Reifen an zwei Achsen')
        st.markdown('   - Vordere Achse (<span style="color:blue; font-weight:bold;">G+C</span>) mit <span style="color:blue; font-weight:bold;">drei</span>facher Verstrebung (3x Wasserstoffbrücken)', unsafe_allow_html=True)
        st.markdown('   - Hintere Achse (<span style="color:blue; font-weight:bold;">A+T/U</span>) mit <span style="color:blue; font-weight:bold;">zwei</span>facher Verstrebung (2x Wasserstoffbrücken)', unsafe_allow_html=True)
        st.markdown('<span style="color:black; font-weight:bold;">3. Glykosylierung:</span>', unsafe_allow_html=True)
        st.markdown('   3.1 N kommt vor O im Alphabet:')
        st.markdown('   - Erst N-Glykosylierung, dann O-Glykosylierung')
        st.markdown('   3.2 E kommt vor G im Alphabet:')
        st.markdown('   - N-Glykosylierung am ER (endoplasmatisches Retikulum), O-Glykosylierung am Golgi Apparat')
        st.markdown('   3.3 A kommt vor S und T im Alphabet:')
        st.markdown('   - N-Glykosylierung an Asparaginresten, O-Glykosylierung an Serin- und Threoninresten')
        st.markdown('<span style="color:black; font-weight:bold;">4. Mitose:</span>', unsafe_allow_html=True)
        st.markdown('<span style="color:blue; font-weight:bold;">I</span>ch <span style="color:blue; font-weight:bold;">P</span>utze <span style="color:blue; font-weight:bold;">M</span>ein <span style="color:blue; font-weight:bold;">A</span>uto <span style="color:blue; font-weight:bold;">T</span>äglich', unsafe_allow_html=True)
        st.markdown('<span style="color:blue; font-weight:bold;">I</span>nterphase, <span style="color:blue; font-weight:bold;">P</span>rophase, <span style="color:blue; font-weight:bold;">M</span>etaphase, <span style="color:blue; font-weight:bold;">A</span>naphase, <span style="color:blue; font-weight:bold;">T</span>elophase', unsafe_allow_html=True)
 
    elif thema == 'Aminosäure':
        st.subheader('Eselsbrücken für Aminosäure')
        st.markdown('<span style="color:black; font-weight:bold;">1. Essentielle Aminosäuren:</span>', unsafe_allow_html=True)
        st.markdown('<span style="color:blue; font-weight:bold;">I</span>soldes <span style="color:blue; font-weight:bold;">t</span>rübe <span style="color:blue; font-weight:bold;">T</span>heorien <span style="color:blue; font-weight:bold;">m</span>achen <span style="color:blue; font-weight:bold;">L</span>eutnant <span style="color:blue; font-weight:bold;">V</span>alentin <span style="color:blue; font-weight:bold;">P</span>henomenal <span style="color:blue; font-weight:bold;">l</span>üstern.', unsafe_allow_html=True)
        st.markdown('-> <span style="color:blue; font-weight:bold;">I</span>soleucin <span style="color:blue; font-weight:bold;">T</span>ryptophan, <span style="color:blue; font-weight:bold;">T</span>hreonin, <span style="color:blue; font-weight:bold;">M</span>ethionin, <span style="color:blue; font-weight:bold;">L</span>eucin, <span style="color:blue; font-weight:bold;">V</span>alin, <span style="color:blue; font-weight:bold;">P</span>henylalanin, <span style="color:blue; font-weight:bold;">L</span>ysin', unsafe_allow_html=True)
        st.markdown('<span style="color:black; font-weight:bold;">ODER</span>', unsafe_allow_html=True)
        st.markdown('<span style="color:blue; font-weight:bold;">PheTTVILLM</span> (ausgesprochen Fettfilm)', unsafe_allow_html=True)
        st.markdown('<span style="color:blue; font-weight:bold;">Phe</span>nylalanin, <span style="color:blue; font-weight:bold;">T</span>hreonin, <span style="color:blue; font-weight:bold;">T</span>ryptophan, <span style="color:blue; font-weight:bold;">V</span>alin, <span style="color:blue; font-weight:bold;">I</span>soleucin, <span style="color:blue; font-weight:bold;">L</span>ysin, <span style="color:blue; font-weight:bold;">L</span>eucin, <span style="color:blue; font-weight:bold;">M</span>ethionin', unsafe_allow_html=True)
 
    elif thema == 'Citratzyklus':
        st.subheader('Eselsbrücken für Citratzyklus')
        st.markdown('<span style="color:black; font-weight:bold;">1. Für Zwischen Produkte:</span>', unsafe_allow_html=True)
        st.markdown('<span style="color:blue; font-weight:bold;">Z</span>itronen <span style="color:blue; font-weight:bold;">i</span>m <span style="color:blue; font-weight:bold;">K</span>oma <span style="color:blue; font-weight:bold;">s</span>ind <span style="color:blue; font-weight:bold;">s</span>uper <span style="color:blue; font-weight:bold;">f</span>ür <span style="color:blue; font-weight:bold;">m</span>eine <span style="color:blue; font-weight:bold;">O</span>ma', unsafe_allow_html=True)
        st.markdown('<span style="color:blue; font-weight:bold;">C</span>itrat, <span style="color:blue; font-weight:bold;">I</span>socitrat, <span style="color:blue; font-weight:bold;">K</span>etoglutarat, <span style="color:blue; font-weight:bold;">S</span>uccinyl-CoA, <span style="color:blue; font-weight:bold;">S</span>uccinat, <span style="color:blue; font-weight:bold;">F</span>umarat, <span style="color:blue; font-weight:bold;">M</span>alat, <span style="color:blue; font-weight:bold;">O</span>xalacetat', unsafe_allow_html=True)
    elif thema == 'Bissl Chemie':
        st.subheader('Eselsbrücken für Bissl Chemie')
        st.markdown('<span style="color:black; font-weight:bold;">1. Redoxreaktionen:</span>', unsafe_allow_html=True)
        st.markdown('Red<span style="color:blue; font-weight:bold;">uuuuu</span>ktion – A<span style="color:blue; font-weight:bold;">uuuuu</span>fnahme (Reduktion ist die Elektronena<span style="color:blue; font-weight:bold;">u</span>fnahme)', unsafe_allow_html=True)
        st.markdown('Oxid<span style="color:blue; font-weight:bold;">aaaaa</span>tion – <span style="color:blue; font-weight:bold;">Aaaaa</span>bgabe (Oxidation ist die Elektronen<span style="color:blue; font-weight:bold;">a</span>bgabe)', unsafe_allow_html=True)
 
    elif thema == 'Fette':
        st.subheader('Eselsbrücken für Fette')
        st.markdown('<span style="color:black; font-weight:bold;">1. Fettsäuren (Anzahl der Doppelbindungen):</span>', unsafe_allow_html=True)
        st.write('Ungesättigte Fettsäuren (Vokale = Anzahl Doppelbindungen):')
        st.write('Öl-säure (1)')
        st.write('Linol-säure (Li-nol = 2)')
        st.write('Linolen-säure (Li-no-len = 3)')
        st.write('Arachidon-säure (A-rach-i-don = 4)')
 
    elif thema == 'Vitamine':
        st.subheader('Eselsbrücken für Vitamine')
        st.markdown('<span style="color:black; font-weight:bold;">1. Fettlösliche Vitamine:</span>', unsafe_allow_html=True)
        st.write('EDeKA (wie der Supermarkt aus Deutschland) -> Vitamine A, D, E, K')
        st.markdown('<span style="color:black; font-weight:bold;">2. B Vitamine:</span>', unsafe_allow_html=True)
        st.write('The Right Night (for) Party, Pussy, Bitches, Fucking (and) Cocaine.')
        st.write('B1 -> Thiamin')
        st.write('B2 -> Riboflavin, FAD')
        st.write('B3 -> Niacin, NAD')
        st.write('B5 -> Pantothensäure')
        st.write('B6 -> Pyridoxin, PALP')
        st.write('B7 -> Biotin')
        st.write('B9 -> Folsäure')
        st.write('B12 -> Cobalamin')
 
    elif thema == 'Immunsystem':
        st.subheader('Eselsbrücken für Immunsystem')
        st.markdown('<span style="color:black; font-weight:bold;">1. Immunglobuline - Reihenfolge der Sezernierung:</span>', unsafe_allow_html=True)
        st.markdown('<span style="color:blue; font-weight:bold;">M</span>it <span style="color:blue; font-weight:bold;">D</span>ildo <span style="color:blue; font-weight:bold;">G</span>eht <span style="color:blue; font-weight:bold;">a</span>lles <span style="color:blue; font-weight:bold;">e</span>infacher', unsafe_allow_html=True)
        st.write('Ig: M -> D -> G -> A -> E')
        st.markdown('<span style="color:black; font-weight:bold;">2. Immunglobuline Gewicht:</span>', unsafe_allow_html=True)
        st.write('Med. AG')
        st.write('Ig: M > E > D > A > G')
        st.markdown('<span style="color:black; font-weight:bold;">3. MHC:</span>', unsafe_allow_html=True)
        st.markdown('MHC-I = Zusammensetzung der MHC-<span style="color:blue; font-weight:bold;">E</span>ins im <span style="color:blue; font-weight:bold;">E</span>ndoplasmatischen Retikulum', unsafe_allow_html=True)
        st.write('MHC-II = 2. Buchstabe im ABC ist B, somit sind MHC-II Komplexe auch auf B-Lymphos zu finden')
        st.markdown('<span style="color:black; font-weight:bold;">4. Mehr über Ig:</span>', unsafe_allow_html=True)
        st.write('IgA = A sieht aus wie eine 4 -> hat 4 Antigenbindungsstellen')
        st.markdown('<span style="color:black; font-weight:bold;">5. Muss immer 8 ergeben:</span>', unsafe_allow_html=True)
        st.write('MHC-II und CD4 = 2x4 = 8')
        st.write('MHC-I und CD8 = 1x8 = 8')
        st.markdown('<span style="color:black; font-weight:bold;">6. 2 Helfer 1 Killer:</span>', unsafe_allow_html=True)
        st.markdown('<span style="color:blue; font-weight:bold;">MHC-II</span> CD4 positive <span style="color:blue; font-weight:bold;">T-Helferzellen</span>', unsafe_allow_html=True)
        st.markdown('<span style="color:blue; font-weight:bold;">MHC-I</span> CD8 positive <span style="color:blue; font-weight:bold;">natürliche Killerzellen</span>', unsafe_allow_html=True)
        st.markdown('<span style="color:black; font-weight:bold;">7. CD:</span>', unsafe_allow_html=True)
        st.write('CD4 = Ich helfe dir')
        st.write('CD8 = gute Nacht (töten)')
 
    elif thema == 'Blutzellen':
        st.subheader('Eselsbrücken für Blutzellen')
        st.markdown('<span style="color:black; font-weight:bold;">1. Grösse der Blutzellen:</span>', unsafe_allow_html=True)
        st.write('(Von klein nach groß) -> Telygram')
        st.write('1. Thrombozyten')
        st.write('2. Erythrozyten')
        st.write('3. Lymphozyten')
        st.write('4. Granulozyten')
        st.write('5. Monozyten')
if __name__ == "__main__":
    main()
            

