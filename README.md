# RSVP com Destaque de Palavras e Diagramas Mermaid

Este projeto é uma aplicação web desenvolvida com **Streamlit** que implementa a técnica **RSVP (Rapid Serial Visual Presentation)** para leitura dinâmica de textos. Além disso, ele permite a renderização de diagramas **Mermaid** para auxiliar na pré-leitura e no entendimento do contexto.

## Funcionalidades

1. **Leitura RSVP**:
   - Exibe palavras de um texto uma por uma, em alta velocidade.
   - Destaque de palavras ou frases importantes usando parênteses `( )`.
   - As palavras destacadas são exibidas em **azul claro e sublinhadas**, com um tempo de exibição maior.

2. **Pré-Leitura com Diagramas Mermaid**:
   - Renderiza diagramas **Mermaid** para fornecer contexto antes da leitura dinâmica.
   - O diagrama é exibido no início da página, como parte do status de **pré-leitura**.

3. **Controle de Velocidade**:
   - Um slider permite ajustar a velocidade de exibição das palavras (em palavras por minuto).

4. **Exemplos de Prompts para IA**:
   - Inclui exemplos de prompts para gerar textos e diagramas Mermaid com IA.

## Como Usar

1. **Insira o Texto**:
   - No campo de texto, insira o conteúdo que deseja ler.
   - Use parênteses `( )` para destacar palavras ou frases importantes. Exemplo: `(Arquitetura Hexagonal)`.

2. **Ajuste a Velocidade**:
   - Use o slider para definir a velocidade de exibição das palavras.

3. **Renderize Diagramas Mermaid**:
   - Insira o código Mermaid no campo correspondente e clique em "Renderizar Diagrama".

4. **Inicie a Leitura RSVP**:
   - Clique em "Iniciar RSVP" para começar a leitura dinâmica.

## Exemplos de Prompts para IA

### Gerar Texto para RSVP

Crie um diagrama Mermaid que represente o fluxo da arquitetura hexagonal. Destaque as palavras chaves entre 
parentesis. O texto deve ter até 1000 palavras e não pode conter tópicos ou títulos, quanto mais exemplos de código. Gere um diagrama mermaid como `pré-leitura` do conteúdo que vc irá me gerar. 


## Requisitos

- Python 3.7 ou superior.
- Bibliotecas Python: `streamlit`, `re`, `time`.

## Instalação 

``` sh 
pip install streamlit
```
Execute o aplicativo:
``` sh
streamlit run app.py
```