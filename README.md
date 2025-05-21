---
title: Hand Recognition App
emoji: 🖐️
colorFrom: indigo
colorTo: green
sdk: streamlit
sdk_version: "1.35.0"
app_file: streamlit_app.py
pinned: false
---


# Hand Gesture Recognition App

A simple web app built with **Streamlit** that uses your webcam to detect hand gestures in real-time using **cvzone** and **Opencv**.

## 🚀 Features

- Real-time webcam streaming.
- Hand detection using `cvzone.HandDetector`.
- Displays numbers of hands detected.
- Interactive UI with Streamlit.

## 📦 Technologies Used

- Python 3
- Streamlit
- OpenCV
- cvzone
- Numpy
- Pillow

## ▶️ Run Locally

To run the appon your local machine: 

```bash

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
pip install -r requirements.txt
streamlit run str