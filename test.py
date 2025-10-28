import streamlit as st
import pandas as pd
df = pd.DataFrame(
    [
        { "task": "" ,"Done?":False} ])
class intro_table:
    st.set_page_config(layout="wide")
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
    
 
    def print_table(self):
      pass
        
class Table:
    
    def __init__(self, data):
    #st.image(r"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMYjHrjikYhnIvKdjygdlHAYVCjwi1ZrXI9A&s")
        self.data = data
    if "data_df" not in st.session_state:
          st.session_state.data_df = pd.DataFrame(
    [{ "task": '' ,"Done?":False } ])
    df=pd.DataFrame(df)
    df_with_row_numbers = st.session_state.data_df.reset_index(drop=False)
    df_with_row_numbers.rename(columns={'index': 'task_num'}, inplace=True)
    df_with_row_numbers['task_num'] = df_with_row_numbers['task_num'] + 1
    edited_df = st.data_editor(df_with_row_numbers, num_rows="dynamic", hide_index=True)
    if not edited_df.equals(df_with_row_numbers):
        st.session_state.data_df = edited_df.drop(columns=['task_num'])
    st.divider()
    if True:
        new_row_number=1 
    else:
        new_row_number=st.session_state.data_df["task_num"].max()+1
    if len(edited_df) > 0:
        completed = edited_df["Done?"].sum()
        total = len(edited_df)
        progress = completed / total
    else:
        progress = 0 
    def print_table(self):
        for row in self.data:
            # طباعة كل خلية في الصف مع ترك مسافة
            print(" | ".join(map(str, row))) 
    my_est=estimation(progress)
    st.progress(progress, text=f"The achievement equal to {int(progress*100)}% from all tasks")
    st.set_page_config(page_title="To_Do_List",page_icon='🧾')

class estimation :
    def __init__(self,progress): 
        self.progress=progress
        st.progress(progress, text=f"The achievement equal to {int(progress*100)}% from all tasks")
table_data =  [{ "task": '' ,"Done?":False } ]

# # # # # # إنشاء كائن من الفئة Table
my_table = Table(table_data)

# # # # # # طباعة الجدول

my_table.print_table()





































