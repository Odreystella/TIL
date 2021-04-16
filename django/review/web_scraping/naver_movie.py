import requests
from bs4 import BeautifulSoup

# 영화를 리스트 출력 함수
def get_movie_list():
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

    return movies_list

movies_list = get_movie_list()
# print(movies_list)

# 영화 제목 입력하면 code를 출력하는 함수
def get_movie_code(movie_title):
    for movie in movies_list:
        if movie_title == movie['movie_title']:
            return movie['code']

print(get_movie_code('서복'))
movie_code = get_movie_code('서복')

# 영화 코드를 입력하면 리뷰를 출력하는 함수
def get_review_of_movie():

    headers = {
        'authority': 'movie.naver.com',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        'sec-ch-ua-mobile': '?0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'iframe',
        'referer': 'https://movie.naver.com/movie/bi/mi/point.nhn?code=159074',
        'accept-language': 'en-US,en;q=0.9,ko;q=0.8',
        'cookie': 'NRTK=ag#all_gr#1_ma#-2_si#0_en#0_sp#0; NNB=WPUBCSBSZUHGA; ASID=6af24fe6000001774c0e192700005e55; _fbp=fb.1.1612100117041.1815354310; _ga=GA1.2.867914976.1612100117; nx_ssl=2; notSupportBrowserAlert=true; BMR=s=1618539655670&r=https%3A%2F%2Fm.blog.naver.com%2Fsamojun%2F221766166563&r2=https%3A%2F%2Fwww.google.com%2F; NV_WETR_LOCATION_RGN_M="MDkxNDAxMDQ="; NV_WETR_LAST_ACCESS_RGN_M="MDkxNDAxMDQ="; page_uid=hcCibwp0YidssPPKn2NssssstMo-105488; csrf_token=cbf59227-d901-4d10-b024-89ef04ca33fc',
    }

    params = (
        ('code', '159074'),
        ('type', 'after'),
        ('isActualPointWriteExecute', 'false'),
        ('isMileageSubscriptionAlready', 'false'),
        ('isMileageSubscriptionReject', 'false'),
    )

    response = requests.get('https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn', headers=headers, params=params)


    


    


    
