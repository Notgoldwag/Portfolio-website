import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    jai_img = Image.open("images/photo.png")
    jai_img = jai_img.resize((550,600))
    st.image(jai_img)

with col2:
    st.title("Jaisharan Ashok Kumar")
    about = """ Hey I am Jaisharan Ashok Kumar! I am dedicated computer science enthusiast driven by a profound passion for technology and innovation. 
    Through my portfolio, you'll discover a collection of projects that not only reflect my commitment to learning but also my creative spirit. 
    As I continue on this exciting journey, I look forward to sharing my experiences and achievements in the world of technology.
    """

    st.info(about)

