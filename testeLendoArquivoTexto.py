#Criando e mostrando arquivo texto
with open('resumo.txt','w') as arquivo:
    arquivo.write("teste de escrita\n")
    arquivo.write("teste de escrita\n")
    arquivo.write("teste de escrita\n")
    arquivo.write("teste de escrita\n")

arquivo = open('resumo.txt','r')
lista = []
lista = arquivo.readlines()
for l in lista:
    print(l)
    

