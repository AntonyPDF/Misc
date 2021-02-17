import requests
import pyperclip

def ip():
    r = requests.get('https://ipinfo.io/json')
    return r.json()['ip']

a = ip()
b = ':25565'
c = a+b

pyperclip.copy(c)