import streamlit as st
import pandas as pd
import plotly.express as px

# configurando o layout
st.set_page_config(layout='wide')

df = pd.read_csv('/home/eduardo/Documentos/fatec/gestão_dados/dashboard/vendas.csv', sep=';', decimal=',')

# Formata a data para yyyy-mm-dd
df['Data'] = pd.to_datetime(df['Data'])

# Ordena do mais novo para o mais velho
df = df.sort_values('Data')

# Pega o mês
df['Mês'] = df['Data'].apply(lambda x: str(x.year) + '-' + str(x.month))

# Cria selectbox de meses na side bar
month = st.sidebar.selectbox('Mês', df['Mês'].unique())

# Com base no mês passado, filtra-os
df_filtered = df[df['Mês'] == month]

# Cria multiselect de gêneros
generos = st.sidebar.multiselect('Gênero', df['Gênero'].unique(), default=df['Gênero'].unique())

# Coloca imagem da fatec de pompeia
st.sidebar.image('fatec_pompeia.jpg', use_container_width=True)

# Se algum gênero for selecionado
if generos:
    # Retorna apenas as linhas que contem os gêneros passados pelo multiselect
    df_filtered = df_filtered[df_filtered['Gênero'].isin(generos)]

st.title('Dashboard Fatec Pompeia')
st.write('Business Intelligence')

st.markdown('## Resumo')

# Faz a soma de todo o faturamento do dataframe filtrado
total_faturamento = df_filtered['Total'].sum()

# Pega o total de vendas
total_vendas = df_filtered.shape[0]

# Pega a média (mean) das avaliações (rating)
avaliacao_media = df_filtered['Rating'].mean()

# Soma todas as quantidades de produto
total_produtos = df_filtered['Quantidade'].sum()

# Cria as colunas para exibição
col1, col2, col3, col4 = st.columns(4)

with col1:
    # Passa o dado junto de uma label
    st.metric(label='Total Faturamento', value=f'R${total_faturamento:.2f}')

with col2:
    st.metric(label='Total vendas', value=total_vendas)

with col3:
    st.metric(label='Avaliação média', value=f'{avaliacao_media:.2f}')

with col4:
    st.metric(label='Total de produtos', value=total_produtos)

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

fig_date = px.bar(df_filtered, x='Data', y='Total', color='Cidade', title='Faturamento por dia')
col1.plotly_chart(fig_date, use_container_width=True)

fig_prod = px.bar(df_filtered, x='Data', y='Linha de produto', 
                  color='Cidade', title='Faturamento por tipo de produto',
                  orientation='h')

col2.plotly_chart(fig_prod, use_container_width=True)

city_total = df_filtered.groupby('Cidade')[['Total']].sum().reset_index()

fig_city = px.bar(city_total, x='Cidade', y='Total', title='Faturamento por cidade')
col3.plotly_chart(fig_city, use_container_width=True)

fig_kind = px.pie(df_filtered, values='Total', names='Pagamento', title='Faturamento por tipo de pagamento')

col4.plotly_chart(fig_kind, use_container_width=True)

city_total = df_filtered.groupby('Cidade')[['Rating']].mean().reset_index()

fig_rating = px.bar(df_filtered, y='Rating', x='Cidade', title='Avaliação média')

col5.plotly_chart(fig_rating, use_container_width=True)

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler

st.markdown("## Recomendação de produto para um cliente ")

X = df[['Gênero', 'Cidade', 'Preço unitário']]
y = df[['Linha de produto']]

# criação de labels para variavel categoria (texto)
le_genero = LabelEncoder()
le_cidade = LabelEncoder()
le_produto = LabelEncoder()

# aplicando de fato a transformacao
X['Gênero'] = le_genero.fit_transform(X['Gênero'])
X['Cidade'] = le_cidade.fit_transform(X['Cidade'])
y_encoded = le_produto.fit_transform(y)

# escalonamento dos dados
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_encoded, test_size=0.15, random_state=0)

knn = KNeighborsClassifier(n_neighbors=3)

knn.fit(X_train, y_train)

st.markdown('### Insira os detalhes do cliente para receber uma recomendação de produto ')

genero_input = st.selectbox('Gênero', df["Gênero"].unique())
cidade_input = st.selectbox('Cidade', df['Cidade'].unique())
preco_input = st.number_input('Preço', min_value=0.0, step=0.1)

novo_cliente = pd.DataFrame([[le_genero.transform([genero_input])[0], le_cidade.transform([cidade_input])[0], preco_input]], columns=["Gênero", "Cidade", "Preço unitário"])

novo_cliente_scaled = scaler.transform(novo_cliente)

predicao = knn.predict(novo_cliente_scaled)

produto_recomendado = le_produto.inverse_transform(predicao)[0]

st.markdown('### Produto recomendado')
st.success(f' Este cliente provavelmente compraria {produto_recomendado}!')