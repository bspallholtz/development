#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup

url = 'http://tmp-auth.slb.sfdc.net/saml_tmp/'

try:
  reqs = requests.get(url, timeout=1)
except:
  print("Failed to auth to end {end}".format(end=url))
  print("Are you connected to the VPN?")
  exit(1)

soup = BeautifulSoup(reqs.text, 'lxml')

for heading in soup.find_all(["h1"]):
    if heading.text.strip() != 'Authenticated!':
       print('Failed to authenticate')
    else:
       print('Authenticated')
