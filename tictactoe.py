import random
import streamlit as st

# 1. Initialize session state memory
if "board" not in st.session_state:
    st.session_state.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

st.title("Tic Tac Toe")


# 2. Helper function to handle a player's move and trigger the computer
def make_move(index):
    # Only allow a move if the chosen space is empty
    if st.session_state.board[index] == " ":
        # Player places "X"
        st.session_state.board[index] = "X"

        # Find all remaining empty indices
        empty_spots = [
            i for i in range(9) if st.session_state.board[i] == " "
        ]

        # Computer places "O" in a random available space
        if empty_spots:
            computer_choice = random.choice(empty_spots)
            st.session_state.board[computer_choice] = "O"


# 3. Create Row 1
col1, col2, col3 = st.columns(3)
if col1.button(st.session_state.board[0], key="btn_0"):
    make_move(0)
    st.rerun()

if col2.button(st.session_state.board[1], key="btn_1"):
    make_move(1)
    st.rerun()

if col3.button(st.session_state.board[2], key="btn_2"):
    make_move(2)
    st.rerun()

# 4. Create Row 2
col21, col22, col23 = st.columns(3)
if col21.button(st.session_state.board[3], key="btn_3"):
    make_move(3)
    st.rerun()

if col22.button(st.session_state.board[4], key="btn_4"):
    make_move(4)
    st.rerun()

if col23.button(st.session_state.board[5], key="btn_5"):
    make_move(5)
    st.rerun()

# 5. Create Row 3
col31, col32, col33 = st.columns(3)
if col31.button(st.session_state.board[6], key="btn_6"):
    make_move(6)
    st.rerun()

if col32.button(st.session_state.board[7], key="btn_7"):
    make_move(7)
    st.rerun()

if col33.button(st.session_state.board[8], key="btn_8"):
    make_move(8)
    st.rerun()

WINNING_COMBINATIONS = [
    # Rows
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    # Columns
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    # Diagonals
    (0, 4, 8), (2, 4, 6)
]
def check_winner():
    board = st.session_state.board
    for a, b, c in WINNING_COMBINATIONS:
        # Check if spot 'a' isn't empty, and if 'a', 'b', and 'c' are all equal!
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]  # Returns "X" or "O"
    return None
winner = check_winner()
if winner:
    st.success(f"🎉 Player {winner} Wins!")