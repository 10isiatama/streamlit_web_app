import streamlit as st
from PIL import Image

st.title("title")
st.caption("caption")

image = Image.open("./datas/23_HBD_Splatoon_1920_1080.jpg")
st.image(image, width=200)