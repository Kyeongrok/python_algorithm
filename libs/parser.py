from bs4 import BeautifulSoup
def parse(string):
    bsObj = BeautifulSoup(string, "html.parser")
    print(bsObj)