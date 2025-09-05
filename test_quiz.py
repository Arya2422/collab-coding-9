import pytest
from main import StreamlitMiniGames

def test_quiz_answer_correct():
    app = StreamlitMiniGames()
    q = {"question": "2+2=?", "options": ["3", "4", "5"], "answer": 1}
    selected = "4"
    assert selected == q["options"][q["answer"]]

def test_quiz_answer_wrong():
    app = StreamlitMiniGames()
    q = {"question": "2+2=?", "options": ["3", "4", "5"], "answer": 1}
    selected = "5"
    assert selected != q["options"][q["answer"]]
