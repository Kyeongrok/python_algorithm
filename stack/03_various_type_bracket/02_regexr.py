import re

s = '({([])})'
while '()' in s or '{}' in s or '[]' in s:
    sp = re.split('\(\)|\{\}|\[\]', s)
    s = ''.join(sp)
    print(s)

print(len(s) == 0)