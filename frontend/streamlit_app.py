import streamlit as st
import requests

st.title("📄 Automated OMR Evaluation")

uploaded_file = st.file_uploader("Upload OMR sheet", type=["jpg","png","jpeg"])

if uploaded_file is not None:
    files = {"file": uploaded_file}
    res = requests.post("http://127.0.0.1:8000/upload", files=files)
    st.json(res.json())
