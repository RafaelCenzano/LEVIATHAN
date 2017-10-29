import urllib2
from bs4 import BeautifulSoup
from html.parser import HTMLParser

url = "http://lhs-sfusd-ca.schoolloop.com"

req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
con = urllib2.urlopen( req )
#print con.read()

soup = BeautifulSoup(htmlfile, 'html.parser')

codes = soup.find_all('span')[49]
print codes[2]
print(soup.get_text())
