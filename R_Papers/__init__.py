#-----------------------------------------------------------------------------------------------------#
#--For IEEE site--#
import json
import _json
import requests
from urllib.parse import urlencode, quote_plus

#----------For iee site----------#
OUTPUT = './Data/ResearchPapers.html'
URL1 = 'https://ieeexplore.ieee.org/rest/search'
HEADERS1 = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText=security',
    'Content-Type': 'application/json',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
}
#----------For science open site----------#
FILENAME2 = './Data/ResearchData.json'
URL2 = 'https://www.scienceopen.com/search-servlet'
HEADERS2 = {
    'Connection':'keep-alive',
    'Accept':'*/*',
    'Origin':'https://www.scienceopen.com',
    'X-Requested-With': 'XMLHttpRequest',
    'Sec-Fetch-Dest': 'empty',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://www.scienceopen.com/search',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'
}
DATA2 = {
    'kind':'61',
    'itemsToGet':'10',
    'firstItemIndex':'0',
    'getFacets':'false',
    'getFilters':'true',
    'search':'{SUB}',
}
SUB = {
        "v":"3",
        "id":"",
        "isExactMatch":"true",
        "context":"null",
        "kind":"77",
        "order":"0",
        "orderLowestFirst":"false",
        "query":"{QUERY}"
        }

f = open(OUTPUT,'w')
# IEEE #
def ieeeSite(TOPIC):
    print("Getting Research: IEEE")
    DATA1 ='{"newsearch":true,"queryText":"'+TOPIC+'","highlight":true,"returnFacets":["ALL"],"returnType":"SEARCH"}'
    response = requests.post(url = URL1, headers = HEADERS1,  data = DATA1)
    response=response.json()
    i=0
    f.write('<!DOCTYPE html>\n<html>\n<body>\n<h1>Research Papers</h1>\n<h2>IEEE</h2><br>')   
    for article in response['records']:
        i = i+1
        if i == 20:
            break;
        f.write('<ol><a href="' + 'https://ieeexplore.ieee.org' + article['documentLink'] + '">' + article['articleTitle'] + '</a></ol><br>')

# Sciece open #
def parseData():
    fp = open(FILENAME2)
    obj = json.load(fp)
    f.write('\n')
    f.write('<h2>Science Open</h2><br>')
    for i in obj['result']['results']:
        f.write(f'<ol><a href={i["_url"]}> {i["_titleSafe"]} </a></ol><br>')
    f.write('</body></html>')

def scOpen(QUERY):
    print("Getting Research: ScienceOpen")
    TEST = f"q=%7B%22kind%22%3A61%2C%22itemsToGet%22%3A20%2C%22firstItemIndex%22%3A0%2C%22getFacets%22%3Afalse%2C%22getFilters%22%3Atrue%2C%22search%22%3A%7B%22v%22%3A3%2C%22id%22%3A%22%22%2C%22isExactMatch%22%3Atrue%2C%22context%22%3Anull%2C%22kind%22%3A77%2C%22order%22%3A0%2C%22orderLowestFirst%22%3Afalse%2C%22query%22%3A%22{QUERY}%22%2C%22filters%22%3A%5B%7B%22kind%22%3A86%2C%22offset%22%3A1%2C%22timeUnit%22%3A5%2C%22%24timezoneOffset%22%3A-19800000%7D%5D%7D%7D"
    r = requests.post(url = URL2 , headers = HEADERS2 , params = TEST )
    with open(FILENAME2, "w") as f2:
        x = r.content.decode()
        f2.write(x)
    parseData()
    f.close()
