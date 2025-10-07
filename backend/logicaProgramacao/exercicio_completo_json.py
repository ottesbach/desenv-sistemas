#crie um sistema de gerenciamento de petshop. 

#deverá ter os campos: nome, raça, idade, sexo, nome_dono, telefone_dono. 

#o nome do arquivo json deve ser "petshop.json" 

#faça um crud completo 


import json 
pets = [] 

try: 
    with open("petshop.json", "r",)as arquivo 
        pets = json.load(arquivo)

except FileNotFoundError: 
    print("arquivo não encontrado") 



try:
    id = int(input("digite o id do pet"))
    nome = input("digite o nome do pet")
    raça = (input("digite a raça do pet: "))
    idade = int(input("digite a idade do pet: "))
    sexo = (input("digite o sexo (m/f): "))
    nome_dono = (input("digite o nome do dono: "))
    telefone_dono = (input ("digite o telefone do dono: "))

    except ValueError: 
        print("digite os valores corretamente") 

    
novo_pet = {"id": id,
            "nome": nome,
            "raca": raca,
            "idade": idade,
            "sexo": sexo,
            "nome_dono": nome_dono
            "telefone_dono": telefone_dono
            }


pets.append(novo_pet)
with open("petshop.json", "w")as arquivo:
    json.dump(pets, arquivo, indent=4)
    print("pet cadastrado com sucesso!") 

    




































[                  
        {                                  

           "nome": "baruck" ,
           "raça": "pastor alemão",
           "idade": "5",
           "sexo": "M", 
           "nome_dono": "Márcio" 
           "telefone_dono": "44999999999"

        } ,
        { 

          "nome": "Mel"
          "raça": "vira lata",
          "idade"; "3", 
          "sexo": "F", 
          "nome_dono": "Lara", 
          "telefone_dono": "44888888888"

    }                                                         

] 