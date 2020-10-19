#Faz o impor da biblioteca pandas
import pandas as pd

import matplotlib as pid


#Traz a uma amostra aleatória dos dados do Enem
fonte = "https://github.com/alura-cursos/imersao-dados-2-2020/blob/master/MICRODADOS_ENEM_2019_SAMPLE_43278.csv?raw=true"

#Pede para o pandas ler o arquivo CSV fruto de parte dos dados do Enem
dados = pd.read_csv(fonte)

#Exibe a tabela
print(dados.head())

#Exibe os valores da coluna 'SG_UF_RESIDENCIA'
print(dados["SG_UF_RESIDENCIA"])

#Exibe todas as colunas presentes na tabela
print(dados.columns.values)

#Exibe os valores das colunas 'SG_UF_RESIDENCIA' e 'Q025'
print(dados[["SG_UF_RESIDENCIA","Q025"]])

#Exibe os membros da coluna 'SG_UF_RESIDENCIA'
print(dados["SG_UF_RESIDENCIA"].unique())

#Exibe a quantidade membros da coluna 'SG_UF_RESIDENCIA'
print(len(dados["SG_UF_RESIDENCIA"].unique()))

#Exibe a frequencia de cada membro da coluna 'SG_UF_RESIDENCIA'
dados["SG_UF_RESIDENCIA"].value_counts()

#Exibe a frequencia de cada membro da coluna 'NU_IDADE'
dados["NU_IDADE"].value_counts()

#Organiza de maneira crescente as idades e exibe a frequencia que essa idade se repete
dados["NU_IDADE"].value_counts().sort_index()

#Gera um histograma a partir da coluna 'NU_IDADE'
dados["NU_IDADE"].hist()