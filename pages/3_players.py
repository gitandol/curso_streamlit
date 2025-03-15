import streamlit as st  # Importa a biblioteca Streamlit para criar a interface web

# Configura a página do Streamlit com um layout amplo e define o título da página
st.set_page_config(
    layout="wide",
    page_title="Players"
)

# Adiciona um título principal à página
st.markdown("# PLAYER ")

# Cria um botão para voltar à página HOME
if st.button("Voltar para HOME"):
    st.switch_page("pages/2_fifa.py")

# Define uma variável padrão caso não haja dados disponíveis na sessão
df_data = 'Sem informações'

# Verifica se existem dados armazenados na sessão do Streamlit
if "data" in st.session_state:
    df_data = st.session_state["data"]  # Obtém os dados da sessão

    # Obtém a lista de clubes únicos ordenados pela contagem de jogadores
    clubes = df_data["Club"].value_counts().index

    # Cria um dropdown na barra lateral para selecionar um clube
    club = st.sidebar.selectbox("Clube", clubes)

    # Filtra os jogadores do clube selecionado
    df_players = df_data[df_data["Club"] == club]

    # Obtém a lista de jogadores únicos do clube selecionado
    players = df_players["Name"].value_counts().index

    # Cria um dropdown na barra lateral para selecionar um jogador
    player = st.sidebar.selectbox("Jogador", players)

    # Obtém os dados do jogador selecionado
    player_stats = df_data[df_data["Name"] == player].iloc[0]

    # Exibe a imagem do jogador
    st.image(player_stats["Photo"])

    # Exibe o nome do jogador como título
    st.title(player_stats["Name"])

    # Exibe o clube e a posição do jogador
    st.markdown(f"**Clube:** {player_stats['Club']}")
    st.markdown(f"**Posição:** {player_stats['Position']}")

    # Divide a tela em quatro colunas para exibir estatísticas básicas do jogador
    col1, col2, col3, col4 = st.columns(4)
    col1.markdown(f"**Idade:** {player_stats['Age']} anos")
    col2.markdown(f"**Altura:** {player_stats['Height(cm.)'] / 100}m")  # Convertendo cm para metros
    col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)'] * 0.453:.2f}kg")  # Convertendo libras para kg

    # Adiciona um divisor visual para separar as seções
    st.divider()

    # Exibe a pontuação geral do jogador
    st.subheader(f"Overall {player_stats['Overall']}")

    # Exibe a pontuação como uma barra de progresso
    st.progress(int(player_stats['Overall']))

    # Divide a tela em quatro colunas para exibir os valores financeiros do jogador
    col1, col2, col3, col4 = st.columns(4)
    col1.metric(label="Valor de mercado", value=f"£ {player_stats['Value(£)']:,}")  # Exibe valor de mercado formatado
    col2.metric(label="Remuneração Semanal", value=f"£ {player_stats['Wage(£)']:,}")  # Exibe salário semanal
    col3.metric(label="Cláusula de rescisão", value=f"£ {player_stats['Release Clause(£)']:,}")  # Exibe cláusula de rescisão
