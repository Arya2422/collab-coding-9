import pytest
import streamlit as st
from main import StreamlitMiniGames

@pytest.fixture(autouse=True)
def clear_session_state():
    # Ensure fresh session state for each test
    try:
        st.session_state.clear()
    except Exception:
        # In some environments session_state may not support clear; ignore
        pass
    yield
    try:
        st.session_state.clear()
    except Exception:
        pass

def test_check_ttt_winner_row():
    app = StreamlitMiniGames()
    board = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
    assert app.check_ttt_winner(board) == 'X'

def test_check_ttt_winner_column():
    app = StreamlitMiniGames()
    board = ['O', ' ', ' ',
             'O', ' ', ' ',
             'O', ' ', ' ']
    assert app.check_ttt_winner(board) == 'O'

def test_check_ttt_winner_diagonal():
    app = StreamlitMiniGames()
    board = ['X', ' ', ' ',
             ' ', 'X', ' ',
             ' ', ' ', 'X']
    assert app.check_ttt_winner(board) == 'X'

def test_check_ttt_winner_none_on_full_board_draw():
    app = StreamlitMiniGames()
    # A full board with no 3-in-a-row (draw)
    board = ['X','O','X',
             'X','O','O',
             'O','X','X']
    assert app.check_ttt_winner(board) is None
    assert ' ' not in board  # confirms board is full -> draw condition in UI logic

def test_empty_board_no_winner():
    app = StreamlitMiniGames()
    board = [' '] * 9
    assert app.check_ttt_winner(board) is None

def test_check_ttt_winner_O_other_diagonal():
    app = StreamlitMiniGames()
    board = [' ', ' ', 'O',
             ' ', 'O', ' ',
             'O', ' ', ' ']
    assert app.check_ttt_winner(board) == 'O'

def test_update_stats_on_ttt_win():
    app = StreamlitMiniGames()
    # initial stats
    assert st.session_state.game_stats['games_played'] == 0
    assert st.session_state.game_stats['total_score'] == 0
    # simulate a win scoring 10 points
    app.update_stats('Tic-Tac-Toe', 10)
    assert st.session_state.game_stats['games_played'] == 1
    assert st.session_state.game_stats['total_score'] == 10
    assert st.session_state.game_stats['play_history'][-1]['game'] == 'Tic-Tac-Toe'
    assert st.session_state.game_stats['favorite_game'] == 'Tic-Tac-Toe'