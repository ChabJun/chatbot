import requests as req
from bs4 import BeautifulSoup
import re

#day = input()

day = '20180126'


url = "http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0046&date=" + day



def time_table(url) :

    response = req.get(url)

    #print(response.status_code)
    #print(response.encoding)

    time = BeautifulSoup(response.text, 'html.parser')

    data = time.find_all('em')

    #print(data)

    for i in data :
        s1 = i.get_text(strip=True)
        if re.search("\d+:\d+", s1) :

            if int(s1[0:2]) >= 22 :
                print(s1)
time_table(url)


