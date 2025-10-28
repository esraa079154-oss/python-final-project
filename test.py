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
df =st.session_state.data_df 
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



# df = pd.DataFrame(
#     [
#         {"command": "st.selectbox", "rating": 4, "is_widget": True},
#         {"command": "st.balloons", "rating": 5, "is_widget": False},
#         {"command": "st.time_input", "rating": 3, "is_widget": True},
#     ]
# )

# st.dataframe(df, use_container_width=True)
# df = pd.DataFrame(
#     [
#         {"command": "st.selectbox", "rating": 4, "is_widget": False},
#         {"command": "st.balloons", "rating": 5, "is_widget": False},
#         {"command": "st.time_input", "rating": 3, "is_widget": False},
#     ]
# )

# edited_df = st.data_editor(df) # 👈 An editable dataframe

# favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
# st.markdown(f"Your favorite command is **{favorite_command}** 🎈")


# edited_df = st.data_editor(df) # 👈 An editable dataframe

# favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
# st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

# edited_df = st.data_editor(df, num_rows="dynamic")

# st.data_editor(df, key="my_key", num_rows="dynamic") # 👈 Set a key
# st.write("Here's the value in Session State:")
# st.write(st.session_state["my_key"]) # 👈 Show the value in Session State

# edited_list = st.data_editor(["red", "green", "blue"], num_rows= "dynamic")
# st.write("Here are all the colors you entered:")   
# st.write(edited_list)

# import numpy as np

# st.data_editor(np.array([
#  	["st.text_area", "widget", 4.92],
#  	["st.markdown", "element", 47.22]
# ]))

# st.data_editor([
#     {"name": "st.text_area", "type": "widget"},
#     {"name": "st.markdown", "type": "element"},
# ])

# import streamlit as st
# import pandas as pd

# df = pd.DataFrame(columns=['name','age','color'])
# colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
# config = {
#     'name' : st.column_config.TextColumn('Full Name (required)', width='large', required=True),
#     'age' : st.column_config.NumberColumn('Age (years)', min_value=0, max_value=122),
#     'color' : st.column_config.SelectboxColumn('Favorite Color', options=colors)
# }

# result = st.data_editor(df, column_config = config, num_rows='dynamic')

# import pandas as pd
# import streamlit as st
# from numpy.random import default_rng as rng

# df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])

# st.scatter_chart(df)

# my_chart = st.vega_lite_chart(
#     {
#         "mark": "line",
#         "encoding": {"x": "a", "y": "b"},
#         "datasets": {
#             "some_fancy_name": df,  # <-- named dataset
#         },
#         "data": {"name": "some_fancy_name"},
#     }
# )
# my_chart.add_rows(some_fancy_name=df)  # <-- name used as keyword

# import streamlit as st
# from datetime import datetime

# start_time = st.slider(
#     "When do you start?",
#     value=datetime(2020, 1, 1, 9, 30),
#     format="MM/DD/YY - hh:mm",
# )
# st.write("Start time:", start_time)

# st.title("🎈 My new app")
# st.title("🎈 My new Streamlit app")

# import numpy as np
# st.write("Here's our first attempt at using data to create a table:")
# st.write(pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# }))

# df

# dataframe = np.random.randn(10, 20)
# st.dataframe(dataframe)
# x = st.slider('x')  # 👈 this is a widget
# st.write(x, 'squared is', x * x)

# import streamlit as st

# st.title('Counter Example')
# count = 0

# increment = st.button('Increment')
# if increment:
#     count += 1

# st.write('Count = ', count)

# if 'key' not in st.session_state:
#     st.session_state['key'] = 'value'


# # Session State also supports the attribute based syntax
# st.title('Counter Example using Callbacks with args')
# if 'count' not in st.session_state:
#     st.session_state.count = 0

# increment_value = st.number_input('Enter a value', value=0, step=1)

# def increment_counter(increment_value):
#     st.session_state.count += increment_value

# # increment = st.button('Increment', on_click=increment_counter,
# #     args=(increment_value, ))

# # st.write('Count = ', st.session_state.count)

# st.title('Counter Example using Callbacks with kwargs')
# if 'count' not in st.session_state:
#     st.session_state.count = 0

# def increment_counter(increment_value=0):
#     st.session_state.count += increment_value

# def decrement_counter(decrement_value=0):
#     st.session_state.count -= decrement_value

# # st.button('Increment', on_click=increment_counter,
# # 	kwargs=dict(increment_value=5))

# st.button('Decrement', on_click=decrement_counter,
# 	kwargs=dict(decrement_value=1))

# st.write('Count = ', st.session_state.count)

# import streamlit as st

# # قائمة المهام
# tasks = ["مهمة 1", "مهمة 2", "مهمة 3", "مهمة 4", "مهمة 5"]

# # اختيار المهام المنجزة
# completed_tasks = st.multiselect("اختر المهام التي أنجزتها اليوم:", tasks)

# # حساب النسبة المئوية للإنجاز
# if tasks:
#     progress = len(completed_tasks) / len(tasks)
# else:
#     progress = 0

# # عرض شريط التقدم
# st.progress(progress, text=f"تم إنجاز {int(progress*100)}% من المهام")












