import streamlit as st
import time
import streamlit.components.v1 as components
import re


# Função para exibir as palavras no ritmo RSVP com destaque
def rsvp_display(text, words_per_minute):
    # Usamos regex para dividir o texto em palavras e blocos entre parênteses
    tokens = re.split(r"(\([^)]+\))", text)  # Captura blocos entre parênteses como tokens únicos
    base_delay = 60.0 / words_per_minute  # Calcula o atraso base entre as palavras em segundos
    highlight_delay_multiplier = 3.00  # 3x o tempo base para palavras destacadas
    placeholder = st.empty()

    for token in tokens:
        if token.strip() == "":
            continue  # Ignora tokens vazios
        # Verifica se o token está entre parênteses (ex: (destaque))
        if re.match(r"^\(.+\)$", token):
            # Remove os parênteses e aplica o estilo de destaque
            word_clean = token.strip("()")
            placeholder.markdown(
                f"<h1 style='text-align: center; color: #1E90FF; text-decoration: underline;'>{word_clean}</h1>",
                unsafe_allow_html=True
            )
            # Aumenta o tempo de exibição para palavras destacadas (3x o tempo base)
            time.sleep(base_delay * highlight_delay_multiplier)
        else:
            # Exibe as palavras normais
            words = token.split()
            for word in words:
                placeholder.markdown(f"<h1 style='text-align: center;'>{word}</h1>", unsafe_allow_html=True)
                time.sleep(base_delay)


# Função para renderizar diagramas Mermaid
def mermaid(code: str) -> None:
    components.html(
        f"""
        <pre class="mermaid">
            {code}
        </pre>

        <script type="module">
            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
            mermaid.initialize({{ startOnLoad: true }});
        </script>
        """
    )


# Configuração da página
st.title("RSVP - Rapid Serial Visual Presentation")

# Seção de Pré-Leitura
st.markdown("### Pré-Leitura: Diagrama de Contexto")
st.markdown(
    "Antes de iniciar a leitura dinâmica, explore o diagrama abaixo para entender o contexto geral do conteúdo. O diagrama faz parte do status de **pré-leitura** e ajuda a criar uma visão geral do tema.")

# Campo de texto para inserir o código Mermaid
mermaid_code = st.text_area("Insira o código Mermaid aqui:", height=150, value="graph LR\n    A --> B --> C")

# Botão para renderizar o diagrama Mermaid
if st.button("Renderizar Diagrama"):
    if mermaid_code:
        st.markdown("### Diagrama Renderizado")
        mermaid(mermaid_code)
    else:
        st.error("Por favor, insira um código Mermaid válido.")

# Descrição do sistema
st.markdown("### Como Funciona o Sistema")
st.markdown(
    "Este sistema utiliza a técnica **RSVP (Rapid Serial Visual Presentation)** para exibir palavras de um texto uma por uma, em alta velocidade, facilitando a leitura dinâmica.")

st.markdown("#### Instruções:")
st.markdown("1. **Texto para RSVP**:")
st.markdown("   - Insira o texto na caixa de texto abaixo.")
st.markdown(
    "   - Use parênteses `( )` para destacar palavras ou frases importantes. Exemplo: `(Arquitetura Hexagonal)`.")
st.markdown(
    "   - O sistema exibirá as palavras destacadas em **azul claro e sublinhadas**, com um tempo de exibição maior.")

st.markdown("2. **Velocidade de Leitura**:")
st.markdown("   - Use o slider para ajustar a velocidade de exibição das palavras (em palavras por minuto).")

st.markdown("#### Exemplos de Prompts para IA:")
st.markdown("- **Gerar Texto para RSVP**:")
st.markdown("  ```")
st.markdown(
    "  Crie um texto resumido sobre (Arquitetura Hexagonal), destacando os conceitos de (Portas e Adaptadores), (Separação de Preocupações) e (Testabilidade). Use parênteses para destacar palavras-chave.")
st.markdown("  ```")

st.markdown("- **Gerar Diagrama Mermaid**:")
st.markdown("  ```")
st.markdown(
    "  Crie um diagrama Mermaid que represente o fluxo da (Arquitetura Hexagonal), incluindo (Núcleo da Aplicação), (Portas), (Adaptadores) e (Sistemas Externos).")
st.markdown("  ```")

# Campo de texto para o usuário inserir o texto
user_input = st.text_area("Insira seu texto aqui:", height=150, help="Use (palavras) para destacar palavras ou frases.")

# Slider para controlar a velocidade de exibição das palavras
words_per_minute = st.slider("Velocidade (palavras por minuto)", min_value=50, max_value=1000, value=300)

# Botão para iniciar a exibição RSVP
if st.button("Iniciar RSVP"):
    if user_input:
        rsvp_display(user_input, words_per_minute)
    else:
        st.error("Por favor, insira um texto para continuar.")