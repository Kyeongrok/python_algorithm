import re
from datetime import datetime

def while1(s):
    while '()' in s or '{}' in s or '[]' in s:
        sp = s.split('()')
        s = ''.join(sp)
        sp = s.split('{}')
        s = ''.join(sp)
        sp = s.split('[]')
        s = ''.join(sp)
    return len(s) == 0

def with_regex(s):
    while '()' in s or '{}' in s or '[]' in s:
        sp = re.split('\(\)|\{\}|\[\]', s)
        s = ''.join(sp)
    return len(s) == 0

s = f'{"("*(2*pow(10,4))}{"{"*(2*pow(10,4))}{"["*(2*pow(10,4))}{"]"*(2*pow(10,4))}{"}"*(2*pow(10,4))}{")"*(2*pow(10,4))}'
start_time = datetime.now()
# print(while1(s))
print(with_regex(s))
print(datetime.now() - start_time)

