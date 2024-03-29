
import streamlit as st
import gspread
import pandas as pd
import streamlit_authenticator as stauth
import time
import datetime
import base64
import yaml
from PIL import Image
import pytz

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



def week_back_button_func(week):
    st.session_state['week'] = week - 1

def week_forward_button_func(week):
    st.session_state['week'] = week + 1

def create_page(name,username):
    global bet_i
    global info_i
    global info_buttons
    global selection_buttons
    global save_button
    global cancel_button
    global first_visit
    global df_gsheet
    global thisweek
    global submitweek

    # And within an expander
    # get max week that is labeled ready
    # get week that is currently in the submit window
    week = st.session_state["week"]
    weekname = qconfig["weeks"][str(week)]["weekname"]
    bet_titles = [qconfig["weeks"][str(week)]["bets"][x]["title"] for x in qconfig["weeks"][str(week)]["bets"]]
    bet_possiblecounts = [qconfig["weeks"][str(week)]["bets"][x]["possiblecount"] for x in qconfig["weeks"][str(week)]["bets"]]
    bet_info = [qconfig["weeks"][str(week)]["bets"][x]["info"] for x in qconfig["weeks"][str(week)]["bets"]]
    bet_choices = [list(qconfig["weeks"][str(week)]["bets"][x]["choices"]) for x in qconfig["weeks"][str(week)]["bets"]]
    bet_types = [qconfig["weeks"][str(week)]["bets"][x]["type"] for x in qconfig["weeks"][str(week)]["bets"]]
    bet_choicestypes = [qconfig["weeks"][str(week)]["bets"][x]["choicestype"] for x in qconfig["weeks"][str(week)]["bets"]]
    bet_textprefixes = [qconfig["weeks"][str(week)]["bets"][x]["textprefixes"] for x in qconfig["weeks"][str(week)]["bets"]]
    bet_textsuffixes = [qconfig["weeks"][str(week)]["bets"][x]["textsuffixes"] for x in qconfig["weeks"][str(week)]["bets"]]


    i = 0
    children = []
    while i < len(bet_titles):
        if bet_types[i] == "main":
            children.append(".e1s6o5jp0:nth-of-type(" + str(i+1) + ") > .streamlit-expander")
        i = i + 1
    style = f"""<style>

        {', '.join(children)} {{
            background-color: #BFBFBF; }}

    </style>"""

    style2 = ''
    if week == 1:
        style2 = """<style>

            #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(4) > div > div:nth-child(1) > div,
            #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(4) > div > div:nth-child(1) > div > button {
                height: 0px; width: 0px !important; visibility: hidden; }

        </style>"""
    if week == qconfig["weeks"][thisweek]["week"]:
        style2 = """<style>

            #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(4) > div > div:nth-child(3) > div,
            #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(4) > div > div:nth-child(3) > div > button {
                height: 0px; width: 0px !important; visibility: hidden; }

        </style>"""

    st.markdown(""" <style>
    #MainMenu {visibility: hidden;}
    .css-k0sv6k {
        height: 5rem;
        background-color: transparent;
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
        border-style: outset;
    }
    .header-custom > img {
        margin: auto;
        vertical-align: baseline;
        padding-top: 6px;
    }
    .e8zbici0 {
        flex-direction: column;
    }
    .e8zbici0 > div > div {
        display: flex;
        flex-direction: column;
        height: 100%;
    }
    .e8zbici0 > div > div > label {
        display: flex;
        flex-direction: column;
        font-size: 12px;
    }
    .e1tzin5v3 {
        font-size: 0px;
    }
    div.stButton > button:first-child {
        background-color: #D90429;
        color: white;
        font-size:18px;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(4)  {
        height: 4.5rem;
        flex: unset !important;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(4) > div {
        height: 4.5rem;
        flex-direction: row;
        flex: unset;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(4) > div > div {
        display: flex;
        flex: 1 1 0%;
        justify-content: center;
        align-items: center;
        -webkit-align-items: center;
        background-color: white;
        overflow-wrap: normal;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(4) > div > div > div {
        width: auto !important;
        text-align: center;
        color: #333333;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(4) > div > div > div > div > p {
        text-align: center;
        font-size: 26px;
        color: #333333;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(4) > div > div > div > button {
        background-color: #EEEEEE;
        color: #BFBFBF;
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
        color: white;
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
        background-color: #D8D5D5;
        border-style: inset;
        line-height: 0.5;
        font-size: 0px;
    }
    .streamlit-expanderContent  {
        line-height: 0.5;
        font-size: 0px;
    }
    .streamlit-expanderContent > div  {
    }
    .streamlit-expanderContent > div > div {
    }
    .streamlit-expanderContent > div > div > div  {
        width: 100%;
        display: flex;
        flex-direction: row;
        flex: 1 1 0%;
        line-height: 0.5;
        font-size: 0px;
    }
    .streamlit-expanderContent > div > div > div > div {
        display: flex;
        flex-direction: row;
        flex: 1 1 0%;
    }
    .streamlit-expanderContent > div > div > div > div > div {
        display: flex;
        flex-direction: row;
        flex: 1 1 0%;
        width: 0%;
        padding: 0px 2px 0px 2px;
    }
    .streamlit-expanderContent > div > div > div > div > div:nth-child(1) {
        flex: 0 0 0%;
        width: 2.5rem;
    }
    .streamlit-expanderContent > div > div > div:nth-child(n+2) > div > div:nth-child(1) {
        flex: 1 1 0%;
        padding: 8px 8px 8px 8px;
        align-items: center !important;
        -webkit-align-items: center;
        justify-content: center;
    }
    .streamlit-expanderContent > div > div > div > div > div:nth-child(1) > div {
        display: flex;
        flex-direction: row;
        flex: 1 1 0%;
    }
    .streamlit-expanderContent > div > div > div > div > div:nth-child(1) > div > button {
        background-color: #456E44;
        flex: 1 1 0%;
    }
    .streamlit-expanderContent > div > div > div > div > div:nth-child(1) > div > button:hover {
        border-color: black;
        color: #333333;
    }
    .streamlit-expanderContent > div > div > div > div > div:nth-child(2) > div {
        display: flex;
        flex-direction: row;
        flex: 1 1 0%;
        align-items: center;
        -webkit-align-items: center;
        justify-content: flex-end;
        padding-right: 3px;
    }
    .streamlit-expanderContent > div > div > div > div > div:nth-child(2) > div > div > p {
        font-size: 20px;
        font-weight: bold;
    }
    .streamlit-expanderContent > div > div > div > div > div:nth-child(3) > div {
        display: flex;
        flex-direction: row;
        flex: 1 1 0%;
        align-items: right;
        -webkit-align-items: right;
        justify-content: right;
    }
    .streamlit-expanderContent > div > div > div > div > div:nth-child(3) > div > button {
        font-size: 20px;
        background-color: #456E44;
        flex: 1 1 0%;
    }
    .streamlit-expanderContent > div > div > div > div > div:nth-child(3) > div > button:hover {
        border-color: black;
        color: #333333;
    }
    .streamlit-expanderContent > div > div > div.element-container > div > div > p {
        padding: 4px 4px 4px 4px;
        margin: 0px 0px 0px;
    }
    .streamlit-expanderContent > div > div > div.element-container > div > div > p:nth-child(2) {
        min-width: 20%;
        overflow-wrap: normal;
    }
    .st-ae {
        font-size: 18px;
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
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(n+16) > div {
        border-style: none;
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
        margin: 6px 6px 6px;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(9) > div > div > div.e1tzin5v0 {
        padding: 6px 12px 6px 6px;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(9) > div > div > div.e1tzin5v0 > div {
        width: 100%;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(9) > div > div > div.e1tzin5v0 > div > div {
        width: 100% !important;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(9) > div > div > div.e1tzin5v0 > div > div > label {
        font-size: 20px;
        font-weight: bold;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(9) > div > div:nth-child(n+2) {
        height: 0px;
        flex: 0 0 0% !important;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(9) > div > div:nth-child(n+2) > div.e1tzin5v0 {
        position: absolute;
        bottom: 0px;
        width: 0px;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(9) > div > div > div.e1tzin5v0 > div:nth-child(3) {
        display: flex;
        flex: 1 1 0%;
        align-items: flex-end;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(9) > div > div > div.e1tzin5v0 > div:nth-child(3) > div.stButton {
        display: flex;
        flex: 1 1 0%;
        justify-content: flex-end;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(9) > div > div:nth-child(1) > div > div:nth-child(1) > div > div > div > div > svg:nth-child(1) {
        width: 40px;
        height: 32px;
        padding: 0px 8px 0px 0px;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(9) > div > div:nth-child(1) > div > div:nth-child(1) > div > div > div > div > svg:nth-child(2) {
        width: 40px;
        height: 32px;
        padding: 0px 0px 0px 8px;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(7) > div > div > div > div > div {
        flex-direction: row;
        display: flex;
        flex: 1 1 100%;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(7) > div > div > div > div > div > div {
        font-size: 40px;
        padding: 8px 16px 8px 8px;
        flex-direction: row;
        display: flex;
        flex: 1 1 100%;
        justify-content: flex-end;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(7) > div > div > div > div > div > div > div {
        align-items: center;
        margin: 0px;
        display: flex;
        position: absolute;
        left: 8px;
        padding-top: 8px;
        padding-bottom: 8px;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(7) > div > div > div > div > div > div > div > div {
        position: absolute;
        left: 15px;
        top: 2px;
        height: 0px;
        font-weight: bold;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(7) > div > div > div > div > div > div > p {
        align-items: center;
        margin: 0px;
        display: flex;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(7) > div > div > div > div > div > div > p:nth-of-type(1) {
        justify-content: center;
        display: flex;
        flex: 1 1 0%;
        padding-left: 60px;
        width: 80px;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(7) > div > div > div > div > div > div > p:nth-of-type(2) {
        overflow-wrap: normal;
        width: 180px;
    }
    .stApp {
        background-color: white;
    }
    </style>
    <link href='https://fonts.googleapis.com/css?family=Norican' rel='stylesheet' type='text/css'>

    """ + style + style2, unsafe_allow_html=True)



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

    with st.container():
        st.button("<", key="leftbutton", on_click=week_back_button_func, args=[week])
        st.write("Week {}".format(weekname))
        st.button(">", key="rightbutton", on_click=week_forward_button_func, args=[week])


    img_dict = {"Alec": 'https://cdn1.edgedatg.com/aws/v2/abc/TheBachelorette/person/4003259/809f10c81eaf7ccd46b7a5807f1fd0e0/1600x640-Q90_809f10c81eaf7ccd46b7a5807f1fd0e0.jpg',
                "Aven": 'https://cdn1.edgedatg.com/aws/v2/abc/TheBachelorette/person/4003284/6d084cfde81ac818446f7f6b55c8303f/1600x640-Q90_6d084cfde81ac818446f7f6b55c8303f.jpg',
                "Brandan": 'https://cdn1.edgedatg.com/aws/v2/abc/TheBachelorette/person/4003289/55e706b199faa49724d907d9a05194af/1600x640-Q90_55e706b199faa49724d907d9a05194af.jpg',
                "Chris": 'https://cdn1.edgedatg.com/aws/v2/abc/TheBachelorette/person/4003301/ad9705379efff9f33b274c14c7642710/1600x640-Q90_ad9705379efff9f33b274c14c7642710.jpg',
                "Colin": 'https://cdn1.edgedatg.com/aws/v2/abc/TheBachelorette/person/4003302/a9d8e4bee79f0c068ffd0c71d07eab6c/1600x640-Q90_a9d8e4bee79f0c068ffd0c71d07eab6c.jpg',
                "Erich": 'https://cdn1.edgedatg.com/aws/v2/abc/TheBachelorette/person/4003303/f50b79c56418a83fc2a7361c98e7454c/1600x640-Q90_f50b79c56418a83fc2a7361c98e7454c.jpg',
                "Ethan": 'https://cdn1.edgedatg.com/aws/v2/abc/TheBachelorette/person/4003311/99f174f61665aeddd70c146379d50fee/1600x640-Q90_99f174f61665aeddd70c146379d50fee.jpg',
                "Hayden": 'https://cdn1.edgedatg.com/aws/v2/abc/TheBachelorette/person/4003318/ab65e2acd1c8f247f414503790065d76/1600x640-Q90_ab65e2acd1c8f247f414503790065d76.jpg',
                "Jacob": 'https://cdn1.edgedatg.com/aws/v2/abc/TheBachelorette/person/4003319/d95bf9fe942f8a6696bee5f3539e3003/1600x640-Q90_d95bf9fe942f8a6696bee5f3539e3003.jpg',
                "James": 'https://cdn1.edgedatg.com/aws/v2/abc/TheBachelorette/person/4003320/10ed9fdd86bcf56666712b79342b4103/1600x640-Q90_10ed9fdd86bcf56666712b79342b4103.jpg',
                "James (Meatball)": 'https://cdn1.edgedatg.com/aws/v2/abc/TheBachelorette/person/4003320/10ed9fdd86bcf56666712b79342b4103/1600x640-Q90_10ed9fdd86bcf56666712b79342b4103.jpg',
                "Jason": 'https://cdn1.edgedatg.com/aws/v2/abc/TheBachelorette/person/4003327/604317984164be87ba6badfd5d482b80/1600x640-Q90_604317984164be87ba6badfd5d482b80.jpg',
                "Joey": 'https://cdn1.edgedatg.com/aws/v2/abc/TheBachelorette/person/4003336/498a897e5d1c7ab0373e3cc8e8f4969a/1600x640-Q90_498a897e5d1c7ab0373e3cc8e8f4969a.jpg',
                "John": 'https://cdn1.edgedatg.com/aws/v2/abc/TheBachelorette/person/4003341/f66997f7e2e49ee1a345f0d65a1cc18d/1600x640-Q90_f66997f7e2e49ee1a345f0d65a1cc18d.jpg',
                "Johnny": 'https://cdn1.edgedatg.com/aws/v2/abc/TheBachelorette/person/4003342/939a460fd196455c3c4caff14f5b4ec4/1600x640-Q90_939a460fd196455c3c4caff14f5b4ec4.jpg',
                "Jordan H.": 'https://cdn1.edgedatg.com/aws/v2/abc/TheBachelorette/person/4003421/993015f8df7f09144bf77915500279bb/1600x640-Q90_993015f8df7f09144bf77915500279bb.jpg',
                "Jordan V.": 'https://cdn1.edgedatg.com/aws/v2/abc/TheBachelorette/person/4003422/eeb0a26e44b6e1dfd0021ccc7c9adfac/1600x640-Q90_eeb0a26e44b6e1dfd0021ccc7c9adfac.jpg',
                "Justin B.": 'https://cdn1.edgedatg.com/aws/v2/abc/TheBachelorette/person/4003426/5c5b3667a86f0e1722f4dd85469d4262/1600x640-Q90_5c5b3667a86f0e1722f4dd85469d4262.jpg',
                "Justin Y.": 'https://cdn1.edgedatg.com/aws/v2/abc/TheBachelorette/person/4003427/deef3202bcf1720ee77c6c275a52ee92/1600x640-Q90_deef3202bcf1720ee77c6c275a52ee92.jpg',
                "Kirk": 'https://cdn1.edgedatg.com/aws/v2/abc/TheBachelorette/person/4003430/cb2c28038138c4c3fc2cd33437b50833/1600x640-Q90_cb2c28038138c4c3fc2cd33437b50833.jpg',
                "Logan": 'https://cdn1.edgedatg.com/aws/v2/abc/TheBachelorette/person/4003434/6cbccf64d86968aed37f9e85ffd1da67/1600x640-Q90_6cbccf64d86968aed37f9e85ffd1da67.jpg',
                "Mario": 'https://cdn1.edgedatg.com/aws/v2/abc/TheBachelorette/person/4003439/a23cb11d6846500a8788aa3ab3fe2518/1600x640-Q90_a23cb11d6846500a8788aa3ab3fe2518.jpg',
                "Matt": 'https://cdn1.edgedatg.com/aws/v2/abc/TheBachelorette/person/4003441/8c0070282bb16145f7cdba54998ac3a5/1600x640-Q90_8c0070282bb16145f7cdba54998ac3a5.jpg',
                "Michael": 'https://cdn1.edgedatg.com/aws/v2/abc/TheBachelorette/person/4004568/ef694b0c1a17d5dc00995832ac908e68/1600x640-Q90_ef694b0c1a17d5dc00995832ac908e68.jpg',
                "Nate": 'https://cdn1.edgedatg.com/aws/v2/abc/TheBachelorette/person/4004578/137c32399ffff6832986719187ea81d1/1600x640-Q90_137c32399ffff6832986719187ea81d1.jpg',
                "Quincey": 'https://cdn1.edgedatg.com/aws/v2/abc/TheBachelorette/person/4004586/03c20ec0e96ce129bb6806b2cf97c86e/1600x640-Q90_03c20ec0e96ce129bb6806b2cf97c86e.jpg',
                "Roby": 'https://cdn1.edgedatg.com/aws/v2/abc/TheBachelorette/person/4004587/6abdf0cb8f56be72c59cc574f18d6107/1600x640-Q90_6abdf0cb8f56be72c59cc574f18d6107.jpg',
                "Ryan": 'https://cdn1.edgedatg.com/aws/v2/abc/TheBachelorette/person/4004594/d803872f0107102d45f2c6d2354eb2b8/1600x640-Q90_d803872f0107102d45f2c6d2354eb2b8.jpg',
                "Spencer": 'https://cdn1.edgedatg.com/aws/v2/abc/TheBachelorette/person/4004595/0ad4a1d3b01af5801647aa3cbb82b2a0/1600x640-Q90_0ad4a1d3b01af5801647aa3cbb82b2a0.jpg',
                "Termayne": 'https://cdn1.edgedatg.com/aws/v2/abc/TheBachelorette/person/4004598/59b04a004391698250e245ff8c3d5e5a/1600x640-Q90_59b04a004391698250e245ff8c3d5e5a.jpg',
                "Tino": 'https://cdn1.edgedatg.com/aws/v2/abc/TheBachelorette/person/4004599/feb9500f43f30a789c1352c0958451ca/1600x640-Q90_feb9500f43f30a789c1352c0958451ca.jpg',
                "Tyler": 'https://cdn1.edgedatg.com/aws/v2/abc/TheBachelorette/person/4004619/3693d4cc2fe4f0f5fa08860523ef46e4/1600x640-Q90_3693d4cc2fe4f0f5fa08860523ef46e4.jpg',
                "Zach": 'https://cdn1.edgedatg.com/aws/v2/abc/TheBachelorette/person/4004620/515d20fec26e682359e4f15122f0848f/1600x640-Q90_515d20fec26e682359e4f15122f0848f.jpg'}

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
            info_buttons = []
            selection_buttons = []
            i = 0
            while i < len(bet_titles):
                if bet_types[i] == "main":
                    my_expander = st.expander(bet_titles[i])
                else:
                    my_expander = st.expander(bet_titles[i] + '\xa0 \xa0 \xa0 \U0001f4b8')
                with my_expander:
                    with st.container():
                        info_buttons.append(st.button("ⓘ", key='infobutton'+str(i)))
                        curr_count = len(df_gsheet[(df_gsheet["Username"]==username)&(df_gsheet["Week"]==week)&(df_gsheet["Question"]==i+1)])
                        st.write(str(curr_count)+" / " + str(bet_possiblecounts[i]) + " selected")
                        selection_buttons.append(st.button("Select", key='editbutton'+str(i)))

                    curr_selects = df_gsheet[(df_gsheet["Username"]==username)&(df_gsheet["Week"]==week)&(df_gsheet["Question"]==i+1)]["Choice"]
                    for curr in curr_selects:
                        img_url = get_display(bet_choicestypes[i], curr, bet_textprefixes[i], bet_textsuffixes[i])
                        img =f"""
                               {img_url}
                        """
                        st.markdown(img, unsafe_allow_html=True)
                i = i + 1

            style = f"""<style>

                #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(n+13) > div > div:nth-child(2) > div > button {{
                    font-size:24px !important; font-weight: bold; }}

            </style>"""
            st.markdown(style, unsafe_allow_html=True)

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


        if standings_button:
            bet_container.empty()
            contestants_container.empty()
            standings_container.empty()
            info_container.empty()
            selection_container.empty()
            st.session_state['visit_flag'] = 100
            standings_container_go()
        if contestants_button:
            bet_container.empty()
            contestants_container.empty()
            standings_container.empty()
            info_container.empty()
            selection_container.empty()
            st.session_state['visit_flag'] = 200
            contestants_container_go()



    def cancel_button_func():
        bet_container.empty()
        contestants_container.empty()
        standings_container.empty()
        info_container.empty()
        selection_container.empty()
        st.session_state['visit_flag'] = 0
        #bet_container_go()

    def save_button_func(selec, b, stat, add=[], delete=[]):
        global df_gsheet
        total = len(df_gsheet)+2
        if stat == "new" or stat == "overwrite":
            if stat == "overwrite":
                for row in reversed(df_gsheet[(df_gsheet["Week"]==week)&(df_gsheet["Question"]==b+1)&(df_gsheet["Username"]==username)].index.to_list()):
                    sh.delete_rows(row+2)
                    time.sleep(0.1)
                df_gsheet = pd.DataFrame(data=sh.get_all_records())
                total = len(df_gsheet)+2
            if bet_possiblecounts[b] > 1:
                cell_range = '{col_i}{row_i}:{col_f}{row_f}'.format(
                    col_i=chr((1-1) + ord('A')),    # converts number to letter = 1 - 1 = A-1
                    col_f=chr((4-1) + ord('A')),
                    row_i=total,
                    row_f=total+len(selec))
                cell_list = sh.range(cell_range)
                for s, select in enumerate(selec):
                    cell_list[(s*4)+1-1].value = week
                    cell_list[(s*4)+2-1].value = b+1
                    cell_list[(s*4)+3-1].value = username
                    cell_list[(s*4)+4-1].value = select
                sh.update_cells(cell_list)
            else:
                cell_range = '{col_i}{row_i}:{col_f}{row_i}'.format(
                    col_i=chr((1-1) + ord('A')),    # converts number to letter = 1 - 1 = A-1
                    col_f=chr((4-1) + ord('A')),
                    row_i=total)
                cell_list = sh.range(cell_range)
                cell_list[1-1].value = week
                cell_list[2-1].value = b+1
                cell_list[3-1].value = username
                cell_list[4-1].value = selec
                sh.update_cells(cell_list)
        if stat == "split":
            cell_range = '{col_i}{row_i}:{col_f}{row_f}'.format(
                col_i=chr((1-1) + ord('A')),    # converts number to letter = 1 - 1 = A-1
                col_f=chr((4-1) + ord('A')),
                row_i=total,
                row_f=total+len(add))
            cell_list = sh.range(cell_range)
            for s, select in enumerate(add):
                cell_list[(s*4)+1-1].value = week
                cell_list[(s*4)+2-1].value = b+1
                cell_list[(s*4)+3-1].value = username
                cell_list[(s*4)+4-1].value = select
            sh.update_cells(cell_list)
            for s, select in enumerate(delete):
                for row in reversed(df_gsheet[(df_gsheet["Week"]==week)&(df_gsheet["Question"]==b+1)&(df_gsheet["Username"]==username)&(df_gsheet["Choice"]==select)].index.to_list()):
                    sh.delete_rows(row+2)
                    time.sleep(0.1)
                df_gsheet = pd.DataFrame(data=sh.get_all_records())
                total = len(df_gsheet)+2

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
            st.markdown("""<style>

                #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(n+13) > div > div:nth-child(1) > div > button {
                    font-size:22px !important; font-weight: bold; }

            </style>""", unsafe_allow_html=True)

    def standings_container_go():
        global standings_container
        with standings_container.container():
            file_1 = open("trophy.ico", "rb")
            contents1 = file_1.read()
            data_url1 = base64.b64encode(contents1).decode("utf-8")
            file_1.close()
            file_up = open("arrow-up.ico", "rb")
            contentsup = file_up.read()
            data_urlup = base64.b64encode(contentsup).decode("utf-8")
            file_up.close()
            file_down = open("arrow-down.ico", "rb")
            contentsdown = file_down.read()
            data_urldown = base64.b64encode(contentsdown).decode("utf-8")
            file_down.close()

            userlist_now = []
            df_gsheet["Points"] = pd.to_numeric(df_gsheet["Points"], errors='coerce')
            for user in config['credentials']['usernames']:
                total_points = 0
                last_points = 0
                for w in range(1,week+1):
                    if w > 1:
                        total_points = total_points + int(sum(df_gsheet[(df_gsheet["Username"]==user) & (df_gsheet["Week"]==w-1)]["Points"].fillna(0)))
                    if w > 2:
                        if w == 3:
                            last_points = 0
                        last_points = last_points + int(sum(df_gsheet[(df_gsheet["Username"]==user) & (df_gsheet["Week"]==w-2)]["Points"].fillna(0)))
                    else:
                        last_points = total_points
                userlist_now.append([user, total_points, last_points])

            userlist_now.sort(key=lambda x:(-x[1]))
            temp1 = [u[0] for u in userlist_now]
            userlist_now.sort(key=lambda x:(-x[2]))
            temp2 = [u[0] for u in userlist_now]

            userlist = []
            for user in config['credentials']['usernames']:
                total_points = 0
                main_points = 0
                fast_points = 0
                fast_dollars = 0
                for w in range(1,week+1):
                    if w > 1:
                        bet_types = [qconfig["weeks"][str(w-1)]["bets"][x]["type"] for x in qconfig["weeks"][str(w-1)]["bets"]]
                        total_points = total_points + int(sum(df_gsheet[(df_gsheet["Username"]==user) & (df_gsheet["Week"]==w-1)]["Points"].fillna(0)))
                        main_points = main_points + int(sum(df_gsheet[(df_gsheet["Username"]==user) & (df_gsheet["Week"]==w-1) & (df_gsheet["Question"].isin([n+1 for n, i in enumerate(bet_types) if i == "main"]))]["Points"].fillna(0)))
                        fast_points = fast_points + int(sum(df_gsheet[(df_gsheet["Username"]==user) & (df_gsheet["Week"]==w-1) & (df_gsheet["Question"].isin([n+1 for n, i in enumerate(bet_types) if i == "oneperperson"]))]["Points"].fillna(0)))
                        fast_dollars = fast_dollars + int(len(df_gsheet[(df_gsheet["Username"]==user) & (df_gsheet["Week"]==w-1) & (df_gsheet["Question"].isin([n+1 for n, i in enumerate(bet_types) if i == "oneperperson"])) & df_gsheet["Points"] > 0]["Points"].fillna(0)))
                arrow = '<p style="border-style: none; outline: none; background-color: transparent; padding-left: 29px; padding-bottom: 25px; margin: 0px 0px 0px;"></p>'
                # if [n for n, i in enumerate(temp1) if i[0] == user][0] > [n for n, i in enumerate(temp2) if i[0] == user][0]:
                #     arrow = f'<img src="data:image/gif;base64,{data_urlup}" alt="rose" height="25px" width="29px" style=" padding-left: 4px; padding-bottom: 2px;">'
                # elif [n for n, i in enumerate(temp1) if i[0] == user][0] < [n for n, i in enumerate(temp2) if i[0] == user][0]:
                #     arrow = f'<img src="data:image/gif;base64,{data_urldown}" alt="rose" height="25px" width="29px" style=" padding-left: 4px; padding-bottom: 2px;">'
                if temp1.index(user) < temp2.index(user):
                    arrow = f'<img src="data:image/gif;base64,{data_urlup}" alt="rose" height="25px" width="29px" style=" padding-left: 4px; padding-bottom: 2px;">'
                elif temp1.index(user) > temp2.index(user):
                    arrow = f'<img src="data:image/gif;base64,{data_urldown}" alt="rose" height="25px" width="29px" style=" padding-left: 4px; padding-bottom: 2px;">'
                userlist.append([config['credentials']['usernames'][user]['name'].split(" ")[0], total_points, main_points, fast_points, fast_dollars, arrow, user])

            userlist.sort(key=lambda x:(-x[1]))
            for u, user in enumerate(userlist):
                with st.container():
                    st.markdown(f""" <div style="font-size: 26px; ">
                            <img src="data:image/gif;base64,{data_url1}" alt="rose" height="50px" width="45px">
                            {user[5]}
                            <div>{u+1}</div></div>
                            <p style="font-size: 20px;"><b>{user[0]}</b></p>
                            <p style="font-size: 12px;">Total Points: {user[1]}<br>Points from Main Bets: {user[2]}<br>Points from Fast Money Bets: {user[3]} (${user[4]})</p> """, unsafe_allow_html=True)

            st.markdown("""<style>

                #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(n+13) > div > div:nth-child(3) > div > button {
                    font-size:22px !important; font-weight: bold; }

            </style>""", unsafe_allow_html=True)

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

            st.markdown("""<style>

                #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(4) > div > div:nth-child(1) > div,
                #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(4) > div > div:nth-child(3) > div,
                #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(4) > div > div:nth-child(1) > div > button,
                #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(4) > div > div:nth-child(3) > div > button {
                    height: 0px; width: 0px !important; visibility: hidden; }

            </style>""", unsafe_allow_html=True)

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
            choices = bet_choices[b]
            if bet_types[b] == "main":
                for c,choice in enumerate(choices):
                    if len(df_gsheet[(df_gsheet["Week"]==week)&(df_gsheet["Question"]==b+1)&(df_gsheet["Choice"]==choice)&(df_gsheet["Username"]==username)]) > 0:
                        choices[c] = str(choices[c]) + "\xa0    *Saved*"

            elif bet_types[b] == "oneperperson":
                for c,choice in enumerate(choices):
                    if len(df_gsheet[(df_gsheet["Week"]==week)&(df_gsheet["Question"]==b+1)&(df_gsheet["Choice"]==choice)]) > 0:
                        usertemp=df_gsheet[(df_gsheet["Week"]==week)&(df_gsheet["Question"]==b+1)&(df_gsheet["Choice"]==choice)]["Username"].to_string(index=False)
                        choices[c] = str(choices[c]) + "\xa0    *" + config['credentials']['usernames'][usertemp]["name"].split(" ")[0] + "*"

            status = ""
            adding = []
            deleting = []
            with st.container() as form:
            #with st.form(key="selectbox") as form:

                if bet_possiblecounts[b] > 1:
                    myselectbox = st.multiselect(bet_titles[b], [c[0:c.find('*')].strip() if c.find('*') > -1 else c for c in choices], [c[0:c.find('*')].strip() for c in choices if str(c).find('*') > -1])

                    if submitweek == "" or week != qconfig["weeks"][submitweek]["week"]:
                        st.write("**You have selected:** " + ', '.join([str(s) for s in myselectbox]) + '  ' + "\n**Submissions are closed for this week.**")
                    elif myselectbox == [c[0:c.find('*')].strip() for c in choices if str(c).find('*') > -1]:
                        st.write("**You have selected:** " + ', '.join([str(s) for s in myselectbox]) + '  ' + "\n**This is the choice you currently have saved.**")
                    elif len(myselectbox) > bet_possiblecounts[b]:
                        st.write("**You have selected:** " + ', '.join([str(s) for s in myselectbox]) + '  ' + "\n**You have selected too many options. Please limit your choices to** " + str(bet_possiblecounts[b]))
                    else:
                        st.write("**You have selected:** " + ', '.join([str(s) for s in myselectbox]) + '  \n**Would you like to save this as your new choice?  \nYou are adding:** '
                                    + ', '.join([str(s) for s in myselectbox if s not in [c[0:c.find('*')].strip() for c in choices if str(c).find('*') > -1]]) + '  \n**You are deleting:** '
                                    +  ', '.join([str(s) for s in [c[0:c.find('*')].strip() for c in choices if str(c).find('*') > -1] if s not in myselectbox]))
                        if len(df_gsheet[(df_gsheet["Week"]==week)&(df_gsheet["Question"]==b+1)&(df_gsheet["Username"]==username)]) > 0:
                            status = "split"
                            adding = [str(s) for s in myselectbox if s not in [c[0:c.find('*')].strip() for c in choices if str(c).find('*') > -1]]
                            deleting = [str(s) for s in [c[0:c.find('*')].strip() for c in choices if str(c).find('*') > -1] if s not in myselectbox]
                        else:
                            status = "new"

                else:
                    if len([n for n,c in enumerate(choices) if (str(c).find('*Saved*') > -1 or str(c).find('*' + name + '*') > -1)]) > 0:
                        myselectbox = st.selectbox(bet_titles[b], choices, index=[n for n,c in enumerate(choices) if (str(c).find('*Saved*') > -1 or str(c).find('*' + name + '*') > -1)][0], key="selectbox"+str(b))
                    else:
                        myselectbox = st.selectbox(bet_titles[b], choices, index=0, key="selectbox"+str(b))

                    if (submitweek == "" or week != qconfig["weeks"][submitweek]["week"]) and str(myselectbox).find("*") > -1:
                        st.write("**You have selected:** " + str(myselectbox[0:str(myselectbox).find('*')]) + '  ' + "\n**Submissions are closed for this week.**")
                    elif str(myselectbox).find("*") == -1:
                        st.write("**You have selected:** " + str(myselectbox) + '  ' + "\n**Would you like to save this as your new choice?**")
                        if len(df_gsheet[(df_gsheet["Week"]==week)&(df_gsheet["Question"]==b+1)&(df_gsheet["Username"]==username)]) > 0:
                            status = "overwrite"
                        else:
                            status = "new"
                    elif str(myselectbox).find("*"+name+"*") > -1 or str(myselectbox).find("*Saved*") > -1:
                        st.write("**You have selected:** " + str(myselectbox[0:str(myselectbox).find('*')]) + '  ' + "\n**This is the choice you currently have saved.**")
                    else:
                        st.write("**You have selected:** " + str(myselectbox) + '  ' + "\n**This choice is unavailable. Please make another selection.**")

                save_button = st.button("Save and Close", on_click=save_button_func, args=[myselectbox,b,status,adding,deleting])


            with st.container():
                cancel_button = st.button("Cancel", on_click=cancel_button_func)

            st.markdown("""<style>

                #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(4) > div > div:nth-child(1) > div,
                #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(4) > div > div:nth-child(3) > div,
                #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(4) > div > div:nth-child(1) > div > button,
                #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div:nth-child(4) > div > div:nth-child(3) > div > button {
                    height: 0px; width: 0px !important; visibility: hidden; }

            </style>""", unsafe_allow_html=True)

    def get_display(type, input, text_prefix='', text_suffix=''):
        if type == "img":
            tag = '<img src="' + img_dict[input] + '" alt="' + input + '" style="max-height: 100%; max-width: 100%;"><p><b>' + input + '</b></p>'
        if type == "text":
            tag = '<p style="font-size: 20px; line-height: 1.6;"><b><i>' + text_prefix + str(input) + text_suffix + '</i></b></p>'

        return tag


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
        st.session_state["visit_flag"] = 100
        standings_container_go()
    elif contestants_button:
        bet_container.empty()
        contestants_container.empty()
        standings_container.empty()
        info_container.empty()
        selection_container.empty()
        st.session_state["visit_flag"] = 200
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
    elif st.session_state["visit_flag"] > 0 and st.session_state["visit_flag"] < 100:
        selection_container_go(st.session_state["visit_flag"]-1)
        st.legacy_caching.clear_cache()
    elif st.session_state["visit_flag"] == 100:
        standings_container_go()
    elif st.session_state["visit_flag"] == 200:
        contestants_container_go()



gc = gspread.service_account(filename='./cred.json')
sheet1 = gc.open_by_url('https://docs.google.com/spreadsheets/d/1iudlYSDTvHLjEa0q04ebYmVnb8cV1xD7qJMUBj0rxFs/edit?usp=sharing')
sh = sheet1.get_worksheet(0)
df_gsheet = pd.DataFrame(data=sh.get_all_records())

with open('./cred.yaml') as file:
    config = yaml.safe_load(file)

with open('./questions.yaml') as file:
    qconfig = yaml.safe_load(file)

for user in config['credentials']['usernames'].keys():
    config['credentials']['usernames'][user]['password'] = stauth.Hasher([config['credentials']['usernames'][user]['password']]).generate()[0]

authenticator = stauth.Authenticate(config['credentials'],'bachelor_bets','harrison',cookie_expiry_days=30)
name, authentication_status, username = authenticator.login('Login','main')
time.sleep(0.5)

ready_weeks = [x for x in qconfig["weeks"] if qconfig["weeks"][x]["ready"] == "yes"]
thisweek = ready_weeks[len(ready_weeks)-1]
now = datetime.datetime.now()
submitweek_group = [x for x in qconfig["weeks"] if
    datetime.datetime(qconfig["weeks"][x]["submitStartyear"],qconfig["weeks"][x]["submitStartmonth"],qconfig["weeks"][x]["submitStartday"],qconfig["weeks"][x]["submitStarthour"],qconfig["weeks"][x]["submitStartminute"]) <= now <
    datetime.datetime(qconfig["weeks"][x]["submitEndyear"],qconfig["weeks"][x]["submitEndmonth"],qconfig["weeks"][x]["submitEndday"],qconfig["weeks"][x]["submitEndhour"],qconfig["weeks"][x]["submitEndminute"])]
if len(submitweek_group) > 0:
    submitweek = submitweek_group[0]
else:
    submitweek = ""

if 'week' not in st.session_state:
    st.session_state["week"] = qconfig["weeks"][thisweek]["week"]

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
