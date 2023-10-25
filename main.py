import streamlit as st
from PIL import Image
import pandas

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

st.text("")
st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
st.write("Here are a few projects that I've worked on:")

col3, col4 = st.columns(2)

data = pandas.read_csv("data.csv")

col3_data = data[:10]
col4_data = data[10:]

with col3:
    for index, row in col3_data.iterrows():
        st.header(row["title"])

with col4:
    for index, row in col4_data.iterrows():
        st.header(row["title"])

