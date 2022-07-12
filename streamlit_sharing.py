
import streamlit as st
import gspread
import pandas as pd
import streamlit_authenticator as stauth
import time
import base64
import yaml

st.set_page_config(page_title="BACHELOR BETS", page_icon="./rose.ico", layout='wide')


test = False
info_buttons = []
selection_buttons = []
save_button = False
cancel_button = False
first_visit = 1
bet_i = 0
if 'visit_flag' not in st.session_state:
    st.session_state["visit_flag"] = 0
def create_page(name,username):
    global bet_i
    global info_i
    global info_buttons
    global selection_buttons
    global save_button
    global cancel_button
    global first_visit
    global df_gsheet

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
        font-size: 45px;
        height: 5rem;
        line-height: 5rem;
        padding: 0rem 0rem 0rem 0rem;
        flex: 1 1 0%;
        background-color: #F7F7F7;
        text-align: center;
        justify-content: center;
        align-items: center;
        font-family: Norican;
    }
    .header-custom > img {
        margin: auto;
        vertical-align: auto;
        padding-top: 6px;
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
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:not(.element-container):not(.resize-triggers):nth-child(n+13) {
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
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:not(.element-container):not(.resize-triggers):nth-child(n+13) > div {
        display: flex;
        flex-direction: row;
        flex: 1 1 0%;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:not(.element-container):not(.resize-triggers):nth-child(n+13) > div > div {
        display: flex;
        flex-direction: row;
        flex: 1 1 0%;
        width: 33%;
        padding: 2px 2px 2px 2px;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:not(.element-container):not(.resize-triggers):nth-child(n+13) > div > div > div > button {
        background-color: #D90429;
        color: black;
        font-size:20px;
        min-height:0em;
        height:100%;
        width: 100%;
        padding: 2px 2px 2px 2px;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:not(.element-container):not(.resize-triggers):nth-child(n+13) > div > div > div > button:hover {
        background-color: #D90429;
        color: white;
        font-size:20px;
        min-height:0em;
        height:100%;
        width: 100%;
        padding: 2px 2px 2px 2px;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:not(.element-container):not(.resize-triggers):nth-child(n+13) > div > div > div > button:active {
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
        justify-content: flex-end;
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
        background-color: #F7F7F7 !important;
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
        margin: 6px 6px 0px;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(9) > div {
        padding: 0px 6px 0px 6px;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(9) > div > div:nth-child(1) {
        padding: 0px 6px 0px 6px;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(9) > div > div:nth-child(1) > div {
        padding: 6px 0px 6px 0px;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(9) > div > div:nth-child(1) > div > div:nth-child(3) {
        position: absolute;
        bottom: 6px;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(9) > div > div:nth-child(1) > div > div:nth-child(3) > div {
        display: flex;
        flex: 1 1 0%;
        justify-content: flex-end;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(9) > div > div:nth-child(1) > div > div:nth-child(3) > div > button {
        display: flex;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(9) > div > div > div > div > div > label {
        font-size: 20px;
        font-weight: bold;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(9) > div > div:nth-child(3) {
        position: absolute;
        bottom: 6px;
        left: 6px;
        flex: 0 0 0%;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(9) > div > div:nth-child(3) {
        width: 0px !important;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(9) > div > div:nth-child(2) > div {
        width: 0%;
        flex: 0 0 0%;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(9) > div > div:nth-child(2) > div > div {
        width: 0%;
        flex: 0 0 0%;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(9) > div > div:nth-child(2) > div > div > div {
        width: 0px !important;
        flex: 0 0 0%;
    }
    .stApp {
        background-color: white;
    }
    </style>
    <link href='https://fonts.googleapis.com/css?family=Norican' rel='stylesheet' type='text/css'>
    """, unsafe_allow_html=True)



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
                "Select the number of bachelors that you think will be sent home in the first week. A correct guess wins 18 points.\nThis bet is ***one guess per person. Make your selection quickly!***\n\n\nOdds: 1 in 6\n\nPossible Points: 18",
                "Select the phrase that you think will be said the most often in the first week. A correct guess wins 18 points.\nThis bet is ***one guess per person. Make your selection quickly!***\n\n\nOdds: 1 in 6\n\nPossible Points: 18"]

    global bet_container
    global contestants_container
    global standings_container
    global info_container
    global selection_container
    global contestants_button
    global bets_button
    global standings_button
    global save_button
    global cancel_button
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
        global save_button
        global cancel_button
        global myselectbox
        global test
        global form
        save_button = False
        myselectbox = ""
        with bet_container.container():
            i = 0
            info_buttons = []
            selection_buttons = []
            while i < len(bet_titles):
                my_expander = st.expander(bet_titles[i])
                with my_expander:
                    info_buttons.append(st.button("ⓘ", key='infobutton'+str(i)))
                    curr_count = len(df_gsheet[(df_gsheet["Username"]==username)&(df_gsheet["Week"]==1)&(df_gsheet["Question"]==i+1)])
                    st.write(str(curr_count)+" / " + str(bet_possiblecounts[i]) + " selected")
                    selection_buttons.append(st.button("Select", key='editbutton'+str(i)))
                i = i + 1

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
                st.session_state["visit_flag"] = b+1
                selection_container_go(b)
                # if save_button:
                #     st.write(myselectbox)
                #     if str(myselectbox).find('*') > -1:
                #         #st.error("This selection is already taken. Please choose another.")
                #         bet_container.empty()
                #         contestants_container.empty()
                #         standings_container.empty()
                #         info_container.empty()
                #         selection_container.empty()
                #         bet_container_go()
                #     else:
                #         total = len(df_gsheet)+2
                #         if b == 2:
                #             for s, select in enumerate(myselectbox):
                #                 sh.update_cell(total+s,1,1)
                #                 sh.update_cell(total+s,2,b+1)
                #                 sh.update_cell(total+s,3,username)
                #                 sh.update_cell(total+s,4,select)
                #         else:
                #             sh.update_cell(total,1,1)
                #             sh.update_cell(total,2,b+1)
                #             sh.update_cell(total,3,username)
                #             sh.update_cell(total,4,myselectbox)
                #         bet_container.empty()
                #         contestants_container.empty()
                #         standings_container.empty()
                #         info_container.empty()
                #         selection_container.empty()
                #         bet_container_go()


        if standings_button:
            bet_container.empty()
            contestants_container.empty()
            standings_container.empty()
            info_container.empty()
            selection_container.empty()
            st.session_state['visit_flag'] = 0
            standings_container_go()
        if contestants_button:
            bet_container.empty()
            contestants_container.empty()
            standings_container.empty()
            info_container.empty()
            selection_container.empty()
            st.session_state['visit_flag'] = 0
            contestants_container_go()


    def cancel_button_func():
        bet_container.empty()
        contestants_container.empty()
        standings_container.empty()
        info_container.empty()
        selection_container.empty()
        st.session_state['visit_flag'] = 0
        bet_container_go()

    def save_button_func(selec, b):
        total = len(df_gsheet)+2
        if b == 2:
            for s, select in enumerate(selec):
                sh.update_cell(total+s,1,1)
                sh.update_cell(total+s,2,b+1)
                sh.update_cell(total+s,3,username)
                sh.update_cell(total+s,4,select)
        else:
            sh.update_cell(total,1,1)
            sh.update_cell(total,2,b+1)
            sh.update_cell(total,3,username)
            sh.update_cell(total,4,selec)
        bet_container.empty()
        contestants_container.empty()
        standings_container.empty()
        info_container.empty()
        selection_container.empty()
        st.session_state["visit_flag"] = 0
        #bet_container_go()


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
        global info_i
        with info_container.container():
            st.write("**"+bet_titles[b]+"**")
            st.write(bet_info[b])
            if "info_i" not in st.session_state:
                st.session_state["info_i"] = 0
            info_i = st.session_state["info_i"] + 1
            st.session_state["info_i"] = info_i
            back_button = st.button("Back", key="infobackbutton"+str(info_i))

        if back_button:
            bet_container.empty()
            contestants_container.empty()
            standings_container.empty()
            info_container.empty()
            selection_container.empty()
            st.session_state["visit_flag"] = 0
            bet_container_go()


    def selection_container_go(b):
        global save_button
        global cancel_button
        global selection_container
        with selection_container.container():
            choices = []
            if b == 0 or b == 1 or b == 2:
                choices = ["Alec","Aven","Brandan","Chris","Colin","Erich","Ethan","Hayden","Jacob","James","Jason","Joey","John","Johnny",
                        "Jordan H.","Jordan V.","Justin B.","Justin Y.","Kirk","Logan","Mario","Matt","Michael","Nate","Quincey","Roby","Ryan","Spencer","Termayne","Tino","Tyler","Zach"]
            if b == 3:
                choices = [5,6,7,8,9,10]
                for c,choice in enumerate(choices):
                    if len(df_gsheet[(df_gsheet["Week"]==1)&(df_gsheet["Question"]==b+1)&(df_gsheet["Choice"]==choice)]) > 0:
                        usertemp=df_gsheet[(df_gsheet["Week"]==1)&(df_gsheet["Question"]==b+1)&(df_gsheet["Choice"]==choice)]["Username"].to_string(index=False)
                        choices[c] = str(choices[c]) + "    *" + config['credentials']['usernames'][usertemp]["name"].split(" ")[0] + "*"
            if b == 4:
                choices = ["the right reasons","journey","connection","open and honest","group of guys","chemistry"]
                for c,choice in enumerate(choices):
                    if len(df_gsheet[(df_gsheet["Week"]==1)&(df_gsheet["Question"]==b+1)&(df_gsheet["Choice"]==choice)]) > 0:
                        usertemp=df_gsheet[(df_gsheet["Week"]==1)&(df_gsheet["Question"]==b+1)&(df_gsheet["Choice"]==choice)]["Username"].to_string(index=False)
                        choices[c] = str(choices[c]) + "    *" + config['credentials']['usernames'][usertemp]["name"].split(" ")[0] + "*"


            with st.container() as form:
            #with st.form(key="selectbox") as form:
                if b == 2:
                    myselectbox = st.multiselect(bet_titles[b], choices, [])
                else:
                    myselectbox = st.selectbox(bet_titles[b], choices, key="selectbox"+str(b))

                if str(myselectbox).find("*") == -1:
                    st.write("You have selected: " + str(myselectbox))
                else:
                    st.write("This selection is unavailable. Please make another selection.")
                save_button = st.button("Save and Close", on_click=save_button_func, args=[myselectbox,b])

            with st.container():
                cancel_button = st.button("Cancel", on_click=cancel_button_func)




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


    if st.session_state['visit_flag'] == 0:
        st.legacy_caching.clear_cache()
        bet_container_go()
    elif standings_button:
        bet_container.empty()
        contestants_container.empty()
        standings_container.empty()
        info_container.empty()
        selection_container.empty()
        st.session_state["visit_flag"] = 0
        standings_container_go()
    elif contestants_button:
        bet_container.empty()
        contestants_container.empty()
        standings_container.empty()
        info_container.empty()
        selection_container.empty()
        st.session_state["visit_flag"] = 0
        contestants_container_go()
    elif bets_button:
        first_visit = 0
        bet_container.empty()
        contestants_container.empty()
        standings_container.empty()
        info_container.empty()
        selection_container.empty()
        st.session_state["visit_flag"] = 0
        bet_container_go()
    elif st.session_state["visit_flag"] > 0:
        selection_container_go(st.session_state["visit_flag"]-1)
        st.legacy_caching.clear_cache()



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
        username = st.session_state["username"]
        create_page(name,username)
elif st.session_state['authentication_status'] == False:
    st.error('Username/password is incorrect')
elif st.session_state['authentication_status'] == None:
    st.warning('Please enter your username and password.')
