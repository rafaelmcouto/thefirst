#!/usr/bin/python

import sys, os

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

parser.add_argument('--url', dest = 'url', default = 'http://zabbix.dev.globoi.com/', help = 'Zabbix server address')
parser.add_argument('-u', '--user', dest = 'user', default = 'admin', help = 'Zabbix user')
parser.add_argument('-p', '--password', dest = 'password', default = '', help = 'Zabbix password')

args = parser.parse_args()

zapi = ZabbixAPI(server = args.url, path = "", log_level = 0)
zapi.login(args.user, args.password)

'''
OpBackup
'''