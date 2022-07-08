
import streamlit as st
import gspread
import pandas as pd
import streamlit_authenticator as stauth
import time
import base64
import yaml

st.set_page_config(page_title="BACHELOR BETS", page_icon="./rose.ico", layout='wide')


test = False
bet_i = 0
info_buttons = []
selection_buttons = []
first_visit = 1
def create_page(name):
    global bet_i
    global info_buttons
    global selection_buttons
    global first_visit

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
        font-size: 0px;
    }
    div.stButton > button:first-child {
        background-color: #D90429;
        color: white;
        font-size:18px;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(4) > div {
        height: 4.5rem;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(4) > div > div {
        height: 100%;
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        -webkit-align-items: center;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(4) > div > div > p {
        text-align: center;
        font-size: 28px;
        color: #333333;
        margin: 0px 0px 0px;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:not(.element-container):not(.resize-triggers):nth-child(n+12) {
        position: fixed;
        bottom: 0;
        width: 100%;
        color: black;
        font-size: 14px;
        height: 5rem;
        padding: 0rem 0rem 0rem 0rem;
        display: flex;
        flex-direction: row;
        flex: 1 1 0%;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:not(.element-container):not(.resize-triggers):nth-child(n+12) > div {
        display: flex;
        flex-direction: row;
        flex: 1 1 0%;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:not(.element-container):not(.resize-triggers):nth-child(n+12) > div > div {
        display: flex;
        flex-direction: row;
        flex: 1 1 0%;
        width: 33%;
        padding: 2px 2px 2px 2px;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:not(.element-container):not(.resize-triggers):nth-child(n+12) > div > div > div > button {
        background-color: #D90429;
        color: black;
        font-size:20px;
        min-height:0em;
        height:100%;
        width: 100%;
        padding: 2px 2px 2px 2px;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:not(.element-container):not(.resize-triggers):nth-child(n+12) > div > div > div > button:hover {
        background-color: #D90429;
        color: white;
        font-size:20px;
        min-height:0em;
        height:100%;
        width: 100%;
        padding: 2px 2px 2px 2px;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:not(.element-container):not(.resize-triggers):nth-child(n+12) > div > div > div > button:active {
        background-color: #D90429;
        color: black;
        font-size:20px;
        min-height:0em;
        height:100%;
        width: 100%;
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
    .ehezqtx6 {
        font-size: 8px;
        text-align: right;
    }
    .streamlit-expander {
        background-color: #F7F7F7;
        border-style: inset;
        line-height: 0.5;
        font-size: 0px;
    }
    .streamlit-expanderContent  {
        line-height: 0.5;
        font-size: 0px;
    }
    .streamlit-expanderContent > div  {
        width: 100%;
        display: flex;
        flex-direction: row;
        flex: 1 1 0%;
        line-height: 0.5;
        font-size: 0px;
    }
    .streamlit-expanderContent > div > div {
        display: flex;
        flex-direction: row;
        flex: 1 1 0%;
    }
    .streamlit-expanderContent > div > div > div  {
        display: flex;
        flex-direction: row;
        flex: 1 1 0%;
        width: 0%;
        padding: 0px 2px 0px 2px;
    }
    .streamlit-expanderContent > div > div > div:nth-child(1) {
        flex: 0 0 0%;
        width: 2.5rem;
    }
    .streamlit-expanderContent > div > div > div:nth-child(1) > div {
        display: flex;
        flex-direction: row;
        flex: 1 1 0%;
    }
    .streamlit-expanderContent > div > div > div:nth-child(1) > div > button {
        background-color: #456E44;
        flex: 1 1 0%;
    }
    .streamlit-expanderContent > div > div > div:nth-child(1) > div > button:hover {
        border-color: black;
        color: #333333;
    }
    .streamlit-expanderContent > div > div > div:nth-child(2) > div {
        display: flex;
        flex-direction: row;
        flex: 1 1 0%;
        align-items: center;
        -webkit-align-items: center;
        justify-content: right;
        padding-right: 3px;
    }
    .streamlit-expanderContent > div > div > div:nth-child(2) > div > div > p {
        font-size: 20px;
        font-weight: bold;
    }
    .streamlit-expanderContent > div > div > div:nth-child(3) > div {
        display: flex;
        flex-direction: row;
        flex: 1 1 0%;
        align-items: right;
        -webkit-align-items: right;
        justify-content: right;
    }
    .streamlit-expanderContent > div > div > div:nth-child(3) > div > button {
        font-size: 20px;
        background-color: #456E44;
        flex: 1 1 0%;
    }
    .streamlit-expanderContent > div > div > div:nth-child(3) > div > button:hover {
        border-color: black;
        color: #333333;
    }
    .st-ae {
        font-size: 20px;
    }
    .css-qri22k {
        font-size: 0px;
        padding: 4.95rem 0rem 0rem 0rem;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) {
        height: 100%;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(n+6) > div {
        border-style: outset;
        background-color: #F7F7F7;
        flex: 1 1 0%;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(n+6) > div > div > div > div > p {
        font-size: 20px;
        padding: 8px 8px 0rem 8px;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(6) > div > div > div > div > a {
        font-size: 20px;
        padding: 8px 0rem 0rem 8px;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(8) > div > div:nth-child(3) {
        display: flex;
        flex-direction: row;
        flex: 1 1 0%;
        align-items: flex-end;
        -webkit-align-items: flex-end;
        margin: 6px;
    }
    .stApp {
        background-color: white;
    }
    </style> """, unsafe_allow_html=True)



    file_ = open("rose.ico", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    header =f"""
        <div class="header-custom">
            <img src="data:image/gif;base64,{data_url}" alt="rose" height="40px" width="40px">
            {name}
            <img src="data:image/gif;base64,{data_url}" alt="rose" height="40px" width="40px">
        </div>
    """
    st.markdown(header, unsafe_allow_html=True)


    st.write("Week One")

    # And within an expander
    bet_titles = ["Gabby's First Impression Rose","Rachel's First Impression Rose","Week One Rose Ceremony","Number of Guys Sent Home","Most Popular Buzz Word"]
    bet_possiblecounts = [1,1,10,1,1]
    bet_info = ["Select the bachelor that you think will win Gabby's first impression rose. A correct guess wins 32 points.\n\n\nOdds: 1 in 32\n\nPossible Points: 32",
                "Select the bachelor that you think will win Rachel's first impression rose. A correct guess wins 32 points.\n\n\nOdds: 1 in 32\n\nPossible Points: 32",
                "Select 10 bachelors that you think will receive a rose in the first week. Ten correct guesses win 10 points each, nine correct guesses win 9 points each, and so on.\n\n\nOdds of 100 points: 1 in 64512239\n\nPossible Points: 100",
                "Select the number of bachelors that you think will be sent home in the first week. A correct guess wins 18 points.\n***This is a one guess per person bet. Make your selection quickly!***\n\n\nOdds: 1 in 6\n\nPossible Points: 18",
                "Select the phrase that you think will be said the most often in the first week. A correct guess wins 18 points.\n***This is a one guess per person bet. Make your selection quickly!***\n\n\nOdds: 1 in 6\n\nPossible Points: 18"]

    global bet_container
    global contestants_container
    global standings_container
    global info_container
    global selection_container
    global contestants_button
    global bets_button
    global standings_button
    bet_container = st.empty()
    contestants_container = st.empty()
    standings_container = st.empty()
    info_container = st.empty()
    selection_container = st.empty()
    def bet_container_go():
        global bet_i
        global bet_container
        global info_buttons
        global selection_buttons
        global test
        with bet_container.container():
            i = 0
            info_buttons = []
            selection_buttons = []
            while i < len(bet_titles):
                my_expander = st.expander(bet_titles[i])
                with my_expander:
                    info_buttons.append(st.button("ⓘ", key='infobutton'+str(bet_i)))
                    st.write("0 / " + str(bet_possiblecounts[i]) + " selected")
                    selection_buttons.append(st.button("Select", key='editbutton'+str(bet_i)))
                i = i + 1
                bet_i = bet_i + 1

        for b,button in enumerate(info_buttons):
            if button:
                bet_container.empty()
                contestants_container.empty()
                standings_container.empty()
                info_container.empty()
                selection_container.empty()
                info_container_go(b)

        for b,button in enumerate(selection_buttons):
            if button:
                bet_container.empty()
                contestants_container.empty()
                standings_container.empty()
                info_container.empty()
                selection_container.empty()
                selection_container_go(b)

        if standings_button:
            bet_container.empty()
            contestants_container.empty()
            standings_container.empty()
            info_container.empty()
            selection_container.empty()
            standings_container_go()
        if contestants_button:
            bet_container.empty()
            contestants_container.empty()
            standings_container.empty()
            info_container.empty()
            selection_container.empty()
            contestants_container_go()

    def contestants_container_go():
        global contestants_container
        with contestants_container.container():
            st.write("Coming Soon! \nFor now, you can look here: ")
            st.markdown(""" <a href="https://abc.com/shows/the-bachelorette/cast">Official ABC Website</a>
                        """, unsafe_allow_html=True)

    def standings_container_go():
        global standings_container
        with standings_container.container():
            st.write("Coming Soon")

    def info_container_go(b):
        global info_container
        with info_container.container():
            st.write("**"+bet_titles[b]+"**")
            st.write(bet_info[b])
            back_button = st.button("Back")

        if back_button:
            bet_container.empty()
            contestants_container.empty()
            standings_container.empty()
            info_container.empty()
            selection_container.empty()
            bet_container_go(b)


    def selection_container_go(b):
        global selection_container
        with selection_container.container():
            st.write("Coming Soon")


    placeholder1 = st.empty()
    placeholder2 = st.empty()
    placeholder3 = st.empty()
    placeholder4 = st.empty()
    placeholder5 = st.empty()
    #bet_container_go()

    button_container = st.empty()
    with button_container.container():
        contestants_button = st.button("Contestants", key='contestants_button')
        bets_button = st.button("Bets", key='bets_button')
        standings_button = st.button("Standings", key='standings_button')


    if standings_button:
        bet_container.empty()
        contestants_container.empty()
        standings_container.empty()
        info_container.empty()
        selection_container.empty()
        standings_container_go()
    if contestants_button:
        bet_container.empty()
        contestants_container.empty()
        standings_container.empty()
        info_container.empty()
        selection_container.empty()
        contestants_container_go()
    if bets_button or first_visit == 1:
        first_visit = 0
        bet_container.empty()
        contestants_container.empty()
        standings_container.empty()
        info_container.empty()
        selection_container.empty()
        bet_container_go()





gc = gspread.service_account(filename='./cred.json')
sheet1 = gc.open_by_url('https://docs.google.com/spreadsheets/d/1iudlYSDTvHLjEa0q04ebYmVnb8cV1xD7qJMUBj0rxFs/edit?usp=sharing')
sh = sheet1.get_worksheet(0)
df_gsheet = pd.DataFrame(data=sh.get_all_records())

with open('./cred.yaml') as file:
    config = yaml.safe_load(file)

for user in config['credentials']['usernames'].keys():
    config['credentials']['usernames'][user]['password'] = stauth.Hasher([config['credentials']['usernames'][user]['password']]).generate()[0]

authenticator = stauth.Authenticate(config['credentials'],'bachelor_bets','harrison',cookie_expiry_days=30)
name, authentication_status, username = authenticator.login('Login','main')
time.sleep(0.5)

if st.session_state['authentication_status']:
    #authenticator.logout('Logout', 'main')
    if st.session_state["name"] != None:
        name = st.session_state["name"].split(' ')[0]
        create_page(name)
elif st.session_state['authentication_status'] == False:
    st.error('Username/password is incorrect')
elif st.session_state['authentication_status'] == None:
    st.warning('Please enter your username and password.')
