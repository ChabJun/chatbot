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

    data = time.find_all(['strong','em'])

    #print(data)

    for i in data :
        s1 = i.get_text(strip=True)
        #print(s1)
        
        if re.search("\d+:\d+", s1) :

            if int(s1[0:2]) >= 22 :
                print(s1)
                
        elif re.search("[\w]+", s1) :
            print(s1)
    
def movie_table(url) :

    response = req.get(url)

    movie = BeautifulSoup(response.text, "html.parser")

    data = movie.find_all('div', class_='col-times')

    for i in data :

        strong = i.find('strong')
        print(strong.get_text(strip=True)) # title
        time = i.find_all('div' ,class_='info-timetable')
        
        #time = i.find_all('em')
        #seat = i.find_all('span', class_='early txt-lightblue')
        
        for t in time :

            s1 = t.get_text(strip=True)

            s1 = s1.replace('좌석', '')

            for n in s1.split('석') :

                if n == '' :
                    continue
                
                if int(n[0:2]) >= 22 :
                    n = n.replace('잔여', ' 잔여')
                    print(n)


            
        
        
#time_table(url)
movie_table(url)

## 영화 없는 제목 빼기


