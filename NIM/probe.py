from itertools import cycle
a={1:"Коля",2:"Петя",3:"Саня"}


def gena(a):
    c = cycle(a.values())
    def generate(c):
        for i in c:
            yield i
    return generate(c)
o=gena(a)
print(next(o))
print(next(o))
print(next(o))
print(next(o))

