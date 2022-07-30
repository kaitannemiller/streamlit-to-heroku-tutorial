


import sys
from contextlib import closing

import lxml.html as html # pip install 'lxml>=2.3.1'
from lxml.html.clean        import Cleaner
from selenium.webdriver     import Chrome
from selenium.webdriver.chrome.options import Options         # pip install selenium
from werkzeug.contrib.cache import FileSystemCache # pip install werkzeug
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select

import time
import datetime
import os
import csv

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import requests

import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

import shutil

import urllib

import clipboard


from progress.bar import IncrementalBar


def openbrowser(url, timeoutloops):
    global Firm
    global maindir
    global shortname

    loop = 0
    success = 0
    while(loop <= timeoutloops and success == 0):
        #try:
        print('staring try 1-' + str(loop) + ' ' + url)
        browser = Chrome(options=opts)
        browser.implicitly_wait(10)
        browser.set_page_load_timeout(60)
        browser.get(url)
        success = 1
        time.sleep(3)
        # except:
        #     print('staring except 1-' + str(loop))
        #     foundbrowser = getTasks('chromedriver')
        #     if foundbrowser != []:
        #         try:
        #             print('staring try 2-' + str(loop))
        #             os.system("taskkill /f /im chromedriver.exe")
        #             browser.quit()
        #             if getTasks('chrome') != []:
        #                 os.system("taskkill /f /im chrome.exe")
        #             time.sleep(1)
        #             foundbrowser = getTasks('chromedriver')
        #             if foundbrowser != []:
        #                 os.system("taskkill /f /im chromedriver.exe")
        #                 browser.quit()
        #                 if getTasks('chrome') != []:
        #                     os.system("taskkill /f /im chrome.exe")
        #                 time.sleep(1)
        #         except:
        #             print('staring except 2-' + str(loop))
        #             try:
        #                 print('staring try 3-' + str(loop))
        #                 os.system("taskkill /f /im chromedriver.exe")
        #                 browser.quit()
        #                 if getTasks('chrome') != []:
        #                     os.system("taskkill /f /im chrome.exe")
        #                 time.sleep(1)
        #             except:
        #                 print('staring except 3-' + str(loop))
        #                 print('timeout error when closing url: \n' + url)
        #         time.sleep(1)

        loop = loop + 1

    if success == 0:
        print('timeout error when loading url: \n' + url)
        print(TimeoutException)
        exit()
    else:
        time.sleep(1)
        browser.switch_to_window(browser.current_window_handle)
        print('successfully loaded url ' + url)
        return browser


def getTasks(name):
    global Firm
    global maindir
    global shortname

    r = os.popen('tasklist /v').read().strip().split('\n')
    for i in range(len(r)):
        s = r[i]
        if name in r[i]:
            return r[i]
    return []


def mail(subject, text, imgfile):

    if not imgfile == '':
        fp = open(imgfile, 'rb')
        img = MIMEImage(fp.read())
        fp.close()

    msgtext = MIMEText(text + '\n', 'plain')

    fromx = 'kamiller5678@gmail.com'
    to  = 'trigger@applet.ifttt.com'
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = fromx
    msg['To'] = to
    msg.attach(msgtext)

    if not imgfile == '':
        msg.attach(img)

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.ehlo()
    server.login('kamiller5678@gmail.com', 'disneY!454')
    server.sendmail(fromx, to, msg.as_string())
    server.quit()



def getValue(string, startterm, endterm, startbuffer=0):
    global Firm
    global maindir
    global shortname


    if string.find(startterm) > -1 and string.find(endterm, string.find(startterm)+len(startterm)+startbuffer+1) > -1:
        return string[string.find(startterm)+len(startterm)+startbuffer:string.find(endterm, string.find(startterm)+len(startterm)+startbuffer)]
    else:
        return ''


#setting up browser
cache = FileSystemCache('.cachedir', threshold=100000)
url = 'https://www.google.com/'
opts = Options()
opts.add_argument("window-size=1200,1200")
opts.add_argument("--log-level=3")
#opts.add_argument("user-data-dir=chrome-data")
page_source = cache.get(url)
if page_source is None:
    with closing(Chrome(options=opts)) as browser:
        browser.get(url)
        page_source = browser.page_source
    cache.set(url, page_source, timeout=60*60*24*7) # week in seconds



browser = openbrowser('https://www.hulu.com/welcome', 10)
time.sleep(8)




newcookie = '[{"name" : "bm_mi", "value" : "F6A24C09E4B37A8F25AAAE88B54906F0~UMFV8JxHGvsqaaA4cLTocEXHxdLnl0KZvjV9+ILYRjsiUG0zJOS28+D+ZscinVhQUmTC+XzMRcSBy/mfFpydB9hyB419PFjuXdJUgBqMVdqAaNs0jPcpQFTn02tdzpEe482Uj2w3yXbtf9u8B0h61UH2wfQ84sn7lf4T6D/IlH5KlTa2jC6u04lywFEgMCffqw+4wLwAgDI7tfWHgfJ0/sV5NZb+Ur0Zu2q27As7FZfVp6cgKWELqV96XpbM5tW0qDm/FWEeonDLHG/GiRcg+A=="}, {"name" : "__utma", "value" : "155684772.1984683707.1639348790.1639348790.1639348790.1"}, {"name" : "__utmc", "value" : "155684772"}, {"name" : "__utmz", "value" : "155684772.1639348790.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)"}, {"name" : "__utmt", "value" : "1"}, {"name" : "__utmb", "value" : "155684772.1.10.1639348790"}, {"name" : "_ga", "value" : "GA1.2.1984683707.1639348790"}, {"name" : "_gid", "value" : "GA1.2.1344526324.1639348791"}, {"name" : "_gcl_au", "value" : "1.1.1123779343.1639348791"}, {"name" : "_uetsid", "value" : "6b5365705b9c11ec979c2715248bff5a"}, {"name" : "_uetvid", "value" : "47c30a802ea511ecad98d76b74169b4a"}, {"name" : "rmStore", "value" : "ald:20211016_1730|atrv:AysPbYF8vuM-Gmy24jM.WIZBavU.HyJSYw"}, {"name" : "stc115168", "value" : "tsa:1639348791589.1512204870.569322.2242630421026217.1:20211212230951|env:1|20220112223951|20211212230951|1|1047148:20221212223951|uid:1639348791588.646494428.8561535.115168.1709060036.:20221212223951|srchist:1047148:1:20220112223951:20221212223951"}, {"name" : "_scid", "value" : "4cd51d82-49c9-4a43-a174-b9af0689f260"}, {"name" : "_clck", "value" : "w5wkpz|1|ex7|0"}, {"name" : "_clsk", "value" : "d3od4o|1639348793030|1|0|f.clarity.ms/collect"}, {"name" : "_sctr", "value" : "1|1639296000000"}, {"name" : "ak_bmsc", "value" : "EE86859D951BD3A42F4250A0D06FC5D2~000000000000000000000000000000~YAAQLy0tF8QtYah9AQAAt2vNsA6y+iuYlE1IWEY8Hb6Us2n8h0sLuFY3j1j5XUCS3Q8R4sY1vacbyviY1/A0vPj/fGxs2KWimyqzhgKrGog6Rj+vDjB/6O2wfbrJ8u+1NEr7tzlyX8W3SDM3KWtNHIMdCqElXUDMaVloWqgI/faEZ7W5F0t9uP6XP+6uUz0nQxqwtsC3urSFuddf9os12NSpooMMxdCvuVyZOLete2ep9rWatTZcQRUkUL92mHLbmJiNip2POHaXO0LRze+tFKrwBMckkr2eOdV7YdD/BFdp3xJcWQQE+OUoY9jGhV8HJ4YHN8DoLndDQ5erK6oz9OSJTtyhZYuwHzhM+ucCUT21BS/Th8qMExfRsERXlB9P1PLpbHJaNwct65FyjmVuCwpdXvZhAykgVDfEoNtLwP0="}, {"name" : "_gat_hulu1", "value" : "1"}, {"name" : "_h_csrf_id", "value" : "215f6efc7c202b5e226d8023a82271c553bc1aa358a633e8e21f5f7d71fe2d85"}, {"name" : "_hulu_uid", "value" : "79292658"}, {"name" : "_hulu_e_id", "value" : "ggouWN02uTyBtt0g3MUEKQ"}, {"name" : "_hulu_bluekai_hashed_uid", "value" : "5a2f7702ee978755fcef5516f108e8ea"}, {"name" : "_hulu_assignments", "value" : "eyJ2MSI6W3siZSI6MTE0MSwidCI6MzE5NywibiI6InB0ZnVuLTE4NC1rdy10cmVhdG1lbnQifV19"}, {"name" : "_p_edit_token", "value" : "y5x_3Cwt4_rW1p0vX9kkkg"}, {"name" : "_hulu_dt", "value" : "vNSc2j56vCVp7FN5LU6GtTe8Cfk-/sPqgDcy/nJ2_EhP9ONXoQ--ryT2jvhbVahart1cE0/v3KjUZdo2xGrCTDBQRQry7lpBeyHNPimE2kczPpQpYBT53vpmbDDG9dgKeMZOJPyhm0hkOzcIRjn7LSsFhDSvcfBhK8q7KeKhOnl2fBtvI0DoZ9U3Vq4mfcWILJ1RsHAn1XpXbcAWpRJ881y77zIODoX3cFgsThnym/JKNPaAsGAIuHRS4OvxewB3kB5i/irlaMVrrNIM7WMCszR353BeCkk/Q0xDP0jTOy2Sp5FGxaYsVC7RlafNWUNmEkQnguw9Bq7Qfl95R/NG7nj5FJSMYGB1IQazVnsFNOHPFZmz3HxIrzp3EZNIusWbYHbpEFYfS3PoxJbuzJ6wc_B5xibajyM8F290GwJoPJauiQvKE3HWJmeELEI7GXpq_fhxZmL26h2v_CsfeH12k5mxdO8J2bflGhIRdLN1JG3P9hDCTsqkTckLSDAJHebJ5Ipm/WRF5/Jc9Z1sV2oGtLzJ74QLtkoCrHFv55MQaUNrx_t9u6WYrk33hEEc2nCnUVw_sgHY8yyPhOvnc_m3CK/NyJ5aRwQ4tYYbnvHTBjaJgmRD9nn_wqOntyXlEDqzlc9YjzBEEvJBvGspYFy0GU7/Szx1UcMQ8QyqcmnoAFXs5SFEq9891lxLjf2C/8Votxm5GbB0Dnu0w/Ce9V4zxCv55feAAcahIGHPHA7HMSxg67RgxITVqreeQaAzV_iR_zKrxtCrH8nhq3hsIFfWsdUIVCUpguuPjwfO77fM45L3Ne4TE/yRFfSGYp29S_q4EmdJEC30bVTfQgK5Puah_uOQXxdwR/lU/hVXXdF0pYkGd1oRTRHN67pUIDzK1B5JcN_L1H8wZdcUKIeLu0gUbrdOud2hX_kYiZ6DO6FtnHT2brU5pbAA7_O2O9qRrcnOJfm9Yun0PA--"}, {"name" : "_hulu_hbc", "value" : "1639349371710"}, {"name" : "XSRF-TOKEN", "value" : "781463f7-e28e-44ed-8558-c763e7a7594a"}, {"name" : "_hulu_pgid", "value" : "50339843"}, {"name" : "_hulu_plid", "value" : "3146728"}, {"name" : "_csrf_id", "value" : "0e9fb1523b2de0a4374c5b1e72745d0ca9aa31719c1d2c98ca1d1225d5f8233a"}, {"name" : "utag_main", "value" : "v_id:017db0cd63c7002277fd8d92b66605072001c06a00bd0$_sn:1$_ss:0$_st:1639351171901$ses_id:1639348790217;exp-session$_pn:2;exp-session$device_category:desktop;exp-session$_prevpage:/profiles;exp-1639352974259$k_sync_ran:1;exp-session$krux_sync_session:1639348790217;exp-session$g_sync_ran:1;exp-session$dc_visit:1$dc_event:1;exp-session$dc_region:us-east-1;exp-session$hhid:646fe35e69077a8afcdb650edfbc314c302c1036d847e8f2049ef6db4b52523b;exp-session"}, {"name" : "_hulu_session", "value" : "zNKnIllyYFIEtGN6RlgmcHy/qHw-F2RnOayNz/RGHkpgceK8jw--0l/wRrVDVp1F1eCfUybV929sxX9T1FAQ0GrCDJSKE8XbRl/PhoHr8ri/Nfp9HBfodxeXnqQ9G5gKNZMUZ/zpy96s0hf4Rbelsfnkjmf5sNtgInsYHAOnUjtMGaB6G/iWQydP81SyR4jjMv3moqLRMDDWMJZmAkhbS1tzkN9w8VB6_QorPI1hiyqCh1NuxCGpet5DJL4z944WS7mHXtfnQCM1jOYdDPsVxi_vzx0jYMIfiDe0HNpkRAf9NYtyfRdgr5J9lUpeNUtKL_eBEBv65p/H2ZKtS0RXRTV710MY_ZWN0lL8zbmQaOOFcq20du5XzOlZwU/7VWKa6GVMC5cATW5DqZHSokbWWOHAmuo/h2lcLdy3NGmWHHv7ByTbbUvtyYWsQGArFqFVdcCM5q7Dfbu3HCnOZ_foQDZGUqtNTvMQuQBzUixxtaGSznIfbsJyR1RkhY7j0PaGUzKmVeremmdjLmU6ee7kyQHXbHzi/ku01VVNeHL/gbpSf0Pw9w7nDAcEyDjx5mJCpfNZyQGmGVlgLbNiWMYdbqMS/HnZRXoHrmdPmc1fGC8a_ND2l3qhTN7Xdj95/PxfyHOJpeMfWCM1p_EqDEHFabvFb/QlbcoOjUtspzYXuVPMb9IjeujVPr720HtE2zDw5FymWBCyKeIvCW1Tb42RmRkJdGgHZ83fZjm2KbYm1Eb/S1UHaE7WgqU3d6mZSG2DwqIgg48vWuKU7Puy_/x2F8_6VyNvZkuf9L1BrFK1nPjqDvjN7N0CI2GstljM1h6BdcOymwe/WIx07G5qDIXvt2E4MF6yV3KMjqVi0PLYi_JaVJFXMxHY7EtbSA9n4fDpQ/XJbVKWTndv8Yfpm7T4OAISI1WoG8798ZRRXR4xFDHm3292Kli8suQXl0/Umkjyfvw_DoxwCr0CYMJWKAju5olh2uLikL6av4NGRLOOyUAeTMwMAQHfq/Q5ct00fKU9OJ3GgjPfswnl0w9QgS3rig/dYJYwllBmjQnV4LeHwY/1vS7z5UXvEx5P9wfKwUlBHDJd/mszukle4CuFGCsr_0DMd7rSK_1J72D5KM7SA8McVg7mh0Fd"}, {"name" : "_hulu_pid", "value" : "79292658"}, {"name" : "_hulu_pname", "value" : "Kaitlin"}, {"name" : "_hulu_is_p_kids", "value" : "0"}, {"name" : "_hulu_pprotect", "value" : "1639349374818"}, {"name" : "bm_sv", "value" : "7F778E16E9BA19170B2AD46611CBFAEF~eED3xPkZg5rSMU9bbDcsqbvce9bv+v9wIbTqbKn/b7m6tZPysOjafEO1HcxtRWCpVs2q08hgIY5zFQaRvpFTrIj3DoDbheAJIlYhU7P5WZZx71tM2R3+Q0iAufMV4oo1rC7uWvbRhdf1qyN/TP6LNQ=="}]'


import json

cookies = json.loads(newcookie)
#print(cookies)

for cook in cookies:
    #print(cook)
    try:
        browser.add_cookie(cook)
        #print('')
    except:
        print('err')
    time.sleep(0.5)
time.sleep(2)
browser.refresh()
time.sleep(2)


def download(mainurl, seasonlist):

    browser.get(mainurl)
    time.sleep(2)

    urls = []
    for season in seasonlist:
        first = browser.find_element_by_xpath('//*[@id="LevelTwo__scroll-area"]/div/div/div[4]/div/div[1]/div/div/div')
        first.click()
        first1 = browser.find_element_by_xpath('//*[@id="LevelTwo__scroll-area"]/div/div/div[4]/div/div[1]/div/div/div/ul')
        items = first1.find_elements_by_tag_name("li")
        for item in items:
            text = item.text
            if text == "Season " + str(season):
                el = item
                print(text)
        el.click()
        time.sleep(3)

        pagesource = browser.page_source
        #print(pagesource)

        pagesource = pagesource[0:pagesource.find('<div class="Nav__item">', pagesource.find('<div class="Nav__item">')+1)]
        pagetemp = pagesource
        tempstr = ''
        while(pagetemp.find('Cover art for') > -1):
            tempstr = pagetemp[0:pagetemp.find('Cover art for')]
            #print(tempstr[tempstr.rfind('/artwork/')+len('/artwork/'):tempstr.find('?', tempstr.rfind('/artwork/')+len('/artwork/'))])
            urls.append('https://www.hulu.com/watch/' + tempstr[tempstr.rfind('/artwork/')+len('/artwork/'):tempstr.find('?', tempstr.rfind('/artwork/')+len('/artwork/'))])
            pagetemp = pagetemp[pagetemp.find('Cover art for')+1:]



    browser.quit()



    for url in urls:
        print(url)
        string = 'cmd /c "C:\\Users\Kaitlin\Downloads\hulusubs_dl.exe --verbose -url ""' + url + '"""'
        os.system(string)
        time.sleep(1)




#download('https://www.hulu.com/series/vanderpump-rules-4aa54966-a0dd-4065-9b92-5ebd7f5e714a', [1,2,3,4,5,6,7,8])
download('https://www.hulu.com/series/the-bachelorette-15f2e58d-3734-4468-b785-e7b22eb97705', [19])
