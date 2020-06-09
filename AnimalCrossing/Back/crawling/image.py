import requests
import bs4
import os
import urllib.request
# 폴더 생성하기
try:
    if not (os.path.isdir('image_animal')):
        os.makedirs(os.path.join('image_animal'))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 생성 실패!")
        exit()

# 403 에러때문에 헤더에 다음과 같은 처리를 해주면 오류가 안뜸!!

opener=urllib.request.build_opener()

opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]

urllib.request.install_opener(opener)

URL = "https://namu.wiki/w/%EB%8F%99%EB%AC%BC%EC%9D%98%20%EC%88%B2%20%EC%8B%9C%EB%A6%AC%EC%A6%88/%EC%9D%BC%EB%B0%98%20%EC%A3%BC%EB%AF%BC?from=%EB%8F%99%EB%AC%BC%EC%9D%98%20%EC%88%B2%20%EC%8B%9C%EB%A6%AC%EC%A6%88%2F%EB%93%B1%EC%9E%A5%20%EC%A3%BC%EB%AF%BC%20%EC%9D%BC%EB%9E%8C"
response = requests.get(URL)
html = response.text
soup = bs4.BeautifulSoup(html, 'html.parser')

paragraph_data = soup.find_all('td')

li_list = []
for data1 in paragraph_data:
    #img 영역 추출
    li_list.extend(data1.findAll('img')) 
#해당 부분을 찾아 li_list와 병합 <태그 자체로 들어가 있을 듯>
#각각 이미지 URL과 이름 추출하기

for li in li_list:
    names = li['alt'].split('_') # ['a','c']
    title = names[0][3:]
    if title == '동숲':
        title = names[1]
    if '-' in title:
        title = title.split('-')[1]
    print(title)
    img_src = li['src']
    urllib.request.urlretrieve( 'https:' + img_src , './image_animal/' + title+'.png') # 어디서 불러올 것인가, 경로 + 파일명
# url = 이미지 url
# urllib.request.urlretrieve(url, '경로/파일 이름')
