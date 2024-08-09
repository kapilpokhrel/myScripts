import requests
import time

URL = 'https://10.100.1.1:8090/login.xml'

# Change username and password as necessary

DATA = {
    'mode':191,
    'username':'********',
    'password':'********',
    'a':int(time.time()),
    'producttype':0
}

headers = {
    'Accept': '*/*',
    'Accept-Encoding':'gzip, deflate, br, zstd',
    'Accept-Language':'en-US,en',
    'Cache-Control':'no-cache',
    'Connection':'keep-alive',
    'Content-Type':'application/x-www-form-urlencoded'
}

requests.post(URL, data=DATA, headers=headers, verify=False)
