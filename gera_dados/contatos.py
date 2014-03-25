from gera_senha import id_generator

nome = []
mail = []

with open ('contatos.txt') as contatof:
    for dados in contatof:
        (nome, mail) = dados.strip().split('=')
        senha = id_generator(9)

print ("Nome: ", nome)
print ("Mail: ", mail)
print ("Senha: ", senha)
