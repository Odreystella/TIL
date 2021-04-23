import requests
from bs4 import BeautifulSoup
import csv

# 영화를 리스트 출력 

# get할 url가져와서 response에 담기
url = 'https://movie.naver.com/movie/running/current.nhn'
response = requests.get(url)
# print(response)

# response에 담긴 내용의 text를 BeautifulSoup를 이용해서 soup 객제 만들기
soup = BeautifulSoup(response.text, 'html.parser')
# 영화 제목이 있는 ul 안의 li태그들만 가져오기
li_list = soup.select('#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li')

movies_list = []
for li in li_list:
    movie_title = li.select_one('dl > dt > a').text
    code = li.select_one('dl > dt > a')['href'].split('?code=')[1]
    
    # movies_list에 들어갈 데이터 셋 딕셔너리로 만들어주기
    movie = {
        'movie_title' : movie_title,
        'code' : code
    }
    movies_list.append(movie)

# print(movies_list)


with open('./reviews.csv', 'w', newline='') as c:
    fieldnames = ['movie_title', 'code']
    writer = csv.DictWriter(c, fieldnames=fieldnames)
    
    writer.writeheader()
    
    for movie in movies_list:
        writer.writerow(movie)
               

# with open('./reviews.csv', newline='') as c:
#     reader = csv.DictReader(c)
#     for row in reader:
#         print(row['movie_title'], row['code'])
