from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())

    data_title = soup.find_all('dt')
    small_titles = [
        tag.p.text
        for tag in data_title
    ]
    print(small_titles)