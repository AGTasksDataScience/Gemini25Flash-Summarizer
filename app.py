import streamlit as st
import json
from google import genai
from google.genai.errors import APIError

# --- Configuração da API do Gemini (Usando st.secrets) ---
client = None
error_message = ""

# Tenta obter a chave via st.secrets
if "GEMINI_API_KEY" in st.secrets:
    try:
        # Inicializa o cliente usando a chave do secrets
        # Se a inicialização falhar (ex: chave inválida), o erro será capturado.
        client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
    except Exception as e:
        error_message = f"Erro ao inicializar o cliente Gemini: {e}"
else:
    error_message = "GEMINI_API_KEY não encontrada no arquivo .streamlit/secrets.toml. Por favor, configure a chave."


# --- Função para Otimizar o Texto (Prompt 2) ---
def get_optimized_text(text_to_optimize: str) -> str:
    """
    Chama o Gemini para otimizar um texto de entrada para fins de marketing/SEO.
    """
    if not client:
        # Retorna a mensagem de erro de configuração se o cliente não foi inicializado
        return f"Erro de Configuração. {error_message}"

    # O Prompt 2: Otimização
    optimization_prompt = f"""
    Sua função é atuar como um Analista de Conteúdo sênior.
    Reescreva o texto a seguir para torná-lo mais envolvente, profissional e otimizado para SEO.
    A reescrita deve:
    1. Manter o tom profissional.
    2. Tornar o título mais atraente.
    3. Incorporar sutilmente termos como "engenharia de dados" ou "inteligência artificial" (se relevantes).
    4. Garantir que a mensagem principal seja clara e focada em valor.

    TEXTO ORIGINAL:
    ---
    {text_to_optimize}
    ---

    FORME SUA RESPOSTA DA SEGUINTE MANEIRA:
    NOVO TÍTULO: [O Novo Título]
    [O Novo Texto Otimizado]
    """

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',  # Usando o modelo rápido
            contents=optimization_prompt
        )
        return response.text
    except APIError as e:
        return f"Erro na API durante a otimização: Verifique sua chave ou cota. Detalhes: {e}"
    except Exception as e:
        return f"Erro inesperado durante a otimização: {e}"


# --- Configuração da Página ---

st.set_page_config(
    page_title="Analista GenAI e MLOps (Portfólio)",
    layout="wide"
)

st.title("⚡ Analista GenAI Flash (Gemini 2.5) e MLOps")

st.markdown("""
Bem-vindo ao projeto de portfólio. Este aplicativo demonstra a velocidade do **Gemini 2.5 Flash** para análise e otimização de ativos digitais, com foco em princípios de **MLOps** e automação Python.
""")

# Placeholder para o input de texto
st.header("1. Entrada de Ativo Digital")
input_text = st.text_area(
    "Cole o texto que você deseja analisar e otimizar (ex: post de blog, descrição de produto):",
    height=200,
    placeholder="Exemplo: O novo produto da empresa é o melhor do mercado, ele tem recursos incríveis e vai revolucionar a indústria."
)

if st.button("Analisar com Gemini"):
    if not input_text:
        st.warning("Por favor, cole algum texto para iniciar a análise.")
    elif client is None:
        # Exibe o erro de configuração se o cliente não foi inicializado
        st.error(f"Falha na Conexão da API: {error_message}")
        st.warning("Corrija a chave em `.streamlit/secrets.toml` antes de prosseguir.")
    else:
        # --- Lógica do Pomodoro #3-4 (Otimização) ---
        st.info("Iniciando Análise e Otimização com Gemini 2.5 Flash...")

        # 1. Obter o texto otimizado
        with st.spinner("Chamando o Gemini 2.5 Flash para otimização de texto..."):
            optimized_text = get_optimized_text(input_text)

        # 2. Exibir os resultados (Layout temporário)
        st.subheader("2. Resultado da Otimização (Gemini 2.5 Flash)")

        # Cria as colunas para a visualização Lado a Lado
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Texto Original:**")
            st.code(input_text, language="text")

        with col2:
            st.markdown("**Texto Otimizado pelo Gemini:**")
            # Usamos st.markdown para renderizar a formatação do Gemini
            st.success(optimized_text)

        # Ponto de sucesso para o Pomodoro #3-4
        if "Erro" not in optimized_text:
            st.success(
                "Otimização concluída! Sua IA está entregando valor. Próximo passo: Análise Estruturada em JSON.")
        else:
            st.error("Falha na Otimização. Verifique se sua chave de API é válida e se há cota disponível.")