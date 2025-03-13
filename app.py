import streamlit as st  # Importa a biblioteca Streamlit para criar a interface web
import pandas as pd  # Importa o Pandas para manipulação de dados

# Configura a página do Streamlit com um layout amplo e título
st.set_page_config(
    layout="wide",
    page_title="spotify songs"
)

# Carrega o arquivo CSV contendo os dados das músicas do Spotify
df = pd.read_csv("01 Spotify.csv")

# Define a coluna "Track" como índice do DataFrame
df.set_index("Track", inplace=True)

# Obtém a lista de artistas únicos ordenados pela contagem de ocorrências
artists = df["Artist"].value_counts().index

# Cria um dropdown (selectbox) para selecionar um artista
artist = st.selectbox("Artista", artists)

# Filtra o DataFrame para exibir apenas as músicas do artista selecionado
df_filtered = df[df["Artist"] == artist]

# Obtém a lista de álbuns únicos do artista selecionado
albuns = df_filtered["Album"].value_counts().index

# Cria um dropdown para selecionar um álbum dentro do artista escolhido
album = st.selectbox("Album", albuns)

# Filtra novamente o DataFrame para exibir apenas as músicas do álbum selecionado
df_filtered = df[df["Album"] == album]

# Adiciona um checkbox para decidir se o gráfico será exibido
display = st.checkbox('Visualizar Dash')

# Se o checkbox estiver marcado, exibe um gráfico de barras com a quantidade de streams das músicas filtradas
if display:
    st.bar_chart(df_filtered["Stream"])
