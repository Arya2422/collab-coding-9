import pytest
from main import StreamlitMiniGames

def test_number_guess_correct():
    app = StreamlitMiniGames()
    app.number_guess_secret = 50
    guess = 50
    assert guess == app.number_guess_secret

def test_number_guess_low():
    app = StreamlitMiniGames()
    app.number_guess_secret = 50
    guess = 25
    assert guess < app.number_guess_secret

def test_number_guess_high():
    app = StreamlitMiniGames()
    app.number_guess_secret = 50
    guess = 75
    assert guess > app.number_guess_secret
    