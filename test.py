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
if "data_df" not in st.session_state:
    st.session_state.data_df = pd.DataFrame(
        [{ "task": '' ,"Done?":False } ])
#df=pd.DataFrame(df)
df_with_row_numbers = st.session_state.data_df.reset_index(drop=False)
df_with_row_numbers.rename(columns={'index': 'task_num'}, inplace=True)
df_with_row_numbers['task_num'] = df_with_row_numbers['task_num'] + 1
edited_df = st.data_editor(df_with_row_numbers, num_rows="dynamic", hide_index=True)
if not edited_df.equals(df_with_row_numbers):
    st.session_state.data_df = edited_df.drop(columns=['task_num'])
st.divider()
st.write(st.session_state.data_df)
# df =st.session_state.data_df 
#num_row=len(df)
#if st.button("Add new row"):
    #new_counter_value =df["counter"].max()+1 
    # new_counter_value=st.session_state.data_df['counter'].max()+1
        
# df.insert(0,"num_row",range(1,1+len(df)))  
# st.dataframe(df,ues_container_width=True)
# range(0,len(df)+1)
# df.insert(0,"num_row",0)
# st.DataFrame(df)
if True:
    new_row_number=1 
else:
    new_row_number=st.session_state.data_df["task_num"].max()+1
# if "Done" not in df.columns:
#     df["Done?"] = False
#shoe table and modify estimation(percentage)
# edited_df = st.data_editor(df, num_rows="dynamic")
#calculate the ratio of achievement of tasks
if len(edited_df) > 0:
    completed = edited_df["Done?"].sum()
    total = len(edited_df)
    progress = completed / total
else:
    progress = 0
#estimation
st.progress(progress, text=f"The achievement equal to {int(progress*100)}% from all tasks")
st.set_page_config(page_title="To_Do_List",page_icon='🧾')
