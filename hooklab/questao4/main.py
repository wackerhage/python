import pandas as pd
import matplotlib.pyplot as plt
from numpy.ma.core import MaskType

dados = pd.read_json("dados_compras.json")

# [780 rows x 6 columns]

# criacao da planilha do excel:

dados_linhas = []
linha = []

for i in range(len(dados)):
    linha = []
    linha.append(dados.loc[i, "Login"])
    linha.append(dados.loc[i, "Idade"])
    linha.append(dados.loc[i, "Sexo"])
    linha.append(dados.loc[i, "Item ID"])
    linha.append(dados.loc[i, "Nome do Item"])
    linha.append(dados.loc[i, "Valor"])

    # Adicionar a linha à lista de dados
    dados_linhas.append(linha)

excel_header = ["Login", "Idade", "Sexo", "Item ID", "Nome do Item", "Valor"]

arquivo_excel = pd.DataFrame(dados_linhas, columns=excel_header)

# verifica se ha valores nulos

linhas_zero = dados[dados["Item ID"] == 0]
print("\nLinhas com valores nulos: \n")
print(linhas_zero)

# Identifique a quantidade total de compras realizadas.

sum = 0
for i in range(len(dados)):
    sum += dados.loc[i, "Valor"]

print(f"\nA quantidade total de compras realizadas foi de R$ {round(sum, 2)}.")

# Calcule a média, o valor mínimo e máximo gasto por compra.

media = sum / len(dados)

print(f"\nA media de gasto foi de R$ {round(media, 2)}.")

print(f"\nO valor minimo foi de R$ {min(dados["Valor"])}.")

print(f"\nO valor maximo foi de R$ {max(dados["Valor"])}.")

# Determine o produto mais caro e o produto mais barato.

produto_mais_caro = dados.loc[dados['Valor'].idxmax()]

produto_mais_barato = dados.loc[dados['Valor'].idxmin()]

print(f"\nO produto mais caro: \n{produto_mais_caro}")

print(f"\nO produto mais barato: \n{produto_mais_barato}")

print("\nSegmentação por Gênero")

# Analise a distribuição de gênero entre os consumidores.
contagem_feminino = dados[dados["Sexo"] == "Feminino"].shape[0]
contagem_masculino = dados[dados["Sexo"] == "Masculino"].shape[0]
contagem_nao_informado = dados[~dados["Sexo"].isin(["Feminino", "Masculino"])].shape[0]

# Criar dados de gênero com contagens
dados_linhas = [
    ["Masculino", contagem_masculino],
    ["Feminino", contagem_feminino],
    ["Não informado", contagem_nao_informado]
]

print(f"\nTotal de pessoas do Sexo Masculino: {contagem_masculino}")

print(f"\nTotal de pessoas do Sexo Feminino: {contagem_feminino}")

print(f"\nTotal de pessoas com sexo nao informado: {contagem_nao_informado}")

excel_header = ["Sexo", "Contagem"]

arquivo_genero = pd.DataFrame(dados_linhas, columns=excel_header)

total_gasto_genero = dados.groupby("Sexo")["Valor"].sum().reset_index()

# Renomear as colunas para melhor compreensão
total_gasto_genero.columns = ["Sexo", "Total Gasto"]

print(f"\nValor total gasto em compras por gênero:\n\n {total_gasto_genero}")

with pd.ExcelWriter('arquivo_excel.xlsx', engine='xlsxwriter') as writer:
    arquivo_excel.to_excel(writer, sheet_name="Informacoes Clientes", index=False)
    arquivo_genero.to_excel(writer, sheet_name="Grafico Genero", index=False)
    total_gasto_genero.to_excel(writer, sheet_name="Total Gasto por Gênero", index=False)












