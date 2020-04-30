import requests
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning

URL = "https://news.google.com/topics"
FILENAME = "Data/news.html"

def getNews():
    print('Getting News from: Google News')
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    r = requests.get(url = URL , verify = False)
    soup = BeautifulSoup(r.content,'html.parser')
  
    with open(FILENAME,'w+') as f:
        f.write('<!DOCTYPE html>\n<html>\n<body>\n<h1> News Links</h1>\n')
        for i in soup.find_all('a', href =  True):
            pp = i.string
            aaa = str(i)
            if "articles" in aaa and pp != None:
                cool = i['href']
                i['href'] = 'https://news.google.com'+cool[1:]
                f.write('* ' +'<ol><a href="'+str(i['href'])+' "a>' + str(pp) + '</a></ol>\n')
            else:
                continue
        f.write('</body>\n</html>')
    f.close
