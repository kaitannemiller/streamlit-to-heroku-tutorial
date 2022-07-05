
import streamlit as st
import gspread
import pandas as pd

gc = gspread.service_account(filename='./cred.json')
sheet1 = gc.open_by_url('https://docs.google.com/spreadsheets/d/1iudlYSDTvHLjEa0q04ebYmVnb8cV1xD7qJMUBj0rxFs/edit?usp=sharing')
sh = sheet1.get_worksheet(0)
df_gsheet = pd.DataFrame(data=sh.get_all_records())


st.set_page_config(page_title="BACHELOR BETS", page_icon="./rose.ico", layout='wide')
padding = 0
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
.css-18e3th9 {
    background-color: grey;
    padding: 0rem 0rem 0rem 0rem;
    flex: 1 1 0%;
}
#root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) {
    flex: 1 1 0%;
    height: 100%;
}
div.stButton > button:first-child {
    background-color: #00cc00;
    color:white;
    font-size:20px;
    height:3em;
    width:100%;
}
#root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(7) {
    position: absolute;
    bottom: 0px;
}
.st-bd {border-style: none;}
.css-qri22k {
    font-size: 0px;
    padding: 0rem 0rem 0rem 0rem;
}
</style> """, unsafe_allow_html=True)



st.write("My First Streamlit Web App")

df = pd.DataFrame({"one": [1, 2, 3], "two": [4, 5, 6], "three": [7, 8, 9]})
st.write(df)

st.title("Connect to Google Sheets")
#gsheet_url = "https://docs.google.com/spreadsheets/d/1iudlYSDTvHLjEa0q04ebYmVnb8cV1xD7qJMUBj0rxFs/edit?usp=sharing"
#conn = gs.connect()
#rows = conn.execute(f'SELECT * FROM "{gsheet_url}"')
#df_gsheet = pd.DataFrame(rows)
st.write(df_gsheet)

def my_widget(key):
    return st.button("Click me " + key)

# And within an expander
my_expander = st.expander("Expand")
with my_expander:
    clicked = my_widget("second")

clicked2 = my_widget("third")
