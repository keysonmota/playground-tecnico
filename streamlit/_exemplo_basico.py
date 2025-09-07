import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# Configuração da página
st.set_page_config(
    page_title="Exemplo Básico Streamlit",
    page_icon="��",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título principal
st.title("🚀 Exemplo Básico - Streamlit")
st.markdown("---")

# Sidebar
st.sidebar.header("Configurações")

# Widgets de entrada
name = st.sidebar.text_input("Seu nome:", "Usuário")
age = st.sidebar.slider("Sua idade:", 0, 100, 25)
color = st.sidebar.selectbox("Cor favorita:", ["Azul", "Verde", "Vermelho", "Amarelo"])

# Conteúdo principal
col1, col2 = st.columns(2)

with col1:
    st.header("📊 Dados Pessoais")
    st.write(f"**Nome:** {name}")
    st.write(f"**Idade:** {age}")
    st.write(f"**Cor favorita:** {color}")

    # Botão
    if st.button("Clique aqui!"):
        st.balloons()
        st.success(f"Olá, {name}! 🎉")

with col2:
    st.header("�� Gráfico de Exemplo")

    # Gerar dados aleatórios
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['A', 'B', 'C']
    )

    st.line_chart(chart_data)

# Seção de métricas
st.header("📊 Métricas")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Temperatura", "21°C", "1.2°C")

with col2:
    st.metric("Umidade", "65%", "-2%")

with col3:
    st.metric("Pressão", "1013 hPa", "0 hPa")

with col4:
    st.metric("Vento", "12 km/h", "3 km/h")

# Seção de dados
st.header("�� Tabela de Dados")
df = pd.DataFrame({
    'Produto': ['Produto A', 'Produto B', 'Produto C', 'Produto D'],
    'Preço': [29.99, 39.99, 19.99, 49.99],
    'Estoque': [100, 50, 200, 75],
    'Categoria': ['Eletrônicos', 'Roupas', 'Casa', 'Eletrônicos']
})

st.dataframe(df, use_container_width=True)

# Gráfico de barras
st.header("📊 Vendas por Categoria")
category_sales = df.groupby('Categoria')['Preço'].sum()
st.bar_chart(category_sales)

# Footer
st.markdown("---")
st.markdown(f"*Última atualização: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}*")
