import streamlit as st
from read_data import load_person_data, get_person_list

st.write("# EKG APP")
st.write("## Versuchsperson auswählen")

# Session State wird leer angelegt, solange er noch nicht existiert
if 'current_user' not in st.session_state:
    st.session_state.current_user = 'None'


st.write("Der Name ist: ", st.session_state.current_user)

# Funktionen aufrufen
person_names = get_person_list()


# Nutzen Sie ihre neue Liste anstelle der hard-gecodeten Lösung
st.session_state.current_user = st.selectbox(
    'Versuchsperson',
    options = person_names, key="sbVersuchsperson")

#streamlit run main.py