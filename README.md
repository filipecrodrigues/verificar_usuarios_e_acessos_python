# Comparar Grupos entre Usuários (Planilhas Excel)

Este projeto tem como objetivo comparar os **grupos** que dois usuários possuem em arquivos Excel diferentes e gerar um novo arquivo com os grupos que o **usuário X** tem a mais em relação ao **usuário Y**. Assim, o usuário Y pode receber os mesmos grupos para padronização de acessos.

---

##  Estrutura do Projeto

```
verificar-planilha/
├── docs/              # docuemntações do projeto 
├── venv/              # Ambiente virtual Python (opcional)
├── .gitignore         # Arquivos a serem ignorados pelo Git
├── main.py            # Script principal para comparar os grupos
├── README.md          # Documentação do projeto
├── requeriments.txt   # Lista de dependências do projeto

```

---

##  Requisitos

- Python 3.10 ou superior
- pip
- venv (ambiente virtual Python)

---

##  Instalação

1. **Clone o repositório**:

```bash
git clone https://github.com/seu-usuario/verificar-planilha.git
cd verificar-planilha
```

2. **Crie e ative o ambiente virtual** (opcional, mas recomendado):

```bash
python -m venv venv
source venv/Scripts/activate    # Windows
# ou
source venv/bin/activate        # macOS/Linux
```

3. **Instale as dependências**:

```bash
pip install -r requirements.txt
```

---

##  Como usar

1. Execute o script:

```bash
python main.py
```

2. Selecione o arquivo Excel do **usuário X**.

3. Selecione o arquivo Excel do **usuário Y**.

4. O sistema irá gerar um novo Excel com os grupos que o usuário X tem a mais, para que Y possa receber os mesmos.

---

## Formato esperado das planilhas

As planilhas de entrada devem conter as colunas com os seguintes nomes:

- `Login`: nome do usuário
- `Grupo`: nome do grupo de acesso

 O sistema é sensível ao nome exato das colunas!

---

##  Exemplo de saída

Será gerado um arquivo:

```
grupos_para_adicionar.xlsx
```

Este arquivo conterá os grupos que o usuário Y ainda não possui.

---

##  Tecnologias Utilizadas

- Python
- pandas
- openpyxl
- tkinter
- pyexcel

---

##  Autor

Desenvolvido por **Filipe C.**  
GitHub: https://github.com/filipecrodrigues/

---

##  Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
