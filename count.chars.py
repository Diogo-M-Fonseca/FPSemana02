pl=str(input)

lista=pl.split(" ")

dic={}

for palavra in lista:
    dic[palavra]=len(palavra)

print (dic)