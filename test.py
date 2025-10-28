import streamlit as st
import pandas as pd
class Table:
    def __init__(self, data):
        st.image(r"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMYjHrjikYhnIvKdjygdlHAYVCjwi1ZrXI9A&s")
        
        self.data = data
        if "data_df" not in st.session_state:
              st.session_state.data_df = pd.DataFrame(
        [{ "task": '' ,"Done?":False } ])
 
    def print_table(self):
      pass 
class Table:
    def __init__(self, data):
        self.data = data

    def print_table(self):
        for row in self.data:
            # طباعة كل خلية في الصف مع ترك مسافة
            print(" | ".join(map(str, row)))
table_data =  [{ "task": '' ,"Done?":False } ]

# # # # # # إنشاء كائن من الفئة Table
my_table = Table(table_data)

# # # # # # طباعة الجدول

my_table.print_table()











