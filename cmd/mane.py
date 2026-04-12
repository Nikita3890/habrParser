import requests
URL_1 = 'https://www.python.org/'
URL_2 = 'https://www.wikipedia.org/'

def main():
    req = requests.get(URL_2)
    if req.status_code == 200:
        print(req.headers)
        print(req.text)
        with open('req.html', 'wb') as f:
            f.write(req.content)
    else:
        print(f'Ошибка запроса\n Status Code:{req.status_code}')
        with open('req.html', 'wb') as f:
            f.write(req.content)
if __name__ == '__main__':
    main()
