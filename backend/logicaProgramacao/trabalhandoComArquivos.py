with open ("compras.txt" , "w")
#w --- abrir o arquivo no modo escrita - apaga 
#a --- " " " adição - adicionar 
#r --- " " " leitura 

with open("tarefas.txt", "w") as arquivo:
    arquivo.write("lavar a louça") 
    arquivo.write("arrumar a cama")

    #ler o arquivo 
    with open ("compras.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print(conteudo) 

#ler o arquivo linha por linha 
with open ("compras.txt" "r") as arquivo:
    for tarefa in compras 
        print("produto:"produto.strip())

#acrecentar dados ao final 
with open("compras.txt", "a") as arquivo:
    arquivo.write("arroz")


#crie um arquivo de nome aluno.txt
#adicione 5 alunos no arquivo 
#confira abrindo o arquivo se escreveu 
#leia o arquivo e faça o print de cada aluno no terminal 

with open("aluno.txt", "w") as dados:
    dados.write("Laura\n")
    dados.write("Giovana\n")
    dados.write("Peterson\n")
    dados.write("Carol\n")
    dados.write("Guilherme\n")
    
with open ("aluno.txt", "r") as dados:
    for alunos in dados:
        print("Aluno:", alunos.strip()) 

