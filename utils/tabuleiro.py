import streamlit as st
import chess
import chess.svg
import cairosvg
import os

def board_editor_function():
    # Inicialização do tabuleiro no estado global
    if "current_board" not in st.session_state:
        st.session_state.current_board = chess.Board()
    if "board_data" not in st.session_state:
        st.session_state.board_data = st.session_state.current_board.fen()

    # Função para renderizar o tabuleiro com estilo customizado
    def render_tabuleiro_customizado(board):
        return chess.svg.board(
            board=board, 
            size=320,  # Tamanho do tabuleiro
            style=""" 
                .square.light { fill: #ffffff; }  /* Casas claras em branco */
                .square.dark { fill: #8FBC8F; }  /* Casas escuras em verde */
            """
        )

    # Função para salvar o tabuleiro como imagem
    def save_board_as_image(board, filename="tabuleiro.png"):
        svg_data = chess.svg.board(board=board, size=320)
        try:
            cairosvg.svg2png(bytestring=svg_data, write_to=filename)
            return filename
        except Exception as e:
            st.error(f"Erro ao gerar a imagem: {e}")
            return None

    # Configuração do tabuleiro com FEN
    st.subheader("Configuração do Tabuleiro")
    fen_input = st.text_input(
        "Insira a notação FEN para configurar o tabuleiro:", 
        value=st.session_state.current_board.fen(),
        help="Insira uma configuração FEN válida para alterar o tabuleiro."
    )

    if st.button("Atualizar Tabuleiro com FEN"):
        try:
            st.session_state.current_board.set_fen(fen_input)
            st.session_state.board_data = st.session_state.current_board.fen()
            st.success("Tabuleiro atualizado com sucesso!")
        except ValueError:
            st.error("Notação FEN inválida. Por favor, insira uma notação correta.")

    # Visualizar tabuleiro configurado
    st.subheader("Tabuleiro Atual")
    st.image(render_tabuleiro_customizado(st.session_state.current_board), use_container_width=True)

    # Exportar tabuleiro como imagem
    if st.button("Exportar Tabuleiro como Imagem"):
        filename = save_board_as_image(st.session_state.current_board)
        if filename:
            st.success("Tabuleiro exportado como imagem com sucesso!")
            # Botão para baixar o tabuleiro como imagem
            with open(filename, "rb") as file:
                st.download_button(
                    label="Baixar Tabuleiro como PNG",
                    data=file,
                    file_name="tabuleiro.png",
                    mime="image/png"
                )
            # Remover a imagem gerada (opcional)
            os.remove(filename)

    # Mostrar a FEN atual
    st.subheader("Notação FEN Atual")
    st.code(st.session_state.board_data, language="text")
