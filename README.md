# Guia para Baixar e Executar um Projeto Streamlit

Este guia descreve o processo para baixar e executar um projeto Streamlit disponível no GitHub. Certifique-se de ter o Python 3.13.2 instalado.

## 1. Clonar o Repositório
Primeiro, abra o terminal e clone o repositório do GitHub:

```sh
git clone git@github.com:gitandol/curso_streamlit.git
```
## 2. Acessar o Diretório do Projeto

Navegue até o diretório do projeto clonado:

```sh
cd curso_streamlit
```

## 3. Criar e Ativar o Ambiente Virtual

Crie um ambiente virtual chamado `.env`:

```sh
python -m venv .env
```

Ative o ambiente virtual:

- **Windows:**
  ```sh
  .env\Scripts\activate
  ```
- **macOS/Linux:**
  ```sh
  source .env/bin/activate
  ```

## 4. Instalar Dependências

Com o ambiente virtual ativado, instale as dependências do projeto:

```sh
pip install -r requirements.txt
```

## 5. Executar o Streamlit

Agora, basta rodar o aplicativo com o seguinte comando:

```sh
streamlit run app.py
```

Substitua `app.py` pelo nome correto do arquivo principal do projeto, se necessário.

## 6. Acessar o Aplicativo

Após executar o comando acima, o Streamlit abrirá automaticamente no navegador padrão. Caso contrário, acesse manualmente o seguinte endereço:

```
http://localhost:8501
```

## 7. Desativar o Ambiente Virtual

Quando terminar, você pode desativar o ambiente virtual com:

```sh
deactivate
```

---

Agora você está pronto para explorar e utilizar o projeto! 🚀

