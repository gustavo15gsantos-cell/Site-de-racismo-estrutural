import streamlit as st
import base64
import os

# ==========================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================
st.set_page_config(
    page_title="QUIZ - Racismo Estrutural",
    page_icon="🧠",
    layout="centered"
)

# ==========================================
# CARREGAR IMAGEM EM BASE64
# ==========================================
def carregar_imagem_base64(caminho):
    if os.path.exists(caminho):
        try:
            with open(caminho, "rb") as arq:
                dados = arq.read()
                return f"data:image/png;base64,{base64.b64encode(dados).decode()}"
        except Exception:
            return None
    return None

img_base64 = carregar_imagem_base64("imagem_racismo.png")

# ==========================================
# ESTILO CSS CORRIGIDO (ALTO CONTRASTE)
# ==========================================
st.markdown("""
<style>
    /* FUNDO DA PÁGINA */
    .stApp {
        background: linear-gradient(135deg, #f5f3ff 0%, #eef2ff 50%, #e0f2fe 100%);
    }

    .block-container {
        max-width: 800px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* CARD DO CABEÇALHO */
    .header-card {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 20px;
        background-color: #ffffff;
        padding: 16px 36px;
        border-radius: 24px;
        box-shadow: 0 8px 24px rgba(76, 29, 149, 0.08);
        border: 2px solid #e0e7ff;
        width: fit-content;
        margin: 0 auto 15px auto;
    }

    .header-logo {
        height: 95px;
        width: auto;
        object-fit: contain;
    }

    .titulo-principal {
        font-size: 60px;
        font-weight: 800;
        color: #4c1d95;
        margin: 0;
        line-height: 1;
    }

    .subtitulo {
        text-align: center;
        font-size: 28px;
        font-weight: 800;
        color: #4c1d95;
        margin-top: 10px;
        margin-bottom: 30px;
    }

    .numero-pergunta {
        color: #6d28d9;
        font-size: 15px;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-top: 20px;
        margin-bottom: 8px;
    }

    .pergunta-texto {
        font-size: 24px;
        font-weight: 750;
        color: #0f172a;
        margin-bottom: 20px;
    }

    /* CORREÇÃO DO TEXTO DO ST.RADIO PARA ALTO CONTRASTE */
    div[data-testid="stRadio"] label {
        color: #0f172a !important;
        font-size: 16px !important;
        font-weight: 600 !important;
    }

    div[data-testid="stRadio"] label p {
        color: #0f172a !important;
        font-size: 16px !important;
        font-weight: 600 !important;
    }

    div[data-testid="stRadio"] div[role="radiogroup"] > label {
        background-color: #ffffff !important;
        padding: 12px 18px !important;
        border-radius: 14px !important;
        border: 2px solid #cbd5e1 !important;
        margin-bottom: 10px !important;
        box-shadow: 0 2px 6px rgba(0,0,0,0.02);
        transition: all 0.2s ease;
    }

    div[data-testid="stRadio"] div[role="radiogroup"] > label:hover {
        border-color: #7c3aed !important;
        background-color: #f3e8ff !important;
    }

    /* ESTILO DOS BOTÕES */
    .stButton > button {
        background: linear-gradient(135deg, #7c3aed, #4f46e5) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 14px !important;
        font-size: 17px !important;
        font-weight: 700 !important;
        padding: 12px !important;
        box-shadow: 0 4px 14px rgba(124, 58, 237, 0.3) !important;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(124, 58, 237, 0.4) !important;
    }

    /* RODAPÉ */
    .rodape-card {
        background: rgba(255, 255, 255, 0.9);
        border: 1px solid #e0e7ff;
        border-radius: 20px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 6px 18px rgba(76, 29, 149, 0.06);
        margin-top: 40px;
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
        padding: 8px 22px;
        border-radius: 50px;
        font-size: 14px;
        font-weight: 700;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# PERGUNTAS DO QUIZ
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
        "pergunta": "Qual é a importância da representatividade nos espaços de poder e destaque?",
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
# ESTADO DA SESSÃO
# ==========================================
if "indice_pergunta" not in st.session_state:
    st.session_state.indice_pergunta = 0
if "pontuacao" not in st.session_state:
    st.session_state.pontuacao = 0
if "confirmado" not in st.session_state:
    st.session_state.confirmado = False

# ==========================================
# CABEÇALHO
# ==========================================
if img_base64:
    st.markdown(f"""
        <div class="header-card">
            <img src="{img_base64}" class="header-logo" alt="Logótipo">
            <div class="titulo-principal">Quiz</div>
        </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <div class="header-card">
            <div class="titulo-principal">🧠 Quiz</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="subtitulo">Racismo Estrutural</div>', unsafe_allow_html=True)

letras = ["A", "B", "C", "D"]
total_perguntas = len(perguntas)

# ==========================================
# ECRÃ FINAL / RESULTADO
# ==========================================
if st.session_state.indice_pergunta >= total_perguntas:
    st.balloons()
    st.markdown(f"""
        <div style="text-align: center; background: white; padding: 30px; border-radius: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
            <h1 style="color: #4c1d95; margin-bottom: 10px;">🏆 Resultado Final</h1>
            <h2 style="color: #6d28d9; font-size: 50px; margin: 15px 0;">{st.session_state.pontuacao} / {total_perguntas}</h2>
            <p style="font-size: 18px; color: #475569;">Obrigado por participar!</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    if st.button("🔄 Reiniciar Quiz", use_container_width=True):
        st.session_state.indice_pergunta = 0
        st.session_state.pontuacao = 0
        st.session_state.confirmado = False
        st.rerun()

# ==========================================
# EXIBIÇÃO DA PERGUNTA ATUAL
# ==========================================
else:
    idx = st.session_state.indice_pergunta
    q = perguntas[idx]

    st.progress(idx / total_perguntas)

    st.markdown(f'<div class="numero-pergunta">Pergunta {idx + 1} de {total_perguntas}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="pergunta-texto">{q["pergunta"]}</div>', unsafe_allow_html=True)

    opcoes = [f"{letras[i]}) {opt}" for i, opt in enumerate(q["opcoes"])]
    
    escolha = st.radio("Escolha uma opção abaixo:", opcoes, key=f"radio_{idx}")

    st.write("")

    if not st.session_state.confirmado:
        if st.button("✅ Confirmar Resposta", use_container_width=True):
            st.session_state.confirmado = True
            st.session_state.escolha_usuario = opcoes.index(escolha)
            if st.session_state.escolha_usuario == q["resposta"]:
                st.session_state.pontuacao += 1
            st.rerun()

    else:
        if st.session_state.escolha_usuario == q["resposta"]:
            st.success("🎉 Resposta Correta!")
        else:
            st.error("❌ Resposta Incorreta!")
            correta_idx = q["resposta"]
            st.info(f"💡 Resposta correta: **{letras[correta_idx]}) {q['opcoes'][correta_idx]}**")

        st.write(f"🏆 Pontuação atual: **{st.session_state.pontuacao} / {total_perguntas}**")
        st.write("")

        if st.button("➡️ Próxima Pergunta", use_container_width=True):
            st.session_state.indice_pergunta += 1
            st.session_state.confirmado = False
            st.rerun()

# ==========================================
# RODAPÉ
# ==========================================
st.markdown("""
    <div class="rodape-card">
        <div class="rodape-texto">🧠 Aprender também é uma forma de transformar a sociedade.</div>
        <div class="rodape-autores">Feito por: Gustavo Gonçalves e Catharina Oliani</div>
    </div>
""", unsafe_allow_html=True)