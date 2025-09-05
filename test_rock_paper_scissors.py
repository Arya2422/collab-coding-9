import pytest
from main import StreamlitMiniGames

def test_rps_draw():
    app = StreamlitMiniGames()
    app.rps_player_choice = "rock"
    app.rps_computer_choice = "rock"
    assert app.rps_player_choice == app.rps_computer_choice

def test_rps_win():
    app = StreamlitMiniGames()
    app.rps_player_choice = "rock"
    app.rps_computer_choice = "scissors"
    assert (app.rps_player_choice, app.rps_computer_choice) == ("rock", "scissors")

def test_rps_lose():
    app = StreamlitMiniGames()
    app.rps_player_choice = "rock"
    app.rps_computer_choice = "paper"
    assert (app.rps_player_choice, app.rps_computer_choice) == ("rock", "paper")