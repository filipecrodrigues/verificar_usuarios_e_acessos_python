import pandas as pd
from tkinter import Tk, filedialog
import os

# Oculta a janela principal do Tkinter
Tk().withdraw()

# Seleciona o arquivo para o usuário X
print("Selecione o arquivo Excel para o usuário X...")
caminho_x = filedialog.askopenfilename(title="Selecione a planilha do usuário X")

# Seleciona o arquivo para o usuário Y
print("Selecione o arquivo Excel para o usuário Y...")
caminho_y = filedialog.askopenfilename(title="Selecione a planilha do usuário Y")

# Lê os arquivos Excel
df_x = pd.read_excel(caminho_x, engine='openpyxl')
df_y = pd.read_excel(caminho_y, engine='openpyxl')

# Padroniza os nomes das colunas para minúsculo
df_x.columns = df_x.columns.str.lower()
df_y.columns = df_y.columns.str.lower()

# Verifica se as colunas esperadas existem
for nome, df in zip(['X', 'Y'], [df_x, df_y]):
    if 'login' not in df.columns or 'grupo' not in df.columns:
        raise Exception(f"O arquivo do usuário {nome} deve conter as colunas 'Login' e 'Grupo'.")

# Extrai login e grupos
usuario_x = df_x['login'].iloc[0]
usuario_y = df_y['login'].iloc[0]

grupos_x = set(df_x['grupo'].dropna().astype(str).str.upper())
grupos_y = set(df_y['grupo'].dropna().astype(str).str.upper())

# Grupos que o usuário X tem a mais que o Y
grupos_para_adicionar = grupos_x - grupos_y

# Cria DataFrame com os grupos a adicionar
df_resultado = pd.DataFrame({
    'login': [usuario_y] * len(grupos_para_adicionar),
    'grupo_para_adicionar': list(grupos_para_adicionar)
})

# Salva resultado em Excel
nome_arquivo = f"grupos_para_{usuario_y.lower()}.xlsx"
df_resultado.to_excel(nome_arquivo, index=False)

print(f"\n✅ Arquivo gerado com sucesso: {nome_arquivo}")
