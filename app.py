import streamlit as st
from ExtratorDeFilmes import extrair_filmes

st.set_page_config(page_title="Extrator de Filmes", page_icon="🎬")
st.title("🎬 Extrator de Filmes")
st.write("Clique no botão abaixo para extrair os dados dos filmes do catálogo.")

if st.button("Extrair filmes"):
    with st.spinner("Buscando dados, aguarde..."):
        try:
            df = extrair_filmes()
            if df.empty:
                st.warning("Nenhum filme encontrado.")
            else:
                st.success(f"{len(df)} filmes encontrados!")
                st.dataframe(df)
                csv = df.to_csv(index=False).encode("utf-8")
                st.download_button("📥 Baixar CSV", csv, "filmes.csv", "text/csv")
        except Exception as e:
            st.error(f"Erro ao extrair dados: {e}")