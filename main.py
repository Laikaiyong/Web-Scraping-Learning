from bs4 import BeautifulSoup
import requests

LINK = ""

html_text = requests.get(LINK).text
soup = BeautifulSoup(html_text, 'lxml')

title_bar = soup.find_all("div", class_="list-card-content")

with open('./result/articles.csv', 'w') as file_writer:
    file_writer.write("title, link, author, created_time\n")
    for title in title_bar:
        title_extract = title.h4.text
        file_writer.write(title_extract + ', ')

        link_extract = title.find('a', recursive=False)['href']
        file_writer.write(link_extract + ', ')

        author = title.h6.find('a', recursive=False).text
        file_writer.write(author + ',')

        full_footer = title.h6.text.strip().split(',')
        date_extract = full_footer[1] + full_footer[2]
        file_writer.write(date_extract + '\n')