import streamlit as st

# ==========================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================

st.set_page_config(
    page_title="QUIZ de racismo estruturado",
    page_icon="🧠",
    layout="centered"
)

# ==========================================
# ESTILO DO SITE
# ==========================================

st.markdown("""
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

    .titulo {
        text-align: left;
        font-size: 48px;
        font-weight: 800;
        color: #4c1d95 !important;
        margin: 0;
    }

    .subtitulo {
        text-align: center;
        font-size: 30px;
        font-weight: 800;
        color: #4c1d95 !important;
        margin-top: 30px;
        margin-bottom: 40px;
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

    .autores-final {
        text-align: center;
        color: #4c1d95 !important;
        font-size: 17px;
        font-weight: 700;
        margin-top: 30px;
    }

    .rodape {
        text-align: center;
        color: #64748b !important;
        font-size: 14px;
        margin-top: 35px;
        margin-bottom: 20px;
    }

    .autores {
        color: #4c1d95 !important;
        font-size: 15px;
        font-weight: 700;
    }
</style>
""", unsafe_allow_html=True)


# ==========================================
# PERGUNTAS
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

# Imagem no canto superior esquerdo e título Quiz ao lado
col1, col2 = st.columns([1, 5])

with col1:
    st.image(
        "imagem_racismo.png",
        width=100
    )

with col2:
    st.markdown(
        '<div class="titulo" style="margin-top: 18px;">🧠 Quiz</div>',
        unsafe_allow_html=True
    )

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
        '<div class="autores-final">'
        'Feito por: Gustavo Gonçalves e Catharina Oliani'
        '</div>',
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
        <div class="rodape">
            🧠 Aprender também é uma forma de transformar a sociedade.
            <br><br>

            <span class="autores">
                Feito por: Gustavo Gonçalves e Catharina Oliani
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )