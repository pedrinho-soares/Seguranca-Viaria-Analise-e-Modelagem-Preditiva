# %%
import pandas as pd 

# %%
import pandas as pd
import os

file_path = (r'C:\Users\Pedro Soares\Desktop\portfolio\aguiabranca\data\data\acidentes_mg.csv')

if os.path.exists(file_path):
    try:
        df = pd.read_csv(file_path, sep=';', encoding='latin-1')
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, sep=';', encoding='cp1252')
    
    print(df.head(2))


# %%
df.columns

# %% [markdown]
# ### Irei remover a coluna "Bicicletas" pra não dar ruído no modelo visto que foi um baixo número.

# %%
df.drop(columns=['bicicleta'], inplace=True)

# %% [markdown]
# #### Criando uma Modelagem Dimensional para tabelas e consultas precisas.

# %%
fato_acidentes = df[['n_da_ocorrencia','data','trecho','km', 'tipo_de_ocorrencia',
                     'tipo_de_acidente', 'automovel', 'moto', 'caminhao', 'onibus','outros'
                     ,'mortos']].copy()

# %%
### Criando dimensão tempo  ###

df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
dim_tempo = pd.DataFrame({'data': df['data'],
                          'ano': df['data'].dt.year,
                          'mes': df['data'].dt.month,
                          'dia': df['data'].dt.day,
                          'dia_da_semana': df['data'].dt.day_name()})

# %%
### criando dimensão veiculos ###

dim_veiculo = pd.DataFrame({'id_veiculo':[1,2,3], 
                            'tipo_veiculo':['Automóvel','Bicicleta','Moto']})




# %%
dim_classificacao = df[['tipo_de_ocorrencia','tipo_de_acidente']].drop_duplicates().reset_index(drop=True)

# %%
dim_tempo.head()

# %%
# CRIANDO FILTRO PARA DIA ESPECÍFICO
df_dia_especifico = dim_tempo[(dim_tempo['dia'].between (22, 30)) & 
                               (dim_tempo['mes'] == 9) & 
                               (dim_tempo['ano'] == 2022)]

# Contar quantos acidentes houve nesse dia
total_acidentes = len(df_dia_especifico)
print(f"Total de acidentes em 22/09/2022: {total_acidentes}")