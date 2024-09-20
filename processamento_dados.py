# processamento_dados.py
def calcular_total_funcionarios(dados, ano):
    dados_sem_cabecalho = dados[1:]  
    
    total_funcionarios = {
        'race_asian': 0,
        'race_black': 0,
        'race_hispanic_latinx': 0,
        'race_native_american': 0,
        'race_white': 0
    }

    filtrados = [linha for linha in dados_sem_cabecalho if linha[1].isdigit() and int(linha[1]) == ano]

    for linha in filtrados:
        total_funcionarios['race_asian'] += int(linha[3]) if linha[3].isdigit() else 0
        total_funcionarios['race_black'] += int(linha[4]) if linha[4].isdigit() else 0
        total_funcionarios['race_hispanic_latinx'] += int(linha[5]) if linha[5].isdigit() else 0
        total_funcionarios['race_native_american'] += int(linha[6]) if linha[6] and linha[6].isdigit() else 0
        total_funcionarios['race_white'] += int(linha[7]) if linha[7].isdigit() else 0

    return total_funcionarios

def calcular_porcentagem_genero(dados, genero, ano):
    dados_sem_cabecalho = dados[1:]

    dados_filtrados = [linha for linha in dados_sem_cabecalho if linha[1].isdigit() and int(linha[1]) == ano]

    total = len(dados_sem_cabecalho)
    contador_genero = sum(1 for linha in dados_filtrados if linha[2] == genero)
    
    return (contador_genero / total) * 100 if total > 0 else 0


def calcular_media_racial_por_ano(dados, ano, raca_coluna):
    total_funcionarios = calcular_total_funcionarios(dados, ano)

    raca_nome = ['race_asian', 'race_black', 'race_hispanic_latinx', 'race_native_american', 'race_white'][raca_coluna - 3]

    total_raca = total_funcionarios[raca_nome]

    total_geral = sum(total_funcionarios.values())

    percentual = (total_raca / total_geral) * 100 if total_geral > 0 else 0

    return percentual
