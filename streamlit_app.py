import streamlit as st
from hand_recognition import run_hand_recognition

st.set_page_config(page_title="Hands Recognition AI", layout="centered")

st.title("Hand Recognition AI - Online")
st.write("Press the button to start the camera and hand recognition")

# This button controls wheher the function is called or not 
start = st.button("Start Recognition", key="start_button")

# This calls the function only when the button is pressed.
if start:
    run_hand_recognition()