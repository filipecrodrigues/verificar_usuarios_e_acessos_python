# Comparador de Grupos de Usuários (Excel)

Este projeto Python compara os grupos de dois usuários a partir de arquivos Excel e gera um novo arquivo com os grupos que um usuário deve receber para igualar o outro.

## 🚀 Funcionalidades

- Seleção de arquivos Excel via janela gráfica
- Leitura de colunas `Login` e `Grupo`
- Comparação de grupos entre dois usuários
- Geração de novo Excel com grupos a adicionar

## ✅ Requisitos

- Python 3.10 ou superior
- VS Code (opcional)
- Bibliotecas:

```bash
pip install pandas openpyxl

## 📦 Execução
Execute o script:

python main.py

 - Você será solicitado a selecionar dois arquivos Excel: um para o usuário X e outro para o usuário Y.
 - O script irá gerar um arquivo como:

grupos_para_[login].xlsx

## 📁 Estrutura 
```

.
├── docs
|   |__ planilha_padrao_grupos.xlsx
├── main.py
├── venv/
├── README.md
└── .gitignore


```