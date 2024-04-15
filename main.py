import streamlit as st
from read_data import load_person_data, get_person_list, find_person_data_by_name
from PIL import Image

st.write("# EKG APP")
st.write("## Versuchsperson auswählen")

# Session State wird leer angelegt, solange er noch nicht existiert
if 'current_user' not in st.session_state:
    st.session_state.current_user = 'None'

# Funktionen aufrufen
person_names = get_person_list()

# Nutzen Sie ihre neue Liste anstelle der hard-gecodeten Lösung
st.session_state.current_user = st.selectbox(
    'Versuchsperson',
    options = person_names, key="sbVersuchsperson")
st.write("Der Name ist: ", st.session_state.current_user)

# Laden eines Bilds
person = find_person_data_by_name(st.session_state.current_user)
image = Image.open(person["picture_path"])
# Anzeigen eines Bilds mit Caption
st.image(image, caption=st.session_state.current_user)


#streamlit run main.py