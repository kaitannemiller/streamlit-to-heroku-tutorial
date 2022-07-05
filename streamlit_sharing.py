
import streamlit as st
import gspread
import pandas as pd

gc = gspread.service_account(filename='./cred.json')
sheet1 = gc.open_by_url('https://docs.google.com/spreadsheets/d/1iudlYSDTvHLjEa0q04ebYmVnb8cV1xD7qJMUBj0rxFs/edit?usp=sharing')
sh = sheet1.get_worksheet(0)
df_gsheet = pd.DataFrame(data=sh.get_all_records())


st.set_page_config(page_title="BACHELOR BETS", page_icon="./rose.ico")
st.write("My First Streamlit Web App")

df = pd.DataFrame({"one": [1, 2, 3], "two": [4, 5, 6], "three": [7, 8, 9]})
st.write(df)

st.title("Connect to Google Sheets")
#gsheet_url = "https://docs.google.com/spreadsheets/d/1iudlYSDTvHLjEa0q04ebYmVnb8cV1xD7qJMUBj0rxFs/edit?usp=sharing"
#conn = gs.connect()
#rows = conn.execute(f'SELECT * FROM "{gsheet_url}"')
#df_gsheet = pd.DataFrame(rows)
st.write(df_gsheet)



st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

def my_widget(key):
    st.subheader('Hello there!')
    return st.button("Click me " + key)

# This works in the main area
clicked = my_widget("first")

# And within an expander
my_expander = st.expander("Expand", expanded=True)
with my_expander:
    clicked = my_widget("second")

# AND in st.sidebar!
with st.sidebar:
    clicked = my_widget("third")
