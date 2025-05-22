import streamlit as st
from hand_recognition import run_hand_recognition

st.title("Hand Recognition AI - Online")
st.write("Press the button to start the camera and hand recognition")

if "start" not in st.session_state:
    st.session_state.start = False

if not st.session_state.start:
    if st.button("Start Recognition"):
        st.session_state.start = True

if st.session_state.start:
    run_hand_recognition()


