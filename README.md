# 🌍 Aplicação de Previsão da Qualidade do Ar

Este projeto é uma aplicação interativa desenvolvida com **Streamlit** que utiliza modelos de **Machine Learning** para prever a **Qualidade do Ar** com base em fatores ambientais como temperatura, humidade, poluentes (PM2.5, NO₂, CO, etc.), proximidade de zonas industriais e densidade populacional.

## 📌 Funcionalidades

- Interface web simples, moderna e responsiva
- Previsão da Qualidade do Ar com:
  - ✅ Regressão Logística
  - ✅ XGBoost
- Abas com:
  - Previsão com entrada personalizada de dados
  - Explicação sobre poluentes atmosféricos
  - Dicas de proteção contra a poluição do ar
  - Resultados comparativos e exportação para CSV
  - Informações sobre o projeto

## 💻 Tecnologias Utilizadas

- Python 3.x
- Streamlit
- Scikit-learn
- XGBoost
- Plotly
- Pandas
- NumPy

## 🧠 Modelos de Machine Learning

Modelos treinados e serializados:
- logistic_regression.pkl
- xgboost.pkl

## 🏁 Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/nome-do-repo.git
cd nome-do-repo
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute o app:

```bash
streamlit run app.py
```

## 📊 Estrutura Esperada dos Dados

```
Temperature, Humidity, PM2.5, PM10, NO2, SO2, CO, Proximity_to_Industrial_Areas, Population_Density
```

Exemplo de entrada:

```
29.8,59.1,5.2,17.9,18.9,9.2,1.72,6.3,319
```

## 📁 Estrutura do Projeto

```
├── app.py                     # Aplicação Streamlit
├── logistic_regression.pkl    # Modelo Logistic Regression
├── xgboost.pkl                # Modelo XGBoost
├── requirements.txt           # Bibliotecas necessárias
└── README.md                  # Este documento
```

## 🧑‍💻 Autor

**Paciência Aníbal Muienga**  
LinkedIn: [linkedin.com/in/paciencia-muienga](https://linkedin.com/in/paciencia-muienga)

## 🛡️ Licença

Este projeto está sob a licença MIT.
