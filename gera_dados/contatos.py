from gera_senha import id_generator

vetor = []
indice = "@"

def log_and_pass():
    with open ('contatos.txt') as contatof:
        for dados in contatof:
            (nome, mail) = dados.strip().split('=')
            index_arroba = mail.find(indice)
            login = mail[0:index_arroba]
            senha = id_generator(9)

            vetor.append(login)
            vetor.append(senha)

    return (vetor)        

if __name__ == "__main__":
    algo = log_and_pass()
    print (algo)