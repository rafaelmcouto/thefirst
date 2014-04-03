"""
    Este codigo trata a entrada de arquivo para a criacao de usuarios no zabbix.
    Ele recebe como parametro um arquivo de texto no seguinte formato
    Nome Sobrenome=nome.sobrenome@mail.com

    Ele separa na ordem necessaria e retorna uma lista para fazer o input dos dados usando a API do Zabbix.
"""
from gera_senha import id_generator

vetor = []
indice = "@"

def log_and_pass(filename):
    #recebe um arquivo como parametro. Dessa forma, pode-se fazer um arquivo por equipe.
    try:
        with open (filename) as contatof:
            for dados in contatof:
                #faz o split e separa o nome do mail
                (funcionario, mail) = dados.strip().split('=')
                #localiza a posicao do @ para pegar o prefixo do mail
                index_arroba = mail.find(indice)
                login = mail[0:index_arroba]
                #gera uma senha aleatoria
                senha = id_generator(9)
                #faz o split do nome  sobrenome para fazer o input no Zabbix
                (nome, sobrenome) = funcionario.strip().split()

                #cria um vetor com a ordem correta
                vetor.append(login)
                vetor.append(senha)
                vetor.append(nome)
                vetor.append(sobrenome)

        return (vetor)
        
    except FileNotFoundError as fnfe:
        print ("O arquivo nao foi encontrado " + str(fnfe))

if __name__ == "__main__":
   algo = log_and_pass("arquivo.txt")
