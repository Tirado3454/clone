import streamlit as st
import chess
from PIL import Image, ImageDraw

def generate_board_image(fen, square_size=60):
    """
    Gera uma imagem do tabuleiro de xadrez a partir de uma configuração FEN.
    """
    board = chess.Board(fen)
    board_image = Image.new("RGB", (square_size * 8, square_size * 8), "white")
    draw = ImageDraw.Draw(board_image)

    # Cores do tabuleiro
    light_color = (240, 217, 181)  # Bege
    dark_color = (181, 136, 99)  # Marrom

    # Desenhar o tabuleiro
    for rank in range(8):
        for file in range(8):
            square_color = light_color if (rank + file) % 2 == 0 else dark_color
            x0 = file * square_size
            y0 = (7 - rank) * square_size
            x1 = x0 + square_size
            y1 = y0 + square_size
            draw.rectangle([x0, y0, x1, y1], fill=square_color)

    # Adicionar peças no tabuleiro
    for square, piece in board.piece_map().items():
        rank = 7 - chess.square_rank(square)
        file = chess.square_file(square)
        x = file * square_size
        y = rank * square_size

        # Desenhar peças como texto (exemplo simplificado)
        piece_color = "black" if piece.color else "white"
        piece_symbol = piece.symbol().upper() if piece.color else piece.symbol().lower()
        draw.text((x + square_size // 3, y + square_size // 4), piece_symbol, fill=piece_color)

    return board_image

def board_editor_function():
    """
    Função principal para o editor de tabuleiro.
    """
    st.title("Editor de Tabuleiro de Xadrez")

    # Posição inicial em FEN
    fen = st.text_input("Insira a configuração do tabuleiro em FEN:", value=chess.STARTING_BOARD_FEN)

    # Exibir o tabuleiro
    st.subheader("Visualização do Tabuleiro Atual")
    board_image = generate_board_image(fen)
    st.image(board_image, caption="Tabuleiro Configurado", use_column_width=True)

    # Exportar tabuleiro como imagem
    if st.button("Exportar Tabuleiro como Imagem"):
        filename = "tabuleiro.png"
        board_image.save(filename, format="PNG")
        st.success("Tabuleiro exportado como imagem com sucesso!")
        # Botão para baixar a imagem
        with open(filename, "rb") as file:
            st.download_button(
                label="Baixar Tabuleiro como PNG",
                data=file,
                file_name="tabuleiro.png",
                mime="image/png"
            )

