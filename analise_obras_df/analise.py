def verifica_coluna(coluna, df):
    """Retorna dois dicionarios com os valores de completude e unicidade da coluna passada como argumento."""

    #print(df[coluna].head(10).unique())
    completude_coluna = {}
    completude_coluna['Valores Nulos'] = df[coluna].isnull().sum()
    completude_coluna['Valores Não Nulos'] = df[coluna].notnull().sum()

    unicidade_coluna = {}
    unicidade_coluna['Valores Únicos'] = df[coluna].nunique()
    unicidade_coluna['Valores Duplicados'] = df[coluna].duplicated().sum()
    
    return completude_coluna, unicidade_coluna


def sugere_conversao(coluna):
    """Sugere a conversão de tipos de dados para a coluna passada como argumento. Utiliza a seguinte ordem de funilamento:
    float64
    int64
    datetime64[ns]
    bool
    category 
    string 
    A ideia é tentar converter para os tipos mais especificos primeiro, e caso não seja possivel, ir descendo o nivel para um tipo mais generico.
    """
    import pandas as pd
    import numpy as np

    if coluna.apply(lambda x: isinstance(x, (list, dict))).any():
        return 'Unhashable'
    
    coluna_limpa = coluna.dropna()
    if coluna_limpa.empty:
        return 'vazia'
    
    # Bloco de booleanos
    valores_unicos_lower = set(coluna_limpa.astype(str).str.lower().unique())
    representacoes_booleanas = {'true', 'false', '1', '0', 'sim', 'nao', 's', 'n', 'yes', 'no'}
    if valores_unicos_lower.issubset(representacoes_booleanas):
        return 'bool'

    # Bloco numerioco
    try:
        coluna_numerica = pd.to_numeric(coluna_limpa, errors='coerce')
        if not coluna_numerica.hasnans:
            if coluna_numerica.between(1900, pd.Timestamp.now().year + 5).all():
                return 'int64' 
            elif not coluna_numerica.isnull().all(): 
                if (coluna_numerica == np.floor(coluna_numerica)).all():
                    return 'int64'
                else:
                    return 'float64' 
    except (ValueError, TypeError):
        pass

    # Bloco datetime
    try:
        coluna_datetime = pd.to_datetime(coluna_limpa, errors='coerce')
        taxa_sucesso = coluna_datetime.notna().sum() / len(coluna_limpa)
        if taxa_sucesso > 0.8: 
            return 'datetime64[ns]'
    except (ValueError, TypeError):
        pass 


    # Bloco de categoricos
    num_unicos = coluna.nunique()
    proporcao_unicos = num_unicos / len(coluna_limpa)
    limiar_categoria=0.05
    if proporcao_unicos < limiar_categoria and num_unicos < len(coluna_limpa):
        return 'category'

    # Ralo String
    return 'string'

