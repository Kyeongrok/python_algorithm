string = '20200305-08:13:51.913 [10]   [OUT] 8=FIXT.1.1|9=1528|35=y|49=TRADS|56=CACIB_MDF|34=2|52=20200305-08:13:51.913|320=SecReqId1583396031899|322=FIXT.1.1:TRADS->CACIB_MDFSecReqId1583396031899|560=0|393=1803|893=N|146=10|55=ANZ 3.45 08/22 c|48=XS0813493631|22=8|454=1|455=XS0813493631|456=4|167=CORP|762=NONE|223=3.45|107=2022-08-08|1151=VARIABLE|15=USD|423=1|55=IAGAU 5.625 12/26 £|48=XS0279568231|22=8|454=1|455=XS0279568231|456=4|167=CORP|762=NONE|223=5.625|107=2026-12-21|1151=NONE|15=GBP|423=1|55=NAB 4.625 02/20|48=XS0485326085|22=8|454=1|455=XS0485326085|456=4|167=CORP|762=NONE|223=4.625|107=2020-02-10|1151=FIXED|15=EUR|423=1|55=ASRIIJ 6.95 20|48=USY00371AA53|22=8|454=1|455=USY00371AA53|456=4|167=CORP|762=NONE|223=6.95|107=2020-03-27|1151=FIXED|15=USD|423=1|55=BHARTI 5.125 23 $|48=USN1384FAA32-$|22=8|454=1|455=USN1384FAA32|456=4|167=CORP|762=NONE|223=5.125|107=2023-03-11|1151=FIXED|15=USD|423=1|55=BJCAPT 8.375 49|48=XS0910884955|22=8|454=1|455=XS0910884955|456=4|167=CORP|762=NONE|223=8.375|107=2049-04-29|1151=VARIABLE|15=USD|423=1|55=CITLTD 6.375 20 $|48=XS0912154381|22=8|454=1|455=XS0912154381|456=4|167=CORP|762=NONE|223=6.375|107=2020-04-10|1151=FIXED|15=USD|423=1|55=CITLTD 8.625 49 $|48=EJ6772689|22=8|454=1|455=XS0933855354|456=4|167=CORP|762=NONE|223=8.625|107=2049-05-29|1151=VARIABLE|15=USD|423=1|55=EIBKOR 2 20 ¬|48=XS0925003732|22=8|454=1|455=XS0925003732|456=4|167=CORP|762=NONE|223=2|107=2020-04-30|1151=FIXED|15=EUR|423=1|55=FDCPM 4.25 20|48=XS0894336907|22=8|454=1|455=XS0894336907|456=4|167=CORP|762=NONE|223=4.25|107=2020-04-02|1151=FIXED|15=USD|423=1|10=131|'
string = '20200305-08:13:51.913 [10]   [OUT] 8=FIXT.1.1|9=1528|35=y|49=TRADS|56=CACIB_MDF|34=2|52=20200305-08:13:51.913|322=FIXT.1.1:TRADS->CACIB_MDFSecReqId1583396031899|560=0|393=1803|893=N|320=SecReqId1583396031899|146=10|55=ANZ 3.45 08/22 c|48=XS0813493631|22=8|454=1|455=XS0813493631|456=4|167=CORP|762=NONE|223=3.45|107=2022-08-08|1151=VARIABLE|15=USD|423=1|55=IAGAU 5.625 12/26 £|48=XS0279568231|22=8|454=1|455=XS0279568231|456=4|167=CORP|762=NONE|223=5.625|107=2026-12-21|1151=NONE|15=GBP|423=1|55=NAB 4.625 02/20|48=XS0485326085|22=8|454=1|455=XS0485326085|456=4|167=CORP|762=NONE|223=4.625|107=2020-02-10|1151=FIXED|15=EUR|423=1|55=ASRIIJ 6.95 20|48=USY00371AA53|22=8|454=1|455=USY00371AA53|456=4|167=CORP|762=NONE|223=6.95|107=2020-03-27|1151=FIXED|15=USD|423=1|55=BHARTI 5.125 23 $|48=USN1384FAA32-$|22=8|454=1|455=USN1384FAA32|456=4|167=CORP|762=NONE|223=5.125|107=2023-03-11|1151=FIXED|15=USD|423=1|55=BJCAPT 8.375 49|48=XS0910884955|22=8|454=1|455=XS0910884955|456=4|167=CORP|762=NONE|223=8.375|107=2049-04-29|1151=VARIABLE|15=USD|423=1|55=CITLTD 6.375 20 $|48=XS0912154381|22=8|454=1|455=XS0912154381|456=4|167=CORP|762=NONE|223=6.375|107=2020-04-10|1151=FIXED|15=USD|423=1|55=CITLTD 8.625 49 $|48=EJ6772689|22=8|454=1|455=XS0933855354|456=4|167=CORP|762=NONE|223=8.625|107=2049-05-29|1151=VARIABLE|15=USD|423=1|55=EIBKOR 2 20 ¬|48=XS0925003732|22=8|454=1|455=XS0925003732|456=4|167=CORP|762=NONE|223=2|107=2020-04-30|1151=FIXED|15=EUR|423=1|55=FDCPM 4.25 20|48=XS0894336907|22=8|454=1|455=XS0894336907|456=4|167=CORP|762=NONE|223=4.25|107=2020-04-02|1151=FIXED|15=USD|423=1|10=131|'


import re

def get_matched_text(pattern, text):
    matches = re.findall(pattern, text)
    result = []
    for match in matches:
        result.append(match)
    return result

list = get_matched_text('(320=[a-zA-Z0-9]+|893=[A-Z]+)', string)

re_order = []
for item in list:
    print(item, type(item))

def fn1(list, regexr):
    print('fn1', regexr)
    pass

def fn2():
    print('y fn2')
    pass


xys = ['x', 'y', 'x', 'x']
for x_or_y in xys:
    if x_or_y == 'x':
        fn1([], 'regexr 1')
    elif x_or_y == 'y':
        fn1([], 'regexr 2')
text = "ddd35=eee"
sec = text[text.index('35=')+3]