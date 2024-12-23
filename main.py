if export_format == "PDF":
    pdf_data = generate_pdf(
        st.session_state.get("mhd_data", []),
        "tabuleiro.png",  # Adicione o caminho da imagem gerada
        st.session_state.get("phrases_selected", [])
    )
    st.download_button(
        label="Baixar PDF",
        data=pdf_data,
        file_name="dados_consolidados.pdf",
        mime="application/pdf"
    )
elif export_format == "CSV":
    csv_data = generate_csv(
        st.session_state.get("mhd_data", []),
        st.session_state.get("board_data", ""),  # FEN ainda disponível
        st.session_state.get("phrases_selected", [])
    )
    st.download_button(
        label="Baixar CSV",
        data=csv_data,
        file_name="dados_consolidados.csv",
        mime="text/csv"
    )
