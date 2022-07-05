
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
.css-k0sv6k {
    height: 5rem;
    background-color: transparent;
    border-style: outset;
}
.css-fk4es0.e8zbici1 {visibility: hidden;}
.header-custom {
    position: fixed;
    top: 0;
    width: 100%;
    color: black;
    font-size: 50px;
    height: 5rem;
    padding: 0rem 0rem 0rem 0rem;
    flex: 1 1 0%;
    background-color: #F7F7F7;
    text-align: center;
    font-family: Brush Script MT;
}
.e1tzin5v3 {
    width: 100%;
}
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
    padding: 5rem 0rem 0rem 0rem;
}
.e1tzin5v0 {
    gap: 0rem;
}
div.stButton > button:first-child {
    background-color: #00cc00;
    color:white;
    font-size:20px;
    min-height:3em;
    width:100%;
}
.footer-custom > div > div.stButton > button:first-child {
    background-color: #D90429;
    color: black;
    font-size:20px;
    min-height:0em;
    height:100%;
    width:100%;
}
.footer-custom > div > div.stButton > button:first-child:hover {
    background-color: #D90429;
    color: white;
    font-size:20px;
    min-height:0em;
    height:100%;
    width:100%;
}
.footer-custom > div > div.stButton > button:first-child:active {
    background-color: #D90429;
    color: black;
    font-size:20px;
    min-height:0em;
    height:100%;
    width:100%;
}
.st-bd {
    background-color: #D2D3D1;
    border-style: inset;
}
.css-qri22k {
    font-size: 0px;
    padding: 5rem 0rem 0rem 0rem;
}
</style> """, unsafe_allow_html=True)

footer = """
    <div class="footer-custom">
        <div class="element-container css-bo0d43 e1tzin5v3" style="height: 100%; display: flex; flex-direction: row; flex: 1 1 0%;">
            <div class="row-widget stButton" style="left: 0; width: 33.3%; padding: 3px 3px 3px 3px;"><button kind="primary" class="css-1cpxqw2 edgvbvh9 footer_button1">Footer1</button></div>
            <div class="row-widget stButton" style="width: 33.3%; padding: 3px 3px 3px 3px;"><button kind="primary" class="css-1cpxqw2 edgvbvh9 footer_button2">Footer2</button></div>
            <div class="row-widget stButton" style="right: 0;  width: 33.3%; padding: 3px 3px 3px 3px;"><button kind="primary" class="css-1cpxqw2 edgvbvh9 footer_button3">Footer3</button></div>
        </div>
    </div>
"""
st.markdown(footer, unsafe_allow_html=True)

import base64
file_ = open("rose.ico", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

name = "Claire"
header =f"""
    <div class="header-custom">
        <img src="data:image/gif;base64,{data_url}" alt="rose" height="40px" width="40px">
        {name}
        <img src="data:image/gif;base64,{data_url}" alt="rose" height="40px" width="40px">
    </div>
"""
st.markdown(header, unsafe_allow_html=True)


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
