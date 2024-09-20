# coleta_dados.py
import csv

def ler_dados_diversidade(arquivo_csv):
    with open(arquivo_csv, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        dados = [row for row in reader]
        return dados
