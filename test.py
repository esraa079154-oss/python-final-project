import streamlit as st
import pandas as pd
#image at begin ofweb application
st.image(r"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMYjHrjikYhnIvKdjygdlHAYVCjwi1ZrXI9A&s")
#header
st.header("To_do_list")
st.header("")
#above the box of name 
user_name=st.text_input(" 👉 Please enter your name : ")
if user_name:
    st.write(f"Welcome {user_name} ")
    
st.subheader("The plan ")
st.image(r"https://emojiat.com/assets/img/emoji/1f4cb.png")
#create table and insert two columns 
df = pd.DataFrame(
    [
        { "task": "" ,"Done?":False} ])
#to increase the width of bage
st.set_page_config(layout="wide")
