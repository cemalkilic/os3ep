# Author : Cemal Kılıç <cemalkilic96 [[at]] gmail.com>

from bs4 import BeautifulSoup

BASE_URL = "http://http://pages.cs.wisc.edu/~remzi/OSTEP/"

with open("html_data.txt", "r") as file:
    html_doc = file.read()

soup = BeautifulSoup(html_doc, 'html.parser')

rows = soup.find("table").find_all("tr")

for row in rows:
    for cell in row.find_all("td"):
        number = cell.find("small")
        link = cell.find("a")
        if number is not None and link is not None:
            seq_number = number.text
            file_name = seq_number.zfill(2) + "-"  + link['href']
            download_link = BASE_URL + link['href']
            print(download_link)
            print(file_name)


