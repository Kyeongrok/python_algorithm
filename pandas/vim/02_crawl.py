from urllib.request import urlopen
url = "http://www.krei.re.kr:18181/chart/main_chart/index/kind/W/sdate/1972-01-01/edate/2018-11-24"
text = urlopen(url)
file = open("./grains.json", "w+")
file.write(str(text.read()))