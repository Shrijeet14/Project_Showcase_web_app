import streamlit as st

import pandas as pd

st.set_page_config(layout="wide",
                   page_title="Project showcase web-app",
                   page_icon=":star:")

col1,col2=st.columns(2)

with col1 :
    st.image("images/mynew.png",use_column_width="always")
with col2 :
    st.title("SHRIJEET KUMAR")
    myinformation="""Hi, I am Shrijeet ! I am a Python Developer and this webapp i have created specially to show case all my projects that i have completed as well as my upcoming projects. I really hope you will love to see my projects . I have provided the source codes of my projects so you can go through it and suggest me changes using the 'contact me' option through your mail. Thanks to visit my works !!!!"""
    st.info(myinformation)

    

st.write("Below you can find  my apps . Feel free to contact me !!")


col3,empty_col,col4= st.columns([1.5,0.5,1.5])


df=pd.read_csv("data.csv",sep=";")


with col3 :
    for index , row in  df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[source code]({row['url']})")

with col4 :
    for index , row in  df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[source code]({row['url']})")