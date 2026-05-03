import requests
import time
from bs4 import BeautifulSoup
from utils import check_and_create_result
URL = "https://habr.com/ru/feed/"
#article header # article link #article views #article tags
def parse_article(soup):
    articles_list = soup.find_all('article', class_='tm-articles-list__item')
    print(F'Parsing articles..., find{len(articles_list)} articles')
    data= []

    for article in articles_list:
        header = articles.find("h2", class_="tm-title")
        if header == None:
            raise ValueError('article do not have header, SKIP')
        header_text = header.find('span').text
        article_link = header.find('a').attrs['href']
        article_views = article.find('span', class_='tm-icon-counter__value').text
        dara.append({'header_text': header_text, 'article_link': article_link, 'article_views': article_views})

    return data

    #article_tags = list(map(lambda tag: tag.find('span').text, article.find('div', class_='tm-publication_hub')))
    
def main():
    req = requests.get(URL, headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
        
    })
    if req.status_code == 200:
        
        with open('test.html', 'wb') as f:
            f.write(req.content)
        soup = BeautifulSoup(req.content, 'html.parser')
        parsed_articles = []
        for a in articles_list:
            try:
                parsed_articles.append(parse_article(a))
            except ValueError as e:
                print(e)

    
    pages = soup.find_all('a', class_='tm-pagination__page')
    print(f'Found {pages[-1]} pages')
    print(pages)

    need_pages = min(5,pages)

    for i in range(2, int(pages[-1].text) + 1):
        url = 'https://habr.com/ru/feed/page{i}'
        print(f'Parsing page {i}...')

        time.sleep(5)
        req = requests.get(URL, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36'})
        if req.status_code == 200:
            try:
                parsed_articles.append(parse_article(soup))
            except ValueError as e:
                print(e)
        else:
            print(f'Parsing page {i} error SKIP')
            continue

        result_path = check_and_create_result()
        with open(f'{result_path}/habr-result-{time.time()}.txt', 'a', encoding='utf-8') as f:
            for a in parsed_articles:
                f.write(f'header:{a["header_text"]}\nviews:{a["article_views"]}\nlink: https://habr.com/ru{a["article_link"]}\n')

if __name__ == '__main__':
    main()