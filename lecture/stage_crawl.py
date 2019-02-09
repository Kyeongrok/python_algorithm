from libs.crawler import crawl
from libs.parser import parse

url = "https://ezone.idexuae.ae/exhibitors-list-json/1/name/_all_/F"
result = crawl(url)
bsobj = parse(result)
print(bsobj)
