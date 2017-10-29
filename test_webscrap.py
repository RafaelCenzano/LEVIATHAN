import urllib2
from bs4 import BeautifulSoup

url = "http://lhs-sfusd-ca.schoolloop.com"

req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
con = urllib2.urlopen( req )
print con.read()

#soup = BeautifulSoup(page)

#print soup.prettify()
