
import re

file= open ("slownik_pl.txt","r")


slowo = input('wprowadz slowo\n')
slowo  = format(slowo).replace('*', '.') 
regex = re.compile(slowo)

def haslo():
    l = set ()
    for a in file:
        haslo = regex.search(a)
        
        if( haslo != None):
            l.add(haslo.group())
    return l 

for b in haslo():
    print(b)
