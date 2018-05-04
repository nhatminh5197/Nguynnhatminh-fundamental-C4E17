from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "https://www.apple.com/itunes/charts/songs/"

conn = urlopen(url)
raw_data = conn.read()
text = raw_data.decode('utf8')

itune_file = open("itune.html","wb")
itune_file.write(raw_data)
itune_file.close()

soup = BeautifulSoup(text,"html.parser")
ul = soup.find("div",id="main")
li_list = ul.find_all("li")
item_list = []
for li in li_list:
    a = li.h4.a
    title = a.string
    link = url + a['href']
    item = {
        "Title":title,
        "link": link,

    }
    item_list.append(item)

import pyexcel
pyexcel.save_as(records = item_list, dest_file_name = "itune.xlsx")
