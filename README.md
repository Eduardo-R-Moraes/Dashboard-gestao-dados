# 📊 Dashboard Gestão de Dados

## 📝 Sobre o Projeto

Este projeto é um **dashboard interativo** desenvolvido durante as aulas de gestão de dados com **Streamlit**, **Pandas** e **Plotly**, focado na análise de vendas. Ele permite visualizar métricas de faturamento, número de vendas, avaliação média e total de produtos vendidos. Além disso, inclui uma funcionalidade de **recomendação de produtos** baseada no perfil do cliente utilizando um modelo de Machine Learning.

---

## 🚀 Tecnologias Utilizadas

- **Python** 🐍
- **Streamlit** (para a interface interativa)
- **Pandas** (para manipulação de dados)
- **Plotly** (para visualizações gráficas dinâmicas)
- **Scikit-Learn** (para Machine Learning - recomendação de produtos)

---

## 📊 Funcionalidades

### 1️⃣ Visualização de Dados
- **Resumo de métricas principais:**
  - Total de faturamento 💰
  - Total de vendas 🛒
  - Avaliação média ⭐
  - Total de produtos vendidos 📦
- **Filtros personalizáveis:**
  - Selecione o mês desejado 📆
  - Filtre por gênero de clientes 🧑‍🤝‍🧑
- **Gráficos interativos:**
  - Faturamento por dia 📅
  - Faturamento por tipo de produto 🎯
  - Faturamento por cidade 🏙️
  - Faturamento por tipo de pagamento 💳
  - Avaliação média por cidade ⭐

### 2️⃣ Recomendação de Produto via Machine Learning 🤖
- O usuário insere **gênero, cidade e preço**.
- O modelo KNN prevê **qual linha de produto** esse cliente provavelmente compraria.

---

## ▶️ Como Executar

### 1️⃣ Instale as Dependências
Certifique-se de ter **Python 3.8+** instalado. Depois, instale os pacotes necessários:
```bash
pip install streamlit pandas plotly scikit-learn
```

### 2️⃣ Execute o Dashboard
Navegue até a pasta do projeto e execute:
```bash
streamlit run dashboard.py
```
Isso abrirá o dashboard automaticamente no navegador.

---

