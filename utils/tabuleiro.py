import chess
import chess.svg
from PIL import Image
import cairosvg
import streamlit as st
import os

def save_board_as_image(fen, filename="tabuleiro.png"):
    """
    Salva o tabuleiro configurado como uma imagem PNG.
    """
    board = chess.Board(fen)

    # Gerar o SVG do tabuleiro
    svg_data = chess.svg.board(board)

    # Converter SVG para PNG usando cairosvg
    try:
        cairosvg.svg2png(bytestring=svg_data, write_to=filename)
        return filename
    except Exception as e:
        st.error(f"Erro ao converter SVG para PNG: {e}")
        return None

def board_editor_function():
    """
    Função principal para o editor de tabuleiro.
    """
    st.title("Editor de Tabuleiro de Xadrez")

    # Posição inicial em FEN
    fen = st.text_input("Insira a configuração do tabuleiro em FEN:", value=chess.STARTING_BOARD_FEN)

    # Exibir o tabuleiro
    st.subheader("Visualização do Tabuleiro Atual")
    board = chess.Board(fen)
    st.write(chess.svg.board(board), unsafe_allow_html=True)

    # Botão para gerar imagem e exportar
    if st.button("Exportar Tabuleiro como Imagem"):
        filename = save_board_as_image(fen)
        if filename:
            st.success("Tabuleiro exportado como imagem com sucesso!")
            # Exibir a imagem no Streamlit
            st.image(filename, caption="Tabuleiro Configurado")

            # Botão para baixar a imagem
            with open(filename, "rb") as file:
                st.download_button(
                    label="Baixar Tabuleiro como PNG",
                    data=file,
                    file_name="tabuleiro.png",
                    mime="image/png"
                )

            # Remover o arquivo gerado localmente (opcional)
            os.remove(filename)

