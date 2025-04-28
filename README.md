# Análise Exploratória de Dados: Qualidade dos Vinhos

Este projeto tem como objetivo realizar uma análise exploratória detalhada de um conjunto de dados contendo informações físico-químicas e avaliações de qualidade de vinhos tintos e brancos.

## Objetivos da Análise

- Avaliar a distribuição das avaliações de qualidade (`quality`) por tipo de vinho (`red` ou `white`);
- Investigar diferenças estatísticas entre os tipos de vinho através do teste t de Student;
- Identificar e remover duplicatas no conjunto de dados;
- Analisar a correlação entre variáveis físico-químicas e a variável `quality` como preparação para modelagem preditiva.

## Principais Etapas Realizadas

- **Análise Descritiva:**
  - Inspeção das distribuições de qualidade para vinhos tintos e brancos.
  - Cálculo de médias e desvios padrão para cada tipo de vinho.
  
- **Teste de Hipóteses:**
  - Aplicação do teste t de Student para duas amostras independentes, considerando variâncias desiguais, a fim de comparar as médias das avaliações de qualidade.
  
- **Tratamento de Dados:**
  - Verificação e remoção de entradas duplicadas no dataset.
  
- **Análise de Correlação:**
  - Estudo preliminar da relação entre variáveis físico-químicas visando orientar futuras etapas de modelagem.

## Tecnologias Utilizadas

- **Linguagem:** Python
- **Bibliotecas:** 
  - Pandas
  - NumPy
  - Matplotlib
  - Seaborn
  - Statsmodels

## Próximos Passos

- Preparação dos dados para modelagem supervisionada (classificação).
- Desenvolvimento de modelos de machine learning para prever a qualidade do vinho baseada nas características físico-químicas.

---

> ⚡ Este README documenta apenas a fase de análises exploratória e estatística. Um README completo será disponibilizado na finalização do projeto.
