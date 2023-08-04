from cookies import COOKIE_NAME, COOKIE_VALUE

import requests
import pandas as pd
from bs4 import BeautifulSoup

URL = "https://icts.kuleuven.be/masterproeven/student/targetgroups/1158"
cookies = {COOKIE_NAME: COOKIE_VALUE}
page = requests.get(URL, cookies=cookies)
parsed_page = BeautifulSoup(page.content, "html.parser")

topics = parsed_page.find_all(class_="subject-card")

topic_info = []

for topic in topics:

    result = []
    title_element = topic.find("h6", class_="title")
    title = title_element.text.strip()
    result.append(title)

    other_elements = topic.find_all("div", class_="element-text")
    for element in other_elements:
        result.append(element.text.strip())
    
    btn = topic.find("div", class_="btn-detail")
    detail_url = btn.find("a", class_="detail")
    result.append(detail_url["href"])
    topic_info.append(result)

data = {
    'Title': [],
    'Promotor': [],
    'Co-promotor': [],
    'Target groups': [],
    'Disciplines': [],
    '#students': [],
    'link': []
}

for row in topic_info:
    data['Title'].append(row[0])
    data['Promotor'].append(row[1])
    if len(row) == 6:
        data['Co-promotor'].append("")
        data['Target groups'].append(row[2])
        data['Disciplines'].append(row[3])
        data['#students'].append(row[4])
        data['link'].append(row[5])
    elif len(row) == 7:
        data['Co-promotor'].append(row[2])
        data['Target groups'].append(row[3])
        data['Disciplines'].append(row[4])
        data['#students'].append(row[5])
        data['link'].append(row[6])

df = pd.DataFrame(data)
print(df)