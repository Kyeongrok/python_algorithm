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

s = f'{"("*(2*pow(10,4))}{"{"*(2*pow(10,4))}{"["*(2*pow(10,4))}{"]"*(2*pow(10,4))}{"}"*(2*pow(10,4))}{")"*(2*pow(10,4))}'
start_time = datetime.now()
print(while1(s))
print(datetime.now() - start_time)