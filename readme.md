Atividades de Reposição de Aula Referente ao dia da Formatura 17/04/2024 Análise de Dados Agrícolas 

Exercício 1: Conhecendo Nosso Dataset de Vendas Agrícolas 

Para começar, precisamos nos familiarizar com os dados que temos em mãos. Este primeiro exercício vai ajudar vocês a entenderem a estrutura e as características básicas do nosso dataset: 

Dando uma primeira olhada nos dados: 

Visualizem as 5 primeiras linhas do dataset usando head(). 

Observem com atenção os tipos de informações disponíveis, como estão organizadas e quais são as variáveis principais. 

Explorando estatísticas descritivas: 

Utilizem a função describe() para obter um panorama estatístico completo das colunas numéricas. 

Analisem com atenção valores como médias, medianas, quartis, valores mínimos e máximos. 

Comentem o que essas métricas iniciais revelam sobre os dados. 

Aprofundando-se nas métricas de vendas: 

Calculem especificamente a média e o desvio padrão das colunas quantidade_vendida e preco_unitario. 

Reflitam: O que essas medidas nos mostram sobre o comportamento das vendas? A variabilidade é alta ou baixa? Quais conclusões preliminares podemos tirar? 

Exercício 2: Identificando e Analisando Valores Atípicos 

Os outliers (valores atípicos) podem influenciar significativamente nossas análises e conclusões. Neste exercício, vamos aprender a identificá-los e interpretá-los: 

Visualizando a distribuição e outliers: 

Construam boxplots para visualizar a distribuição das variáveis quantidade_vendida e preco_unitario. 

Lembrem-se que no boxplot, os pontos que aparecem isolados além dos "bigodes" representam possíveis outliers. 

Análise crítica dos valores atípicos: 

Caso identifiquem outliers, elaborem uma análise detalhada sobre:  

Quais critérios visuais permitiram identificá-los no gráfico? 

Qual a possível origem desses valores atípicos? (Considerem hipóteses como: erros na coleta de dados, eventos sazonais extraordinários, grandes pedidos corporativos, promoções especiais, etc.) 

Como esses outliers podem impactar as conclusões da nossa análise? 

Em um cenário real, quais decisões tomaríamos em relação a esses valores? 

Exercício 3: Análise Comparativa por Segmentos 

Agora vamos segmentar nossos dados para descobrir padrões específicos por região e categoria de produtos: 

Análise regional das vendas: 

Agrupem os dados por região e calculem a média da quantidade vendida para cada uma. 

Identifiquem qual região apresenta o maior volume médio de vendas. 

Reflitam sobre possíveis fatores que explicam essas diferenças regionais (população, economia local, cultura agrícola da região). 

Perfil de preço por categoria de produto: 

Calculem o preço unitário médio para cada categoria de produto. 

Identifiquem se há categorias com preços significativamente maiores ou menores. 

Discutam brevemente se essas diferenças fazem sentido considerando o mercado agrícola (custos de produção, demanda, perecibilidade, etc.). 

Representação visual das comparações: 

Elaborem gráficos de barras para visualizar:  

A média de quantidade vendida por região. 

A média de preço unitário por categoria. 

Apresentação visual: incluam títulos descritivos, legendas claras e nomeiem adequadamente os eixos. 

Destaquem no gráfico (usando cores ou anotações) os resultados mais expressivos ou surpreendentes. 

Escrevam uma breve interpretação para cada gráfico, explicando os padrões observados. 

 