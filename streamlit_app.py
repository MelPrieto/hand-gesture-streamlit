import streamlit as st
from hand_recognition import run_hand_recognition

st.title("Hand Recognition AI - Online")
st.write("Press the button to start the camera and hand recognition")

if st.button("Start Recognition"):
    run_hand_recognition()