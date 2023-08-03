from cookies import COOKIE_NAME, COOKIE_VALUE

import requests
from bs4 import BeautifulSoup

URL = "https://icts.kuleuven.be/masterproeven/student/targetgroups/1158"

cookies = {COOKIE_NAME: COOKIE_VALUE}

page = requests.get(URL, cookies=cookies)

soup = BeautifulSoup(page.content, "html.parser")

topic_table = soup.find(id="selectsubject")

topics = topic_table.find_all(class_="subject-card")

for topic in topics:
    title_element = topic.find("h6", class_="title")
    title = title_element.text.strip()

    other_elements = topic.find("div", class_="element-text")
    


