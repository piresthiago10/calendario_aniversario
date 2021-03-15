from datetime import date

def data_aniversario_valido(data_aniversario):

    hoje = date.today()

    if data_aniversario < hoje:
        return True
    else:
        return False

def nome_valido(nome):
    return nome.isalpha()