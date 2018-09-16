# Author : Cemal Kılıç <cemalkilic96 [[at]] gmail.com>

from bs4 import BeautifulSoup

with open("html_data.txt", "r") as file:
    html_doc = file.read()

soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())
