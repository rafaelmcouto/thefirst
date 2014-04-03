#!/usr/bin/python

import sys, os
import smtplib

# Este modulo gera o login a partir do prefixo do mail e a senha
from contatos import log_and_pass

from zabbix_api import ZabbixAPI
from argparse import ArgumentParser

debug_flag = False
progname = os.path.basename(sys.argv[0])

def error(msg) :
    sys.stderr.write('%s:%s\n' % (progname, msg))
    sys.exit(255)

def debug(msg) :
    if debug_flag :
        sys.stderr.write('%s:DEBUG:%s\n' % (progname, msg))

parser = ArgumentParser(description = 'Create Zabbix Screen with specified criteria')

parser.add_argument('--url', dest = 'url', default = 'http://zabbix.url.com/', help = 'Zabbix server address')
parser.add_argument('-u', '--user', dest = 'user', default = 'Admin do Zabbix', help = 'Zabbix user')
parser.add_argument('-p', '--password', dest = 'password', default = 'Senha do Admin', help = 'Zabbix password')
parser.add_argument('-n', '--name', dest = 'name', default = 'Nome', help = 'Zabbix alias')
parser.add_argument('-ln', '--last_name', dest = 'last_name', default = 'Sobrenome', help = 'Zabbix last name')
parser.add_argument('-t', '--team', dest = 'team', default = 'Equipe', help = 'Zabbix team')

args = parser.parse_args()

zapi = ZabbixAPI(server = args.url, path = "", log_level = 0)
zapi.login(args.user, args.password)

#voce precisa especificar o arquivo no path local
info = log_and_pass("arquivo.txt")

#print apenas para se certificar da execucao correta
print ("Informacoes processadas: ", info)

num = 0

while num < len(info):
    destinatario = 'seumail@gmail.com'
    para = info[num] + "nome_do_destinatario@seumail.com"
    mensagem = "Ola " + info[num + 2] + " " + info[num + 3] + ", estamos enviando a sua senha do Zabbix. Seu login e: " + info[num] + " e sua senha e: " + info[num + 1] + ". Acesse atraves da url - http://zabbix.url.com"

    usuario = 'seuemail@gmail.com'
    senha = 'sua_senha' 
 
    server = smtplib.SMTP('smtp.gmail.com:25')
    server.starttls() 
    server.login(usuario,senha) 
    server.sendmail(destinatario, para, mensagem)
    
    num += 4

print ("\nOs mails foram enviados.")    
server.quit()

num = 0

#Remove a posicao 0 da lista, pegando assim sempre a sequencia correta
#Neste caso, o 'usrgrpid' esta sendo usado como uma constante. Basta passar o id correto.
while num < len(info):
    zapi.user.create({
                "alias": info.pop(0),
                "passwd": info.pop(0),
                "name": info.pop(0),
                "surname": info.pop(0),
                "usrgrps": [{
                        "usrgrpid": "xx"
                        }],
                })
