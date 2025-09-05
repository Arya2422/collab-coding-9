import pytest
from main import StreamlitMiniGames

def test_scramble_word_changes_order():
    app = StreamlitMiniGames()
    word = "python"
    scrambled = app.scramble_word(word)
    assert scrambled != word or len(word) == 1
    assert sorted(scrambled) == sorted(word)
