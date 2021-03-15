from datetime import date

def data_aniversario_valido(data_aniversario):
    """ Valida data de aniversário. 
    Se a data de aniversário for maior do que
    o dia de hoje o validador não permite
    a criacão do resgistro """

    hoje = date.today()

    if data_aniversario < hoje:
        return True
    else:
        return False

def nome_valido(nome):
    """ Valida nome do aniversariante.
    Se a string possuir números o validador
    não permite a ciração do registro. """
    return nome.isalpha()