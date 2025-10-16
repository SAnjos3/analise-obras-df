# Análise Exploratória de Dados (EDA): Obras do Governo no DF

## Sumário
1.  [Visão Geral e Estrutura do DataFrame](#fase1)
2.  [Análise de Qualidade por Coluna](#fase2)
    * 2.1. [Análise de Validade (Validity)](#validade)
    * 2.2. [Análise de Unicidade (Uniqueness)](#unicidade)
    * 2.3. [Análise de Consistência (Consistency)](#consistencia)
    * 2.4. [Análise de Atualidade (Timeliness)](#atualidade)
3.  [Sumário da Qualidade dos Dados e Próximos Passos](#fase3)

---

<a id='fase1'></a>
## 1. Visão Geral e Estrutura do DataFrame

Nesta seção inicial, realizamos uma análise macroscópica para entender a escala, a estrutura geral e as características primárias do conjunto de dados como um todo.

### 1.1. Dimensões do DataFrame
* **Descrição:** Define a escala do problema, mostrando o número total de registros (linhas) e características (colunas) disponíveis para análise.
* **Resultados:**
    * *Cole aqui a saída do seu código `df.shape`*
* **Análise:**
    * *Escreva sua interpretação. Ex: O DataFrame é composto por X linhas e Y colunas...*

### 1.2. Dicionário de Dados Inicial e Tipagem Bruta
* **Descrição:** Apresenta a lista de todas as colunas e o tipo de dado (`Dtype`) que o Pandas atribuiu a cada uma durante a leitura inicial.
* **Resultados:**
    * *Cole aqui a saída do seu código `df.info()`*
* **Análise:**
    * *Escreva sua interpretação. Ex: A leitura inicial resultou em todas as colunas sendo classificadas como `object`. Isso indica que uma etapa de tratamento e conversão de tipos será necessária para habilitar análises numéricas e de data. Esta conversão será abordada na análise por coluna.*

### 1.3. Análise Geral de Completude (Valores Nulos)
* **Descrição:** Identifica a proporção de dados ausentes em todo o conjunto de dados, permitindo priorizar as colunas mais problemáticas.
* **Resultados:**
    * *Cole aqui o seu gráfico de barras de valores nulos e/ou a tabela de porcentagens.*
* **Análise:**
    * *Escreva sua interpretação, destacando as colunas com as maiores taxas de nulidade e o que isso pode significar. Ex: As colunas `dataFinalEfetiva` e `dataInicialEfetiva` apresentam uma taxa de ausência superior a 95%, sugerindo que a maioria das obras no dataset ainda não foi concluída ou que o preenchimento desses campos não é obrigatório...*

### 1.4. Análise Geral de Unicidade (Clones Perfeitos)
* **Descrição:** Realiza a primeira verificação de qualidade, quantificando o número de registros que são 100% idênticos a outros.
* **Resultados:**
    * *Cole aqui o resultado da sua análise de clones perfeitos (o número de linhas removidas).*
* **Análise:**
    * *Escreva sua interpretação. Ex: Foram identificados e removidos X registros que eram clones perfeitos. O DataFrame limpo, `df_limpa`, agora com Y linhas, será utilizado para as análises subsequentes.*

---

<a id='fase2'></a>
## 2. Análise de Qualidade por Coluna (Data Profiling)

Nesta fase, aprofundamos a investigação em cada coluna (ou grupos de colunas), avaliando a qualidade dos dados com base em um framework estruturado, como o da IBM ou DAMA-DMBOK.

<a id='validade'></a>
### 2.1. Análise de Validade (Validity)
* **Objetivo:** Verificar se os dados estão no formato correto e se conformam às regras de negócio esperadas.
* **Análise:**
    * **Colunas Numéricas (`valor_obra`, etc.):** *Após a conversão para o tipo numérico, foram analisadas as estatísticas descritivas. O valor mínimo de X e máximo de Y estão dentro do esperado. A diferença entre a média e a mediana sugere a presença de outliers, que serão investigados.*
    * **Colunas de Data (`dataCadastro`, etc.):** *Após a conversão para datetime, o intervalo de datas se mostrou plausível. A verificação de regras lógicas, como `dataFinalPrevista` > `dataInicialPrevista`, não retornou nenhuma inconsistência.*
    * **Colunas Categóricas (`situacao`, etc.):** *A análise dos valores únicos revelou que todas as categorias presentes são válidas de acordo com as regras de negócio conhecidas.*

<a id='unicidade'></a>
### 2.2. Análise de Unicidade (Uniqueness)
* **Objetivo:** Investigar a presença de redundâncias e duplicatas no nível da coluna.
* **Análise:**
    * **Coluna Identificadora (`idUnico`):** *Esta coluna apresentou a anomalia de qualidade mais significativa. Embora seja um identificador, foram encontrados X IDs distintos que se repetem. A análise de frequência revelou que as repetições ocorrem em grupos de 2, 3 e 4. A hipótese é que este comportamento representa um processo de negócio de atualização de registros, e não um erro de dados.*
    * **Colunas Descritivas (`nome`, etc.):** *A coluna `nome` apresentou Y ocorrências duplicadas. Uma verificação de plausibilidade demonstrou que estes casos se referem a projetos legitimamente distintos que compartilham nomes genéricos, não sendo considerados um problema de qualidade.*

<a id='consistencia'></a>
### 2.3. Análise de Consistência (Consistency)
* **Objetivo:** Verificar a padronização dos dados e a coerência lógica entre diferentes colunas.
* **Análise:**
    * **Padronização de Categorias:** *A coluna `situacao` apresentou valores não padronizados, como 'CONCLUÍDA' e 'Concluída'. Foi realizado um tratamento para unificar estas categorias.*
    * **Coerência Lógica entre Colunas:** *Foi verificado se os registros com `situacao` igual a 'CONCLUÍDA' possuíam a `dataFinalEfetiva` preenchida. Encontrou-se Z casos onde essa regra não era seguida, indicando uma inconsistência no processo de atualização dos dados.*

<a id='atualidade'></a>
### 2.4. Análise de Atualidade (Timeliness)
* **Objetivo:** Determinar a "idade" ou o "frescor" dos dados.
* **Análise:**
    * *A análise da coluna `dataCadastro` (ou outra coluna de data relevante) revelou que o registro mais recente no conjunto de dados é de **[insira a data máxima encontrada]**. Isso indica que a base de dados reflete o estado das obras até essa data.*

---

<a id='fase3'></a>
## 3. Sumário da Qualidade dos Dados e Próximos Passos

### 3.1. Matriz de Qualidade de Dados (Resumo)

| Dimensão         | Análise Realizada                                    | Status      | Observações Chave                                                                           |
| :--------------- | :--------------------------------------------------- | :---------- | :------------------------------------------------------------------------------------------ |
| **Completude**   | Análise de valores nulos por coluna.                 | **Alerta**  | Alta taxa de nulos em colunas de datas efetivas e dados de impacto.                         |
| **Unicidade**    | Investigação de clones e duplicatas no `idUnico`.    | **Crítico** | Identificadas duplicatas que indicam um processo de atualização, não erros.                 |
| **Validade**     | Verificação de tipos, formatos e regras de negócio.  | OK          | Após tratamento, os valores se mostraram dentro dos intervalos esperados.                   |
| **Consistência** | Padronização de categorias e coerência entre campos. | **Alerta**  | Encontradas categorias não padronizadas e inconsistências lógicas entre `situacao` e datas. |
| **Atualidade**   | Verificação da data do registro mais recente.        | OK          |