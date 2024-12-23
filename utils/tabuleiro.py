import chess
from PIL import Image, ImageDraw
import streamlit as st

def generate_board_image(fen, square_size=50):
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

    # Adicionar peças
    for square, piece in board.piece_map().items():
        rank = 7 - chess.square_rank(square)
        file = chess.square_file(square)
        x = file * square_size
        y = rank * square_size

        # Carregar imagem da peça (requer arquivos de peças)
        piece_image_path = f"assets/{piece.symbol().lower()}.png"
        try:
            piece_image = Image.open(piece_image_path).resize((square_size, square_size))
            board_image.paste(piece_image, (x, y), piece_image)
        except FileNotFoundError:
            st.error(f"Imagem da peça não encontrada: {piece_image_path}")

    return board_image

def board_editor_function():
    st.title("Editor de Tabuleiro de Xadrez")

    # Posição inicial em FEN
    fen = st.text_input("Insira a configuração do tabuleiro em FEN:", value=chess.STARTING_BOARD_FEN)

    # Botão para gerar e exibir o tabuleiro
    if st.button("Gerar Tabuleiro"):
        board_image = generate_board_image(fen)
        if board_image:
            st.success("Tabuleiro gerado com sucesso!")
            st.image(board_image, caption="Tabuleiro Configurado", use_column_width=True)

            # Botão para baixar a imagem
            img_bytes = board_image.tobytes()
            st.download_button(
                label="Baixar Tabuleiro como PNG",
                data=img_bytes,
                file_name="tabuleiro.png",
                mime="image/png"
            )

