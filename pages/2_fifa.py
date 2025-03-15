import streamlit as st  # Importa a biblioteca Streamlit para criar a interface web
import pandas as pd  # Importa o Pandas para manipulação de dados
from datetime import datetime

# Configura a página do Streamlit com um layout amplo e título
st.set_page_config(
    layout="wide",
    page_title="Fifa"
)

if "data" not in st.session_state:
    try:
        df_data = pd.read_csv("fifa/CLEAN_FIFA23_official_data.csv")
        df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
        df_data = df_data.sort_values(by="Overall", ascending=False)
        st.session_state["data"] = df_data
    except:
        df_data = []

st.markdown("# FIFA 2023 ")
st.markdown("""
O ranking de jogadores do FIFA 23 reflete as avaliações dos melhores atletas do jogo, levando em consideração atributos como velocidade, finalização, passe, drible, defesa e físico. A EA Sports analisa o desempenho dos jogadores na vida real para atribuir notas que definem suas habilidades dentro do game.

No topo do ranking, jogadores como Karim Benzema, Lionel Messi, Robert Lewandowski e Kevin De Bruyne aparecem com overalls acima de 90, consolidando-se como os mais bem avaliados. Kylian Mbappé, conhecido por sua explosão e finalização, também figura entre os melhores, destacando-se como um dos atacantes mais letais do jogo.

Além disso, craques como Mohamed Salah, Virgil van Dijk e Thibaut Courtois garantem posições de destaque, representando a elite do futebol mundial. Cristiano Ronaldo, apesar de uma leve queda em sua avaliação em relação a edições anteriores, continua sendo uma opção poderosa dentro do jogo.

No quesito jovens promessas, Erling Haaland, Vinícius Jr. e Pedri chamam atenção com ratings elevados e grande potencial de crescimento no modo Carreira. Esses atletas são frequentemente escolhidos pelos jogadores que buscam construir elencos para o futuro.

O FIFA 23 também trouxe atualizações que refletem a ascensão de novos talentos e a queda de veteranos que tiveram desempenhos abaixo do esperado. O equilíbrio nas avaliações permite que jogadores testem diferentes estratégias e montem equipes variadas nos modos Ultimate Team e Carreira.

Com gráficos aprimorados, jogabilidade refinada e a tecnologia HyperMotion2, FIFA 23 entrega uma experiência imersiva e realista, onde cada jogador no ranking desempenha um papel crucial para a vitória dentro de campo.
""")

st.sidebar.markdown("Desenvolvido no Curso Streamlit")


