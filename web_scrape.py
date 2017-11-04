import urllib2
from bs4 import BeautifulSoup

url = "http://lhs-sfusd-ca.schoolloop.com"

request = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
page = urllib2.urlopen(request)
soup = BeautifulSoup(page, 'html.parser')

name_box = soup.find('table', attrs={'style': 'color;#000080;'})
name = name_box.text.strip()
print name
