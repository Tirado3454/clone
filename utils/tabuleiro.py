import chess
import chess.svg
from PIL import Image
import cairosvg
import streamlit as st
import os

def save_board_as_image(fen, filename="tabuleiro.png"):
    # Criar o tabuleiro a partir da configuração FEN
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
    st.title("Editor de Tabuleiro de Xadrez")

    # Posição inicial em FEN
    fen = st.text_input("Insira a configuração do tabuleiro em FEN:", value=chess.STARTING_BOARD_FEN)

    # Botão para gerar e exibir o tabuleiro
    if st.button("Gerar Tabuleiro"):
        filename = save_board_as_image(fen)
        if filename:
            st.success("Tabuleiro gerado com sucesso!")
            # Exibir a imagem no Streamlit
            st.image(filename, caption="Tabuleiro Configurado")

            # Botão para baixar o tabuleiro como imagem
            with open(filename, "rb") as file:
                st.download_button(
                    label="Baixar Tabuleiro como PNG",
                    data=file,
                    file_name="tabuleiro.png",
                    mime="image/png"
                )

            # Remover o arquivo gerado localmente (opcional)
            os.remove(filename)

