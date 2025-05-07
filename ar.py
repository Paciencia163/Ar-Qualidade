import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os
import plotly.express as px

# Configuração da página
st.set_page_config(page_title="🌍 Qualidade do Ar - Previsão Inteligente", layout="wide")

st.markdown("""
    <style>
        .main { background-color: #f4f6f9; }
        .stTabs [data-baseweb="tab"] {
            font-size: 16px; padding: 10px; color: #2c3e50;
        }
        .stTabs [data-baseweb="tab--selected"] {
            background-color: #3498db; color: white;
        }
        .title { font-size:28px !important; font-weight:700; color: #2c3e50; }
    </style>
""", unsafe_allow_html=True)

st.title("🌍 Qualidade do Ar - Previsão Inteligente")

# Abas
abas = st.tabs(["📊 Previsão", "🌫️ Poluentes", "🛡️ Dicas de Proteção", "📈 Resultados", "ℹ️ Sobre"])

# Armazena previsões para exportar e plotar
previsoes_dict = {}

# ============================
# ABA 1 - Previsão
# ============================
with abas[0]:
    st.subheader("📊 Insira os dados ambientais:")

    col1, col2, col3 = st.columns(3)

    with col1:
        temperature = st.number_input("🌡️ Temperatura (°C)", -50.0, 60.0, step=0.1)
        pm25 = st.number_input("🧪 PM2.5 (µg/m³)", 0.0, step=0.1)
        no2 = st.number_input("🧪 NO2 (ppb)", 0.0, step=0.1)

    with col2:
        humidity = st.number_input("💧 Humidade (%)", 0.0, 100.0, step=0.1)
        pm10 = st.number_input("🧪 PM10 (µg/m³)", 0.0, step=0.1)
        so2 = st.number_input("🧪 SO2 (ppb)", 0.0, step=0.1)

    with col3:
        co = st.number_input("🧪 CO (ppm)", 0.0, step=0.01)
        proximity = st.number_input("🏭 Proximidade de Indústrias (km)", 0.0, step=0.1)
        density = st.number_input("👥 Densidade Populacional (hab/km²)", 0.0, step=1.0)

    user_input = np.array([[temperature, humidity, pm25, pm10, no2, so2, co, proximity, density]])

    # Apenas dois modelos
    model_files = {
        "Logistic Regression": "logistic_regression.pkl",
        "XGBoost": "xgboost.pkl"
    }

    if st.button("🚀 Prever Qualidade do Ar"):
        st.info("A processar previsões...")

        for nome, arquivo in model_files.items():
            if os.path.exists(arquivo):
                try:
                    with open(arquivo, "rb") as f:
                        modelo = pickle.load(f)

                    if hasattr(modelo, "n_features_in_") and user_input.shape[1] != modelo.n_features_in_:
                        st.warning(f"⚠️ O modelo '{nome}' espera {modelo.n_features_in_} variáveis.")
                        continue

                    predicao = modelo.predict(user_input)[0]
                    previsoes_dict[nome] = predicao
                    st.success(f"✅ {nome} prevê: **{predicao}**")
                except Exception as e:
                    st.error(f"❌ Erro no modelo '{nome}': {str(e)}")
            else:
                st.error(f"❌ Arquivo '{arquivo}' não encontrado.")

# ============================
# ABA 2 - Poluentes
# ============================
with abas[1]:
    st.subheader("🌫️ Principais Poluentes do Ar")
    st.markdown("""
    - **PM2.5 / PM10**: Partículas finas. Podem causar problemas pulmonares e cardiovasculares.
    - **NO₂**: Irrita vias respiratórias, agrava asma.
    - **SO₂**: Causa inflamações respiratórias e chuva ácida.
    - **CO**: Gás incolor e tóxico que impede o transporte de oxigênio.
    """)

# ============================
# ABA 3 - Dicas de Proteção
# ============================
with abas[2]:
    st.subheader("🛡️ Como se Proteger da Poluição do Ar")
    st.markdown("""
    - 🏃 Evite atividades ao ar livre em dias poluídos
    - 😷 Use máscaras de boa filtragem
    - 🏠 Mantenha ambientes ventilados e limpos
    - 🌱 Plante mais árvores na sua comunidade
    - 📱 Monitore a qualidade do ar com aplicativos confiáveis
    """)

# ============================
# ABA 4 - Resultados
# ============================
with abas[3]:
    st.subheader("📈 Visualização e Exportação de Resultados")

    if previsoes_dict:
        df_resultados = pd.DataFrame(list(previsoes_dict.items()), columns=["Modelo", "Previsão"])
        st.table(df_resultados)

        fig = px.bar(df_resultados, x="Modelo", y="Previsão", color="Modelo",
                     title="Comparação das Previsões por Modelo",
                     text="Previsão", height=400)
        st.plotly_chart(fig)

        # Exportar
        csv = df_resultados.to_csv(index=False).encode('utf-8')
        st.download_button(label="⬇️ Baixar CSV das Previsões",
                           data=csv,
                           file_name='previsoes_modelos.csv',
                           mime='text/csv')
    else:
        st.info("⚠️ Nenhuma previsão disponível ainda. Execute a previsão na aba inicial.")

# ============================
# ABA 5 - Sobre
# ============================
with abas[4]:
    st.subheader("ℹ️ Sobre Esta Aplicação")
    st.markdown("""
    Esta aplicação utiliza algoritmos de machine learning para prever a qualidade do ar com base em diversos fatores ambientais.

    **Modelos Utilizados:**
    - Regressão Logística
    - XGBoost

    **Desenvolvedor:** Paciência Aníbal Muienga  
    **Tecnologias:** Python, Streamlit, Scikit-Learn, Plotly  
    """)
