import string
import random
'''
Este modulo imprime uma senha aleatoria de 6 caracteres.
Caso tenha o interesse de variar a quantidade de caracteres, passe o parametro size=X, onde X eh a quantidade.
'''
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
