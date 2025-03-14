import streamlit as st  # Importa a biblioteca Streamlit para criar a interface web
import pandas as pd  # Importa o Pandas para manipulação de dados
import time  # Importa a biblioteca time para simular um atraso no carregamento dos dados

# Configura a página do Streamlit com um layout amplo e título
st.set_page_config(
    layout="wide",
    page_title="spotify songs"
)

# Função para carregar os dados do arquivo CSV
@st.cache_data  # Utiliza cache para armazenar os dados e evitar recarregamentos desnecessários
def load_data():
    time.sleep(5)  # Simula um atraso no carregamento dos dados
    return pd.read_csv("01 Spotify.csv")  # Carrega o arquivo CSV contendo as músicas do Spotify

# Carrega os dados e os armazena em um DataFrame
df = load_data()

# Armazena o conteúdo de df em uma variável da sessão para uso em outras páginas
st.session_state["df_spotify"] = df

# Define a coluna "Track" como índice do DataFrame
df.set_index("Track", inplace=True)

# Obtém a lista de artistas únicos ordenados pela contagem de ocorrências
artists = df["Artist"].value_counts().index

# Cria um dropdown (selectbox) para selecionar um artista dentro da barra lateral
artist = st.sidebar.selectbox("Artista", artists)

# Filtra o DataFrame para exibir apenas as músicas do artista selecionado
df_filtered = df[df["Artist"] == artist]

# Obtém a lista de álbuns únicos do artista selecionado
albuns = df_filtered["Album"].value_counts().index

# Cria um dropdown para selecionar um álbum dentro do artista escolhido
album = st.selectbox("Album", albuns)

# Filtra novamente o DataFrame para exibir apenas as músicas do álbum selecionado
df_filtered = df_filtered[df_filtered["Album"] == album]  # Corrigido para manter os filtros aplicados

# Adiciona um checkbox para decidir se o gráfico será exibido
display = st.checkbox('Visualizar Dash')

# Se o checkbox estiver marcado, exibe um gráfico de barras com a quantidade de streams das músicas filtradas
if display:
    st.bar_chart(df_filtered["Stream"])

# Divide a tela em duas colunas com proporção 70% e 30%
col1, col2 = st.columns([0.7, 0.3])  # Ou col1, col2 = st.columns(2) para tamanhos iguais

# Exibe um gráfico de barras com a quantidade de streams na primeira coluna
col1.bar_chart(df_filtered["Stream"])

# Exibe um gráfico de linha com a métrica "Danceability" na segunda coluna
col2.line_chart(df_filtered["Danceability"])
