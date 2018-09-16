# Author : Cemal Kılıç <cemalkilic96 [[at]] gmail.com>

from bs4 import BeautifulSoup
from urllib.request import urlopen
from concurrent.futures import *
import argparse

# base url for downloading the files
BASE_URL = "http://pages.cs.wisc.edu/~remzi/OSTEP/"

def download_pdf(url, file_name):
    response = urlopen(url)
    file = open(file_name, 'wb')
    file.write(response.read())
    file.close()
    print("File downloaded: " + file_name)
    
def parse_table():
    # get the table and parse it
    with open("html_data.txt", "r") as file:
        html_doc = file.read()
        
    soup = BeautifulSoup(html_doc, 'html.parser')
    rows = soup.find("table").find_all("tr")
    urls = []

    for row in rows:
        for cell in row.find_all("td"):
            number = cell.find("small")
            link = cell.find("a")
            # if cell includes both <a> and <small> tag,
            # we download it            
            if number is not None and link is not None:
                # seq_number for ordering the downloaded files
                seq_number = number.text
                # file_name consists of seq number and the original name itself
                file_name = seq_number.zfill(2) + "-"  + link['href']
                download_link = BASE_URL + link['href']
                url = {"link" : download_link, "file_name" : file_name}
                urls.append(url)
    return urls

def download_multithread(urls, number_of_threads):
    with ThreadPoolExecutor(max_workers=number_of_threads) as executor:
        future_list = {executor.submit(download_pdf, url['link'], url['file_name']): url for url in urls}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download pdfs for the free' +
    ' book Operating System Three Easy Pieces...')
    parser.add_argument("-t", "--threads", action="store", type=int,
    dest="number_of_threads", default=4, help='Number of threads')

    args = parser.parse_args()
    
    urls = parse_table()
    download_multithread(urls, args.number_of_threads)
