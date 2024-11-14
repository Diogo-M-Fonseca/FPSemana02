pl = input()

lista = pl.split(" ")
ar={}
for x in lista:
    for y in x:
        if y not in ar:
            ar[x] = x.count(y)
            
            x.count(y)
