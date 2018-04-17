import urllib
import re
import requests
import MySQLdb
import os
import argparse
from bs4 import BeautifulSoup
from array import *

parser = argparse.ArgumentParser()
parser.add_argument("--url","-u", help="URL Adresi Yaziniz (http://example.com)")

args = parser.parse_args()
url = args.url

r  = requests.get(url)
data = r.text
soup = BeautifulSoup(data)

description = soup.find_all('meta',attrs={'name':'description'})
keywords = soup.find_all('meta',attrs={'name':'keywords'})
title = soup.find_all('title')

for desc in description:
    for key in keywords:
        for tt in title:

            db = MySQLdb.connect(host="localhost",user="root", passwd="root", db="root")
    db.set_character_set('utf8')
    insert_stmt = (
      "INSERT INTO icerik (url, description, keywords, title) "
      "VALUES (%s, %s, %s, %s)"
    )
    data=(url,desc,key,tt)
    cur = db.cursor()
    cur.execute(insert_stmt, data)
    db.commit()
