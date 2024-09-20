import csv
def salvar_relatorio_csv(caminho_arquivo, dados):
    with open(caminho_arquivo, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(dados)