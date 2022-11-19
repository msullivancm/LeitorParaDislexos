with open('resumo.txt','w') as arquivo:
    arquivo.write("teste de escrita\n")
    arquivo.write("teste de escrita\n")
    arquivo.write("teste de escrita\n")
    arquivo.write("teste de escrita\n")

arquivo = open('resumo.txt','r')
print(arquivo.readlines())
print(arquivo.readline())
