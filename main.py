import urllib.request
import urllib.parse
import re

import requests
import base64
import json
from bs4 import BeautifulSoup

drooble = "https://drooble.com/"


# Url and Request Headers of drooble function

# Extras from credCheckHeader
"""
    ":authority": "drooble.com",
    ":method": "POST",
    ":path": "/api/dt/checkCredentials",
    ":scheme": "https",
"""

credCheck = "https://drooble.com/api/dt/checkCredentials"
credCheckHeader = { "accept": "application/json",
                    "accept - encoding": "gzip, deflate, br",
                    "accept - language": "en-GB,en-US;q=0.9,en;q=0.8",
                    "content - length": "69",
                    "content - type": "application/json",
                    "cookie": "__cfduid=dc0771eaf20713173f46e22ec3b2d035f1610627564; drbfp=1610627566.2114; drbanon=73c677a036efda214e05f0ea9cc9f32a; lang=en; lng=en; drbl-last-locale-get-en=1608031159; mp-lpe=2184410; forward_segment=1; SgSut=2021-01-14; asrc=b2ZHeVA5c2NUZ3ZNYW9MeDZVbUVVU2pOOVJCQmI0NVFpcXJGSmE5d2EvdVNrdVExbWFESVBqL0lldDFCWlh1Kzo6JHHTYfmsm3HDPsqx2Yq1mg%3D%3D; DrbS=_prod_DB_O_NULL_f81363533a58090c56ff98e6631a5936",
                    "origin": "https://drooble.com",
                    "referer": "https://drooble.com/",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "sec-gpc": "1",
                    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}

logoutUrl = "https://drooble.com/api/dt/logout"

# Extras from logoutHeaders
"""
    ":authority": "drooble.com",
    ":method": "POST",
    "path": "/api/dt/logout",
    ":scheme": "https",
"""

logoutHeaders = {
    "accept": "application/json",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "content-length": "0",
    "content-type": "application/json",
    "cookie": "__cfduid=dc0771eaf20713173f46e22ec3b2d035f1610627564; drbfp=1610627566.2114; drbanon=73c677a036efda214e05f0ea9cc9f32a; lang=en; lng=en; drbl-last-locale-get-en=1608031159; mp-lpe=2184410; forward_segment=1; DrbS=_prod_DB_I_98918_6369dc4fa1f1551ede9eef00ffe8c321; DrbC=em163c7caf5acb52efdc79fe9c89756112; asrc=ckZ3Ukl6dnRrZW90cVFYRFhKSGttbm9CUVZPeEVPRjdlaXd5clRhOG1RKzN6a0NGSnEvVmM3NTM5Y0xWVmRpLzo6NQt78CcqiC44kwF%2Bn4NGfg%3D%3D; SgSut=2021-01-14",
    "origin": "https://drooble.com",
    "referer": "https://drooble.com/dashboard/overview",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sec-gpc": "1",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
}

username = "waltercortz12@gmail.com"
password = "1998walter12"

values = {  "user": username,
            "pass": password,
            "remember": 1}

data = urllib.parse.urlencode(values)
data = data.encode("utf-8")

ses = requests.Session()

# Log into Drooble
success = True
try:
    login = ses.post(url=credCheck, headers=credCheckHeader, data=values)
    print(f"Login to {username} successful")
except Exception as e:
    print(f"Failed to login to {username}")
    success = False
    print(str(e))

# Retrieve Reviews
if success == True:
    pass


# Logout
if success == True:
    try:
        logout = ses.post(url=logoutUrl, headers=logoutHeaders)
        print("Logged Out Successfully")
    except Exception as e:
        print("Failed to LogOut")
        success = False
        print(str(e))