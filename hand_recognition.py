import cv2
from cvzone.HandTrackingModule import HandDetector
import streamlit as st
from PIL import Image
import numpy as np


def run_hand_recognition():
    webcam = cv2.VideoCapture(0)
    detector = HandDetector(detectionCon=0.8, maxHands=2)

    stframe = st.empty()       # Area where the video will be displayed

    while True:
        success, image = webcam.read()
        if not success:
            st.error("Could not get the camera image.")
            break

        hands, image = detector.findHands(image)

        # Show numbers of hands detected
        cv2.putText(image, f"Handas: {len(hands)}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

        # Convert BGR to RGB to display it in Streamlit
        img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        stframe.image(img_rgb, channels="RGB")

        # Output if the Stremlit button is pressed
        if st.button("Stop"):
            break