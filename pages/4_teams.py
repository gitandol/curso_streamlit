import streamlit as st  # Importa a biblioteca Streamlit para criar a interface web

# Configura a página do Streamlit com um layout amplo e define o título da página
st.set_page_config(
    layout="wide",
    page_title="Teams"
)

# Adiciona um título principal à página
st.markdown("# TEAM ")

# Cria um botão para voltar à página HOME
if st.button("Voltar para HOME"):
    st.switch_page("pages/2_fifa.py")  # Redireciona para a página "2_fifa.py" dentro da pasta "pages/"

# Define um valor padrão para os dados, caso a sessão não contenha informações
df_data = 'Sem informações'

# Verifica se existem dados armazenados na sessão do Streamlit
if "data" in st.session_state:
    df_data = st.session_state["data"]  # Obtém os dados armazenados na sessão

    # Obtém a lista de clubes únicos ordenados pela contagem de jogadores
    clubes = df_data["Club"].value_counts().index

    # Cria um dropdown na barra lateral para selecionar um clube
    club = st.sidebar.selectbox("Clube", clubes)

    # Filtra o DataFrame para obter apenas os jogadores do clube selecionado
    df_filtred = df_data[df_data["Club"] == club].set_index("Name")  # Define "Name" como índice

    # Exibe a logo do clube selecionado
    club_logo = df_filtred.iloc[0].get("Club Logo", None)
    if club_logo:
        st.image(club_logo)

    # Exibe o nome do clube como um subtítulo
    st.markdown(f"## {club}")

    # Define as colunas que serão exibidas na tabela
    columns = [
        "Age", "Photo", "Flag", "Overall", "Value(£)", "Wage(£)", "Joined", "Height(cm.)",
        "Weight(lbs.)", "Contract Valid Until", "Release Clause(£)"
    ]

    # Exibe uma tabela interativa com os jogadores do clube
    st.dataframe(
        df_filtred[columns],  # Exibe apenas as colunas selecionadas
        column_config={
            # Configura a coluna "Overall" para ser exibida como barra de progresso
            "Overall": st.column_config.ProgressColumn(
                "Overall", format="%d", min_value=0, max_value=100
            ),
            # Configura a coluna "Wage(£)" como barra de progresso com valores monetários
            "Wage(£)": st.column_config.ProgressColumn(
                "Week Wage", format="£%f", min_value=0, max_value=df_filtred["Wage(£)"].max()
            ),
            # Configura as colunas "Photo" e "Flag" para exibir imagens
            "Photo": st.column_config.ImageColumn(),
            "Flag": st.column_config.ImageColumn("Country"),
        }
    )
