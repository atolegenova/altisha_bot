# import requests
# from bs4 import BeautifulSoup
#
# response = requests.get('https://www.kloop.kg/').text
#
#
# soup = BeautifulSoup(response, 'html.parser')
# posts = soup.find_all('a', class_='elementor-post__thumbnail__link')
# links = []
# for p in posts:
#     href = p.get('href')
#     links.append(href)
# for i in links:
#     r = requests.get(i).text
#     post = BeautifulSoup(r, 'html.parser')
#     h = post.find('h1').text
#     print(h)
import requests
from bs4 import BeautifulSoup



def get_news():
    response = requests.get('https://kloop.kg/').text

    soup = BeautifulSoup(response, 'html.parser')
    posts = soup.find_all('a', class_='elementor-post__thumbnail__link')
    links = []
    news = []

    for p in posts:
        href = p.get('href')

        links.append(href)
    # for i in links:
    #     r = requests.get(i).text
    #     post = BeautifulSoup(r, 'html.parser')
    #     h = post.find('h1').text
    #     #p = post.find_all('p', class_='stk-reset wp-exclude-emoji')
    #     # text = ''
    #     # for x in p:
    #     #     t = x.text
    #     #     text += t
    #     news.append(f"{i} \n{h}")
    # return news
    return links

list_news = get_news()
