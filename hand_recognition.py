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
    st.info("Camera and hand recognition starting...")
    webrtc_streamer(
        key="hand-recognition",
        video_transformer_factory=HandRecognitionTransformer,
        media_stream_constraints={"video": True, "audio": False}
    )

