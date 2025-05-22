import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import av
import cv2
from cvzone.HandTrackingModule import HandDetector

class HandRecognitionTransformer(VideoTransformerBase):
    def __init__(self):
        self.detector = HandDetector(detectionCon=0.8, maxHands=2)

    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        hands, img = self.detector.findHands(img)
        cv2.putText(img, f"Hands: {len(hands)}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)
        return img

def run_hand_recognition():
    
    if "recognition_started" not in st.session_state:
        st.session_state.recognition_started = False

    if not st.session_state.recognition_started:
        if st.button("Start Recognition", key="start_btn"):
            st.session_state.recognition_started = True
            st.experimental_rerun()
    else:
        st.write("🔍 Starting camera and hand recognition...")
        webrtc_streamer(
            key="hand-recognition",
            video_transformer_factory=HandRecognitionTransformer,
            media_stream_constraints={"video": True, "audio": False}
        )

