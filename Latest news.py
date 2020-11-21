from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

link = "https://www.financialexpress.com/india-news/"
data = urlopen(link)

data_html = data.read()

data_soup = soup(data_html, "html.parser")
newz = data_soup.findAll("h3")
print('''      There are {} news as follow;;
                        '''.format(len(newz)))
for i in newz:
    print(">> {}".format(i.text))

print('''
              Have a nice day ;)''')