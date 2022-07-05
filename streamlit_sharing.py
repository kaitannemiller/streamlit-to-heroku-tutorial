
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
.footer-custom {
    position: fixed;
    bottom: 0;
    width: 100%;
    color: black;
    font-size: 14px;
    height: 5rem;
    padding: 0rem 0rem 0rem 0rem;
    flex: 1 1 0%;
}
footer {
    position: static;
}
.css-18e3th9 {
    background-color: grey;
    padding: 0rem 0rem 0rem 0rem;
}
div.stButton > button:first-child {
    background-color: #00cc00;
    color:white;
    font-size:20px;
    min-height:3em;
    width:100%;
}
.footer-custom > div > div.stButton > button:first-child:active {
    background-color: #00cc00;
    color: black;
    font-size:30px;
    min-height:3em;
    width:100%;
}
.st-bd {border-style: none;}
.css-qri22k {
    font-size: 0px;
    padding: 5rem 0rem 0rem 0rem;
}
</style> """, unsafe_allow_html=True)

footer = """
    <div class="footer-custom">
        <div class="element-container css-bo0d43 e1tzin5v3"><div class="row-widget stButton">
            <button kind="primary" class="css-1cpxqw2 edgvbvh9" style="background-color: red; height: 5em;">Footer</button>
        </div></div>
    </div>
"""
st.markdown(footer, unsafe_allow_html=True)


#gsheet_url = "https://docs.google.com/spreadsheets/d/1iudlYSDTvHLjEa0q04ebYmVnb8cV1xD7qJMUBj0rxFs/edit?usp=sharing"
#conn = gs.connect()
#rows = conn.execute(f'SELECT * FROM "{gsheet_url}"')
#df_gsheet = pd.DataFrame(rows)
#st.write(df_gsheet)

# And within an expander
i = 0
while i < 7:
    my_expander = st.expander("Expand")
    with my_expander:
        clicked = st.button("Click me", key='button'+str(i))
    i = i + 1
