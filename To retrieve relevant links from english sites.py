__author__ = 'Xuan'
import csv
from bs4 import BeautifulSoup
#import lxml.html
import urllib
import re
import requests

session = requests.Session()
headers = {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53",
           "Accept":"text/html, application/xhtml+xml,application/xml; q=0.9,image/webp,*/*;q=0.8"}


with open('sites2.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        url = ''.join(row)
        page = urllib.urlopen(url)
        soup = BeautifulSoup(page.read(), "lxml")
        filename = "output_n28.txt"
        with open(filename, 'a') as g:
            for link in soup.find_all('a'):
                text = link.get_text()
                matchOBJ = re.search("China",text)
                if (matchOBJ):
                    my_text = link.get_text()
                    g.write(my_text.encode('utf8')),
                    g.write("|"),
                    my_href = link.get('href')
                    g.write(my_href.encode('utf8')),
                    g.write("\n")
                my_regex = re.findall(r'.{50,50}property.market.{50,50}', str(soup))
                for eachP in my_regex:
                    g.write(eachP),
                    g.write("|"),
                    g.write("\n")
