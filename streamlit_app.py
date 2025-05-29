import streamlit as st
import numpy as np
import random

# Define Tetris shapes
SHAPES = [
    np.array([[1, 1, 1, 1]]),                        # I
    np.array([[1, 1], [1, 1]]),                      # O
    np.array([[0, 1, 0], [1, 1, 1]]),                # T
    np.array([[1, 0, 0], [1, 1, 1]]),                # J
    np.array([[0, 0, 1], [1, 1, 1]]),                # L
    np.array([[1, 1, 0], [0, 1, 1]]),                # S
    np.array([[0, 1, 1], [1, 1, 0]])                 # Z
]

BOARD_WIDTH = 10
BOARD_HEIGHT = 20

def new_piece():
    shape = random.choice(SHAPES)
    return {"shape": shape, "x": BOARD_WIDTH // 2 - shape.shape[1] // 2, "y": 0}

def check_collision(board, piece, dx=0, dy=0, rotate=False):
    shape = piece["shape"]
    if rotate:
        shape = np.rot90(shape)
    for y in range(shape.shape[0]):
        for x in range(shape.shape[1]):
            if shape[y, x]:
                px = piece["x"] + x + dx
                py = piece["y"] + y + dy
                if px < 0 or px >= BOARD_WIDTH or py >= BOARD_HEIGHT:
                    return True
                if py >= 0 and board[py, px]:
                    return True
    return False

def merge(board, piece):
    shape = piece["shape"]
    for y in range(shape.shape[0]):
        for x in range(shape.shape[1]):
            if shape[y, x]:
                px = piece["x"] + x
                py = piece["y"] + y
                if 0 <= px < BOARD_WIDTH and 0 <= py < BOARD_HEIGHT:
                    board[py, px] = 1
    return board

def clear_lines(board):
    new_board = board[~np.all(board, axis=1)]
    lines_cleared = BOARD_HEIGHT - new_board.shape[0]
    return np.vstack([np.zeros((lines_cleared, BOARD_WIDTH)), new_board]), lines_cleared

def draw_board(board, piece):
    temp_board = board.copy()
    shape = piece["shape"]
    for y in range(shape.shape[0]):
        for x in range(shape.shape[1]):
            if shape[y, x]:
                px = piece["x"] + x
                py = piece["y"] + y
                if 0 <= px < BOARD_WIDTH and 0 <= py < BOARD_HEIGHT:
                    temp_board[py, px] = 2
    return temp_board

def render(board):
    html = ""
    for y in range(BOARD_HEIGHT):
        for x in range(BOARD_WIDTH):
            color = "#222"
            if board[y, x] == 1:
                color = "#888"
            elif board[y, x] == 2:
                color = "#f00"
            html += f'<span style="display:inline-block;width:20px;height:20px;background:{color};border:1px solid #555"></span>'
        html += "<br>"
    return html

if "board" not in st.session_state:
    st.session_state.board = np.zeros((BOARD_HEIGHT, BOARD_WIDTH), dtype=int)
if "piece" not in st.session_state:
    st.session_state.piece = new_piece()
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "score" not in st.session_state:
    st.session_state.score = 0

st.title("Tetris in Streamlit")

if st.session_state.game_over:
    st.write("Game Over! Score:", st.session_state.score)
    if st.button("Restart"):
        st.session_state.board = np.zeros((BOARD_HEIGHT, BOARD_WIDTH), dtype=int)
        st.session_state.piece = new_piece()
        st.session_state.game_over = False
        st.session_state.score = 0
    st.stop()

board = st.session_state.board
piece = st.session_state.piece

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    left = st.button("←")
with col2:
    rotate = st.button("⟳")
with col3:
    down = st.button("↓")
with col4:
    right = st.button("→")
with col5:
    drop = st.button("Drop")

# Handle movement
if left and not check_collision(board, piece, dx=-1):
    piece["x"] -= 1
if right and not check_collision(board, piece, dx=1):
    piece["x"] += 1
if rotate and not check_collision(board, piece, rotate=True):
    piece["shape"] = np.rot90

