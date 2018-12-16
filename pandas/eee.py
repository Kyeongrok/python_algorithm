import requests
from bs4 import BeautifulSoup
url = "http://www.netd.ac.za/portal/?option=Keyword&query=indigenous+knowledge&modifier1=OR&option1=Keyword&query1=ecological+knowledge&modifier2=OR&option2=Keyword&query2=traditional+knowledge&modifier3=NOT&option3=Keyword&query3=indigenous&action=advancedsearch"
result = requests.get(url)

print(result.content)
bs_obj = BeautifulSoup(result.content, "html.parser")
ol = bs_obj.find("ol", {"start":"1"})
lis = ol.findAll("li")
urlPrefix = "http://www.netd.ac.za/portal/"
for li in lis:
    subUrl = urlPrefix + li.find("a")["href"]
    print(subUrl)