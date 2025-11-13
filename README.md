⚡ **Analista GenAI Flash: Pipeline de Otimização e MLOps - MVP (realizado na máquina local e usando o modelo de versão gratuita)**

🎯 Visão Geral do Projeto

Este projeto é um protótipo de produção que demonstra como a **Inteligência Artificial Generativa (GenAI)** pode ser utilizada para otimização de ativos digitais (como posts de blog, descrições de produtos ou e-mails) com velocidade e monitoramento de produção (MLOps).

O objetivo é simular um pipeline real onde a IA é o "modelo" principal, e o **MLOps garante sua confiabilidade, performance e rastreabilidade**.

🛠️ Tecnologias Principais

|Categoria |Tecnologia |Justificativa
| :--- | :---: | ---: |
GenAI/LLM| Google Gemini 2.5 Flash| Escolhido por sua velocidade e baixa latência, crucial para aplicações em tempo real.**A API funcionou corretamente. Ponto de melhoria, testar outros modelos.** 
Frontend/Demo |Streamlit|Interface de usuário rápida para demonstrar o valor de negócio e o Dashboard MLOps.**E familiaridade com a ferramenta.**
Automação/MLOps|Python, Pandas, Logging (CSV)|Utilizado para orquestração, medição de latência, consumo de tokens e simulação de versionamento de prompt.

🧠 Foco em GenAI: Otimização e Análise Estruturada

O pipeline GenAI executa duas tarefas críticas em sequência, utilizando o gemini-2.5-flash:

Análise Estruturada (JSON): Força o modelo a retornar metadados do conteúdo (público-alvo, tom de voz, keywords) em formato JSON.

  * Obs.: O formato JSON contribui na Engenharia de Prompt para saída estruturada e facilidade de integração de dados em outros sistemas. **Este é um ponto que pode ser melhorado futuramente, conforme a necessidade do projeto**

**Otimização de Texto**: Este é um ponto crítico do projeto. Conforme a definição do prompt o modelo vai executar a otimização. Nesta etapa é onde se reescreve o texto de entrada. Neste MVP foi configurado para maior engajamento e aplicação de SEO/termos técnicos (simulando uma intervenção de um Analista Sênior). O texto utilizado foi o resumo da monografia:  COSTA, Gabriel Satiro Reis. Estudo sobre os determinantes da inflação brasileira (1980-2022). 2025. 86 f. Monografia (Graduação em Ciências Econômicas) - Instituto de Ciências Sociais Aplicadas, Universidade Federal de Ouro Preto, Mariana, 2025. 
**Em uma versão futura vou aperfeiçoar a estrutura MLops para que o prompt esteja fora do script principal como prática de POO (Programação Orientada a Objetos)**

📈 Foco em MLOps: Rastreabilidade e Performance

Este projeto aplica princípios de MLOps para monitorar o modelo GenAI:

1. Versionamento de Prompts (Lite)

O código utiliza uma função (load_prompt_version) para registrar a versão exata do prompt no log (v1.0-mvp), simulando a prática de versionamento de modelo para rastrear mudanças na performance. **Neste projeto utilizo o mesmo modelo, mas modifico o prompt de otimização, limitando o texto de saída com a quantidade de 150 caracteres.** 

2. Dashboard de Métricas em Tempo Real

Um Dashboard MLOps dedicado (na aba 📈 Dashboard MLOps do Streamlit) lê o arquivo de log (log_analises.csv) para exibir métricas históricas, como:

* Latência Média (KPI de Performance do Gemini 2.5 Flash). **Nesta etapa eu tenho tanto a latência (tempo de resposta) do texto de entrada, quanto a latência do texto de saída.**

* Tokens Consumidos (KPI de Custo da operação).**Esta informação é muito valiosa, uma vez que as empresas pagam por token e caracteres. Porque além do custo com o modelo, tem o custo de implementação - se local ou na nuvem.**

* Taxa de Falha de API (KPI de Disponibilidade/Confiabilidade).**Em pipelines de MLOps, falhas constantes indicam gargalos — podem ser por limite de tokens, instabilidade da rede, problemas de autenticação ou bugs de integração.A taxa de falha de 0.00 % indica que o modelo Gemini-2.5-Flash respondeu corretamente a todas as requisições de análise e otimização.**
*       Taxa de Falha de API (%)= (Nº total de requisições / Nº de requisições com erro​ ) × 100

3. Logging Automatizado

A função log_metrics_to_csv garante que cada execução, seja ela sucesso ou falha, registra o timestamp, a latência, o consumo de tokens e o status em um arquivo CSV, essencial para **auditoria e monitoramento contínuo.**


<font size="5">**Considerações Finais: O que este projeto me ensinou como pessoa?**</font> 
A técnologia está a nosso favor como ferramenta para melhoria contínua, mas ela não substitui a capacidade analítica do ser humano. 
Utilizei o Gemini como mentor para me guiar neste projeto, otimizar minha execução com scripts prontos e até mesmo me ajudar a quebrar o projeto em Pomodoros (técnica que utilizo que me auxilia a manter o foco em atividades). 
Apesar de toda a tecnologia utilizada, isso não me isentou de quebrar a cabeça identificando os bugs de configuração, lidando com as minhas dificuldades comportamentais e até mesmo sendo **manual** em alguns momentos para consultar documentações oficiais.  
Inclusive este texto REDME, que poderia ter sido apenas um "copia e cola", fez-me praticar a escrita em linguagem Markdown, tal como, faz-me sentir orgulho por ter acrescentado o meu toque pessoal e comentários úteis para eu usar nos projetos futuros.
