import streamlit as st
import base64
import os

# ==========================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================

st.set_page_config(
    page_title="QUIZ de racismo estruturado",
    page_icon="🧠",
    layout="centered"
)

# ==========================================
# FUNÇÃO PARA CARREGAR IMAGEM EM BASE64
# ==========================================

def carregar_imagem_base64(caminho):
    if os.path.exists(caminho):
        with open(caminho, "rb") as arq:
            dados = arq.read()
            return f"data:image/png;base64,{base64.b64encode(dados).decode()}"
    return ""

img_base64 = carregar_imagem_base64("imagem_racismo.png")

# ==========================================
# ESTILO DO SITE
# ==========================================

estilo_css = r"""
<style>
    .stApp {
        background: linear-gradient(
            135deg,
            #f5f3ff 0%,
            #eef2ff 50%,
            #e0f2fe 100%
        );
    }

    .block-container {
        max-width: 820px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* CARD CENTRALIZADO DO CABEÇALHO */
    .header-card {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 22px;
        background-color: #ffffff;
        padding: 18px 40px;
        border-radius: 24px;
        box-shadow: 0 8px 24px rgba(76, 29, 149, 0.08);
        border: 2px solid #e0e7ff;
        width: fit-content;
        margin: 10px auto 15px auto;
    }

    /* LOGO MAIOR QUE O NOME DO QUIZ */
    .header-logo {
        height: 100px;
        width: auto;
        object-fit: contain;
    }

    /* NOME DO QUIZ EM TAMANHO GRANDE */
    .titulo-principal {
        font-size: 60px;
        font-weight: 800;
        color: #4c1d95 !important;
        margin: 0;
        line-height: 1;
    }

    .subtitulo {
        text-align: center;
        font-size: 30px;
        font-weight: 800;
        color: #4c1d95 !important;
        margin-top: 12px;
        margin-bottom: 35px;
    }

    .numero {
        color: #6d28d9 !important;
        font-size: 15px;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-top: 35px;
    }

    .pergunta {
        font-size: 28px;
        font-weight: 750;
        color: #172033 !important;
        margin-top: 10px;
        margin-bottom: 25px;
        line-height: 1.35;
    }

    div[data-testid="stRadio"] > label {
        color: #334155 !important;
        font-size: 16px !important;
        font-weight: 600 !important;
    }

    div[data-testid="stRadio"] div[role="radiogroup"] {
        gap: 12px;
    }

    div[data-testid="stRadio"] div[role="radiogroup"] label {
        background-color: #ffffff !important;
        border: 2px solid #dbe2ea !important;
        border-radius: 14px !important;
        padding: 14px 18px !important;
        transition: all 0.2s ease;
    }

    div[data-testid="stRadio"] div[role="radiogroup"] label p {
        color: #172033 !important;
        font-size: 16px !important;
        font-weight: 500 !important;
    }

    div[data-testid="stRadio"] div[role="radiogroup"] label span {
        color: #172033 !important;
    }

    div[data-testid="stRadio"] div[role="radiogroup"] label:hover {
        border-color: #8b5cf6 !important;
        background-color: #f5f3ff !important;
    }

    .stButton > button {
        width: 100%;
        border-radius: 14px !important;
        border: none !important;
        background: linear-gradient(
            135deg,
            #7c3aed,
            #4f46e5
        ) !important;
        color: white !important;
        font-size: 17px !important;
        font-weight: 700 !important;
        padding: 13px !important;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(79, 70, 229, 0.25);
    }

    div[data-testid="stProgressBar"] {
        margin-top: 0px;
        margin-bottom: 25px;
    }

    div[data-testid="stProgressBar"] > div {
        background-color: #ddd6fe !important;
        border-radius: 20px;
    }

    div[data-testid="stProgressBar"] > div > div {
        background: linear-gradient(
            90deg,
            #7c3aed,
            #4f46e5
        ) !important;
        border-radius: 20px;
    }

    .resultado {
        text-align: center;
        font-size: 38px;
        font-weight: 800;
        color: #4c1d95 !important;
        margin-top: 20px;
    }

    .pontuacao-final {
        text-align: center;
        font-size: 60px;
        font-weight: 800;
        color: #6d28d9 !important;
        margin-top: 30px;
    }

    /* CARTÃO E DESIGN DO RODAPÉ */
    .rodape-card {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(8px);
        border: 1px solid #e0e7ff;
        border-radius: 20px;
        padding: 20px 24px;
        text-align: center;
        box-shadow: 0 8px 20px rgba(76, 29, 149, 0.05);
        margin-top: 40px;
        margin-bottom: 20px;
    }

    .rodape-texto {
        color: #475569;
        font-size: 15px;
        font-weight: 600;
        margin-bottom: 12px;
    }

    .rodape-autores {
        display: inline-block;
        background: linear-gradient(135deg, #7c3aed, #4f46e5);
        color: #ffffff !important;
        padding: 8px 20px;
        border-radius: 50px;
        font-size: 14px;
        font-weight: 700;
        box-shadow: 0 4px 12px rgba(124, 58, 237, 0.2);
    }
</style>
"""

st.markdown(estilo_css, unsafe_allow_html=True)


# ==========================================
# PERGUNTAS (10 PERGUNTAS AO TODO)
# ==========================================

perguntas = [
    {
        "pergunta": "O que significa racismo estrutural?",
        "opcoes": [
            "Uma atitude racista praticada apenas por uma pessoa",
            "Um conjunto de desigualdades e práticas racistas presentes nas estruturas da sociedade",
            "Uma discussão que acontece somente nas redes sociais",
            "Uma forma de preconceito que não afeta instituições"
        ],
        "resposta": 1
    },
    {
        "pergunta": "Onde o racismo estrutural pode aparecer?",
        "opcoes": [
            "Somente nas escolas",
            "Somente no mercado de trabalho",
            "Em diferentes instituições e áreas da sociedade",
            "Somente na internet"
        ],
        "resposta": 2
    },
    {
        "pergunta": "Qual é uma possível consequência do racismo estrutural?",
        "opcoes": [
            "Desigualdade de oportunidades",
            "Aumento da igualdade social automaticamente",
            "Fim dos preconceitos",
            "Maior acesso igualitário a todas as oportunidades"
        ],
        "resposta": 0
    },
    {
        "pergunta": "Qual atitude pode ajudar no combate ao racismo?",
        "opcoes": [
            "Ignorar situações de discriminação",
            "Reproduzir estereótipos",
            "Buscar informação e combater atitudes discriminatórias",
            "Evitar falar sobre o assunto"
        ],
        "resposta": 2
    },
    {
        "pergunta": "Por que estudar o racismo estrutural é importante?",
        "opcoes": [
            "Para entender como desigualdades históricas podem continuar afetando a sociedade",
            "Para criar mais divisões entre as pessoas",
            "Para justificar preconceitos",
            "Para evitar discussões sobre desigualdade"
        ],
        "resposta": 0
    },
    {
        "pergunta": "O racismo estrutural está relacionado apenas às atitudes individuais?",
        "opcoes": [
            "Sim, sempre",
            "Não. Ele também pode estar relacionado ao funcionamento de instituições e estruturas sociais",
            "Sim, mas somente em escolas",
            "Não, porque o racismo não existe"
        ],
        "resposta": 1
    },
    {
        "pergunta": "O que são ações afirmativas na sociedade?",
        "opcoes": [
            "Medidas e políticas voltadas a reparar desigualdades históricas e promover a inclusão de grupos discriminados",
            "Regras que proíbem o acesso de certas pessoas às universidades",
            "Leis aplicadas apenas no ambiente escolar sem impacto social",
            "Punições aplicadas a crimes ocorridos exclusivamente na internet"
        ],
        "resposta": 0
    },
    {
        "pergunta": "Qual é a importância da representatividade nos espaços de poder e de destaque?",
        "opcoes": [
            "Apenas uma questão estética e sem efeito real na sociedade",
            "Permite a diversidade de visões de mundo e serve de inspiração para grupos historicamente marginalizados",
            "Garante o fim imediato de todas as formas de preconceito",
            "Acontece de forma espontânea sem necessidade de debate"
        ],
        "resposta": 1
    },
    {
        "pergunta": "De que forma o racismo estrutural pode impactar a economia e o mercado de trabalho?",
        "opcoes": [
            "Garantindo remuneração igual para todas as pessoas independentemente da etnia",
            "Através da disparidade salarial e menor presença de negros em cargos de liderança",
            "Eliminando qualquer tipo de discriminação nos processos seletivos",
            "Afetando apenas a área do entretenimento"
        ],
        "resposta": 1
    },
    {
        "pergunta": "O que significa o conceito de 'letramento racial'?",
        "opcoes": [
            "O processo de alfabetização básica de crianças na escola",
            "A tradução de termos jurídicos sobre Direitos Humanos",
            "O processo contínuo de reeducação para reconhecer, compreender e combater o racismo",
            "Um teste de leitura aplicado em processos seletivos"
        ],
        "resposta": 2
    }
]


# ==========================================
# CONFIGURAÇÃO DO ESTADO
# ==========================================

if "pergunta_atual" not in st.session_state:
    st.session_state.pergunta_atual = 0

if "pontuacao" not in st.session_state:
    st.session_state.pontuacao = 0

if "respondida" not in st.session_state:
    st.session_state.respondida = False

if "resposta_usuario" not in st.session_state:
    st.session_state.resposta_usuario = None


# ==========================================
# CABEÇALHO
# ==========================================

if img_base64:
    cabecalho_html = f"""
    <div class="header-card">
        <img src="{img_base64}" class="header-logo" alt="Logótipo">
        <div class="titulo-principal">🧠 Quiz</div>
    </div>
    """
else:
    cabecalho_html = """
    <div class="header-card">
        <div class="titulo-principal">🧠 Quiz</div>
    </div>
    """

st.markdown(cabecalho_html, unsafe_allow_html=True)

st.markdown(
    '<div class="subtitulo">Racismo Estrutural</div>',
    unsafe_allow_html=True
)


letras = ["A", "B", "C", "D"]


# ==========================================
# RESULTADO FINAL
# ==========================================

if st.session_state.pergunta_atual >= len(perguntas):

    pontuacao = st.session_state.pontuacao
    total = len(perguntas)

    st.markdown(
        '<div class="resultado">🏆 Resultado</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="pontuacao-final">{pontuacao} / {total}</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="rodape-card">
            <div class="rodape-autores">Feito por: Gustavo Gonçalves e Catharina Oliani</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================
# PERGUNTAS DO QUIZ
# ==========================================

else:

    numero = st.session_state.pergunta_atual
    pergunta = perguntas[numero]

    progresso = numero / len(perguntas)

    st.progress(progresso)

    st.markdown(
        f'<div class="numero">Pergunta {numero + 1} de {len(perguntas)}</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="pergunta">{pergunta["pergunta"]}</div>',
        unsafe_allow_html=True
    )

    opcoes_formatadas = [
        f"{letras[i]}) {opcao}"
        for i, opcao in enumerate(pergunta["opcoes"])
    ]

    resposta = st.radio(
        "Escolha uma alternativa:",
        opcoes_formatadas,
        key=f"resposta_{numero}"
    )

    st.write("")

    # ==========================================
    # RESPONDER
    # ==========================================

    if not st.session_state.respondida:

        if st.button(
            "✅ Responder",
            use_container_width=True
        ):

            indice = opcoes_formatadas.index(resposta)

            st.session_state.resposta_usuario = indice
            st.session_state.respondida = True

            if indice == pergunta["resposta"]:
                st.session_state.pontuacao += 1

            st.rerun()

    # ==========================================
    # RESULTADO DA RESPOSTA
    # ==========================================

    else:

        indice = st.session_state.resposta_usuario

        if indice == pergunta["resposta"]:

            st.success("🎉 Resposta correta!")

        else:

            st.error("❌ Resposta incorreta!")

            resposta_correta = pergunta["resposta"]

            st.info(
                f"💡 Resposta correta: "
                f"**{letras[resposta_correta]}) "
                f"{pergunta['opcoes'][resposta_correta]}**"
            )

        st.write("")

        st.write(
            f"🏆 Pontuação atual: "
            f"**{st.session_state.pontuacao} / {len(perguntas)}**"
        )

        st.write("")

        if st.button(
            "➡️ Próxima pergunta",
            use_container_width=True
        ):

            st.session_state.pergunta_atual += 1
            st.session_state.respondida = False
            st.session_state.resposta_usuario = None

            st.rerun()


# ==========================================
# RODAPÉ
# ==========================================

if st.session_state.pergunta_atual < len(perguntas):

    st.markdown(
        """
        <div class="rodape-card">
            <div class="rodape-texto">🧠 Aprender também é uma forma de transformar a sociedade.</div>
            <div class="rodape-autores">Feito por: Gustavo Gonçalves e Catharina Oliani</div>
        </div>
        """,
        unsafe_allow_html=True
    )