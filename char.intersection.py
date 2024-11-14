pl1=input()
pl2=input()

meio=set(pl1) and set(pl2)



resultado=""

for car in pl1:
    if car in meio and car not in resultado:
        resultado += car

print(resultado)