def notas(*n, sit=False):
    """
    ==> Função para analizar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param Sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dict = {}
    dict['total'] = len(n)
    dict['maior'] = max(n)
    dict['menor'] = min(n)
    dict['média'] = sum(n) / len(n)
    if sit == True:
        if dict['média'] < 5:
            dict['situação'] = 'RUIM'
        if 5 <= dict['média'] < 7:
            dict['situação'] = 'RAZOÁVEL'
        if dict['média'] >= 7:
            dict['situação'] = 'BOA'
    return dict


# Programa principal
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)
