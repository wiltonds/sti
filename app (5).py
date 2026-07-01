import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Dashboard Estratégico SST', layout='wide')

try:
    df = pd.read_csv('base_tratada_sst.csv')
    df_sub = pd.read_csv('analise_assinatura_sst.csv')

    st.title('📊 Dashboard Estratégico SST')
    
    col1, col2, col3 = st.columns(3)
    col1.metric('Ticket Médio (25-26)', 'R$ 3.894,39')
    col2.metric('Foco ICP', 'Micro/Pequena')
    col3.metric('Líder', 'Contrato SST')

    st.header('Simulação de Assinatura')
    st.dataframe(df_sub[['Razao Social', 'Total_Pago', 'Mensalidade_Estimada_Base']].head(10))
    
    fig = px.pie(df, names='Porte', title='Distribuição por Porte')
    st.plotly_chart(fig)

except Exception as e:
    st.error(f'Erro: {e}. Certifique-se de que os arquivos CSV estão no GitHub.')