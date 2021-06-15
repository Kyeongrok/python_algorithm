
class AutoMLCandate():
    def __init__(self):
        pass

def foo(*args):
    for a in args:
        print(a)

#
foo({'ddd', 'sss'},2,3, 5)

def foo2(a, b, c, d):
    print(a, b, c)

foo2(100,**{'b':10, 'c':'lee', 'd':'eeeewww'})


def make_coffee(*matreials):
    mixed = ''
    for item in matreials:
        mixed += item
    print(mixed)

make_coffee('water', 'espresso', 'ice')



def fn(**kwargs):
    print(kwargs)

fn(year=2, age=35)

def fn2(**kwargs):
    print(kwargs['year'], kwargs['age'])

fn2(year=2, age=35)

def plus_all(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum

print(plus_all(1, 2))
print(plus_all(1, 2, 3))
