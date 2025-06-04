import pandas as pd
import streamlit as st

# Título e descrição
st.title("🎧 Artistas mais ouvidos no Spotify em 2024")

# Lê os dados
df = pd.read_csv("artistas_spotify_2024.csv")

# Mostra a tabela
st.subheader("📋 Tabela de artistas e ouvintes")
st.dataframe(df)

# Mostra o gráfico de barras
st.subheader("📊 Gráfico de ouvintes por artista (em milhões)")
st.bar_chart(df.set_index("artista"))
