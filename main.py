"""
Collaborative Coding Project - Mini Games with Beautiful Streamlit GUI
=====================================================================
A modern, interactive mini-games collection with stunning UI design.

Project: collab-coding-group-[ID]
Theme: Mini Games Collection with Streamlit GUI
"""

import streamlit as st
import random
import time
from typing import List, Dict, Union
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime


# Page configuration with custom styling
st.set_page_config(
    page_title="🎮 Mini Games Collection",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced Custom CSS for beautiful styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    /* Main header styling */
    .main-header {
        font-family: 'Poppins', sans-serif;
        font-size: 2.5rem;
        font-weight: 700;
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Enhanced sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
        padding-top: 2rem;
    }
    
    .sidebar-content {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    .sidebar-title {
        color: white;
        font-family: 'Poppins', sans-serif;
        font-size: 1.5rem;
        font-weight: 600;
        text-align: center;
        margin-bottom: 1rem;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }
    
    .sidebar .sidebar-content .block-container {
        padding: 1rem;
        background: rgba(255,255,255,0.1);
        border-radius: 10px;
        backdrop-filter: blur(10px);
    }
    
    /* Enhanced stats cards - consistent sizing */
    .stats-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        height: 120px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        transition: transform 0.3s ease;
        margin-bottom: 1rem;
    }
    
    .stats-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 35px rgba(0,0,0,0.2);
    }
    
    .stats-card h3 {
        margin: 0;
        font-size: 0.9rem;
        font-weight: 400;
        opacity: 0.9;
    }
    
    .stats-card h2 {
        margin: 0.5rem 0 0 0;
        font-size: 1.8rem;
        font-weight: 700;
    }
    
    /* Game card styling */
    .game-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        margin: 1rem 0;
        transition: transform 0.3s ease;
    }
    
    .game-card:hover {
        transform: translateY(-5px);
    }
    
    /* Winner animation */
    .winner-animation {
        animation: pulse 2s infinite;
        color: #ff6b6b;
        font-size: 1.8rem;
        text-align: center;
        padding: 1rem;
        background: linear-gradient(135deg, #ffeaa7, #fab1a0);
        border-radius: 15px;
        margin: 1rem 0;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    /* Enhanced button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    }
    
    /* Radio button styling for sidebar */
    .stRadio > div {
        background: rgba(255,255,255,0.1);
        border-radius: 10px;
        padding: 0.5rem;
        margin: 0.2rem 0;
    }
    
    .stRadio > div > label {
        color: white;
        font-weight: 500;
        padding: 0.5rem;
        border-radius: 8px;
        transition: background 0.3s ease;
    }
    
    .stRadio > div > label:hover {
        background: rgba(255,255,255,0.2);
    }
    
    /* Welcome section styling */
    .welcome-section {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        padding: 2rem;
        border-radius: 20px;
        margin: 2rem 0;
        text-align: center;
    }
    
    .game-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1rem;
        margin: 2rem 0;
    }
    
    .game-item {
        background: linear-gradient(135deg, #74b9ff, #0984e3);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        transition: transform 0.3s ease;
    }
    
    .game-item:hover {
        transform: translateY(-5px);
    }
    
    /* Footer styling */
    .footer {
        text-align: center;
        color: #666;
        padding: 2rem;
        background: linear-gradient(135deg, #f8f9fa, #e9ecef);
        border-radius: 15px;
        margin-top: 3rem;
    }
</style>
""", unsafe_allow_html=True)


class StreamlitMiniGames:
    """Beautiful Streamlit Mini Games Collection"""
    
    def __init__(self):
        if 'game_stats' not in st.session_state:
            st.session_state.game_stats = {
                'games_played': 0,
                'total_score': 0,
                'favorite_game': 'None',
                'play_history': []
            }
    
    def display_header(self):
        """Display beautiful animated header with consistent stats cards"""
        st.markdown('<h1 class="main-header">🎮 Mini Games Collection</h1>', unsafe_allow_html=True)
        st.markdown("---")
        
        # Calculate average score
        avg_score = 0
        if st.session_state.game_stats['play_history']:
            avg_score = sum(game['score'] for game in st.session_state.game_stats['play_history']) / len(st.session_state.game_stats['play_history'])
        
        # Enhanced stats display with consistent card sizing
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown(f"""
            <div class="stats-card">
                <h3>🎯 Games Played</h3>
                <h2>{st.session_state.game_stats['games_played']}</h2>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="stats-card">
                <h3>⭐ Total Score</h3>
                <h2>{st.session_state.game_stats['total_score']}</h2>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div class="stats-card">
                <h3>❤️ Favorite Game</h3>
                <h2 style="font-size: 1.2rem;">{st.session_state.game_stats['favorite_game']}</h2>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown(f"""
            <div class="stats-card">
                <h3>📊 Average Score</h3>
                <h2>{avg_score:.1f}</h2>
            </div>
            """, unsafe_allow_html=True)
    
    def display_enhanced_sidebar(self):
        """Display enhanced sidebar with beautiful styling"""
        st.sidebar.markdown("""
        <div class="sidebar-title">
            🎮 Game Menu
        </div>
        """, unsafe_allow_html=True)
        
        # Add some spacing
        st.sidebar.markdown("<br>", unsafe_allow_html=True)
        
        games = {
            "🏠 Home": "home",
            "🎯 Number Guessing": "number_guessing",
            "✂️ Rock Paper Scissors": "rock_paper_scissors", 
            "🔤 Word Scramble": "word_scramble",
            "🧠 Quiz Game": "quiz",
            "❌⭕ Tic-Tac-Toe": "tic_tac_toe",
            "📊 Analytics": "analytics"
        }
        
        selected_game = st.sidebar.radio(
            "",
            list(games.keys()),
            key="game_selector"
        )
        
        # Add some game tips in sidebar
        st.sidebar.markdown("---")
        st.sidebar.markdown("""
        <div style="background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 10px; color: white;">
            <h4>💡 Quick Tips</h4>
            <ul style="font-size: 0.9rem;">
                <li>Play regularly to improve your average score</li>
                <li>Try different difficulty levels</li>
                <li>Check Analytics to track progress</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        return games[selected_game]
   
  #number guessing 
 
    def number_guessing_game(self):
        """
        Beautiful Number Guessing Game with Streamlit
        Author: Dakshish
        """
        st.markdown("## 🎯 Number Guessing Game")
        st.markdown("*I'm thinking of a number between 1 and 100. Can you guess it?*")
        
        # Initialize game state
        if 'number_game' not in st.session_state:
            st.session_state.number_game = {
                'secret_number': random.randint(1, 100),
                'attempts': 0,
                'max_attempts': 7,
                'game_over': False,
                'won': False,
                'hints': []
            }
        
        game = st.session_state.number_game
        
        if not game['game_over']:
            col1, col2 = st.columns([3, 1])
            
            with col1:
                guess = st.number_input(
                    f"Attempt {game['attempts'] + 1}/{game['max_attempts']} - Enter your guess:",
                    min_value=1,
                    max_value=100,
                    value=50,
                    key=f"guess_input_{game['attempts']}"
                )
            
            with col2:
                if st.button("🎯 Submit Guess", key="submit_guess"):
                    game['attempts'] += 1
                    
                    if guess == game['secret_number']:
                        game['won'] = True
                        game['game_over'] = True
                        score = max(100 - (game['attempts'] - 1) * 10, 10)
                        self.update_stats('Number Guessing', score)
                        
                        st.markdown(f'<div class="winner-animation">🎉 Congratulations! You guessed it in {game["attempts"]} attempts!</div>', unsafe_allow_html=True)
                        st.balloons()
                        
                    elif game['attempts'] >= game['max_attempts']:
                        game['game_over'] = True
                        st.error(f"😔 Game Over! The number was {game['secret_number']}")
                        self.update_stats('Number Guessing', 0)
                        
                    else:
                        if guess < game['secret_number']:
                            hint = f"📈 Too low! Try a higher number."
                            st.info(hint)
                        else:
                            hint = f"📉 Too high! Try a lower number."
                            st.info(hint)
                        
                        game['hints'].append(f"Attempt {game['attempts']}: {guess} - {hint}")
            
            # Display hints history
            if game['hints']:
                st.markdown("### 💡 Previous Hints:")
                for hint in game['hints'][-3:]:  # Show last 3 hints
                    st.text(hint)
            
            # Progress bar
            progress = game['attempts'] / game['max_attempts']
            st.progress(progress)
            
        else:
            if st.button("🔄 Play Again"):
                del st.session_state.number_game
                st.rerun()


  # rock_paper_scissors
def rock_paper_scissors(self):
        """
        Beautiful Rock Paper Scissors with Streamlit
        Author: Rishabh
        """
        st.markdown("## ✂️ Rock Paper Scissors")
        st.markdown("*Choose your weapon and battle the computer!*")
        
        # Initialize game state
        if 'rps_game' not in st.session_state:
            st.session_state.rps_game = {
                'player_wins': 0,
                'computer_wins': 0,
                'draws': 0,
                'game_history': []
            }
        
        game = st.session_state.rps_game
        choices = ["🪨 Rock", "📄 Paper", "✂️ Scissors"]
        choice_map = {"🪨 Rock": "rock", "📄 Paper": "paper", "✂️ Scissors": "scissors"}
        
        # Score display
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("🎮 Your Wins", game['player_wins'])
        with col2:
            st.metric("🤖 Computer Wins", game['computer_wins'])
        with col3:
            st.metric("🤝 Draws", game['draws'])
        
        # Game interface
        st.markdown("### Make Your Choice:")
        selected_choice = st.radio("", choices, horizontal=True, key="rps_choice")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("⚔️ BATTLE!", key="rps_battle", use_container_width=True):
                player_choice = choice_map[selected_choice]
                computer_choice = random.choice(["rock", "paper", "scissors"])
                
                # Determine winner
                result = self.determine_rps_winner(player_choice, computer_choice)
                
                if result == "draw":
                    game['draws'] += 1
                    result_text = "🤝 It's a draw!"
                    result_color = "blue"
                    score = 5
                elif result == "win":
                    game['player_wins'] += 1
                    result_text = "🎉 You win!"
                    result_color = "green"
                    score = 10
                else:
                    game['computer_wins'] += 1
                    result_text = "🤖 Computer wins!"
                    result_color = "red"
                    score = 0
                
                self.update_stats('Rock Paper Scissors', score)
                
                # Display result with animation
                computer_emoji = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}
                
                st.markdown(f"""
                <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #ffeaa7, #fab1a0); border-radius: 15px; margin: 1rem 0;">
                    <h2>You: {selected_choice} VS Computer: {computer_emoji[computer_choice]} {computer_choice.title()}</h2>
                    <h1 style="color: {result_color};">{result_text}</h1>
                </div>
                """, unsafe_allow_html=True)
                
                game['game_history'].append({
                    'player': player_choice,
                    'computer': computer_choice,
                    'result': result
                })
        
        # Game history
        if game['game_history']:
            st.markdown("### 📊 Recent Games:")
            recent_games = game['game_history'][-5:]  # Show last 5 games
            df = pd.DataFrame(recent_games)
            st.dataframe(df, use_container_width=True)
    
    def determine_rps_winner(self, player_choice, computer_choice):
        """Determine Rock Paper Scissors winner"""
        if player_choice == computer_choice:
            return "draw"
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            return "win"
        else:
            return "lose"

   #Word_scramble 
    

    def word_scramble_game(self):
        """
        Beautiful Word Scramble Game with Streamlit
        Author: Rishika
        """
        st.markdown("## 🔤 Word Scramble Game")
        st.markdown("*Unscramble the letters to form the original word!*")
        
        # Word lists
        word_lists = {
            "Easy 🟢": ["cat", "dog", "sun", "car", "book", "tree", "fish", "bird"],
            "Medium 🟡": ["python", "computer", "keyboard", "program", "function", "variable"],
            "Hard 🔴": ["programming", "algorithm", "collaboration", "development", "repository"]
        }
        
        # Initialize game state
        if 'scramble_game' not in st.session_state:
            st.session_state.scramble_game = {
                'current_word': '',
                'scrambled_word': '',
                'score': 0,
                'round': 1,
                'total_rounds': 5,
                'difficulty': 'Easy 🟢',
                'start_time': 0,
                'game_active': False
            }
        
        game = st.session_state.scramble_game
        
        # Difficulty selection
        col1, col2 = st.columns([2, 1])
        with col1:
            difficulty = st.selectbox("Choose Difficulty:", list(word_lists.keys()), 
                                    index=list(word_lists.keys()).index(game['difficulty']))
            game['difficulty'] = difficulty
        
        with col2:
            st.metric("Current Score", game['score'])
        
        # Game controls
        if not game['game_active']:
            if st.button("🎮 Start New Game", use_container_width=True):
                game['current_word'] = random.choice(word_lists[difficulty])
                game['scrambled_word'] = self.scramble_word(game['current_word'])
                game['start_time'] = time.time()
                game['game_active'] = True
                game['round'] = 1
                game['score'] = 0
                st.rerun()
        
        if game['game_active']:
            # Progress indicator
            progress = (game['round'] - 1) / game['total_rounds']
            st.progress(progress, text=f"Round {game['round']}/{game['total_rounds']}")
            
            # Display scrambled word
            st.markdown(f"""
            <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #a8edea, #fed6e3); border-radius: 15px; margin: 2rem 0;">
                <h1 style="font-size: 3rem; letter-spacing: 10px; color: #2d3436;">{game['scrambled_word'].upper()}</h1>
                <p>Unscramble this word!</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Input and submit
            col1, col2 = st.columns([3, 1])
            with col1:
                user_guess = st.text_input("Your guess:", key=f"scramble_guess_{game['round']}")
            
            with col2:
                if st.button("✅ Submit"):
                    if user_guess.lower() == game['current_word'].lower():
                        time_taken = time.time() - game['start_time']
                        points = max(20 - int(time_taken), 5)
                        game['score'] += points
                        
                        st.success(f"🎉 Correct! +{points} points")
                        
                        if game['round'] < game['total_rounds']:
                            game['round'] += 1
                            game['current_word'] = random.choice(word_lists[difficulty])
                            game['scrambled_word'] = self.scramble_word(game['current_word'])
                            game['start_time'] = time.time()
                            time.sleep(1)
                            st.rerun()
                        else:
                            game['game_active'] = False
                            self.update_stats('Word Scramble', game['score'])
                            st.markdown('<div class="winner-animation">🏆 Game Complete!</div>', unsafe_allow_html=True)
                            st.balloons()
                    else:
                        st.error(f"❌ Wrong! The word was: {game['current_word']}")
                        if game['round'] < game['total_rounds']:
                            game['round'] += 1
                            game['current_word'] = random.choice(word_lists[difficulty])
                            game['scrambled_word'] = self.scramble_word(game['current_word'])
                            game['start_time'] = time.time()
                            time.sleep(1)
                            st.rerun()
                        else:
                            game['game_active'] = False
                            self.update_stats('Word Scramble', game['score'])
    
    def scramble_word(self, word):
        """Scramble the letters of a word"""
        scrambled = list(word)
        random.shuffle(scrambled)
        # Ensure the scrambled word is different from original
        while ''.join(scrambled) == word and len(word) > 1:
            random.shuffle(scrambled)
        return ''.join(scrambled)
    
    
    ## quiz gamee
    
    def simple_quiz_game(self):
        """
        Beautiful Quiz Game with Streamlit
        Author: Arya
        """
        st.markdown("## 🧠 Quiz Game")
        st.markdown("*Test your knowledge with our interactive quiz!*")
        
        # Quiz data
        quiz_data = {
            "General Knowledge 🌍": [
                {
                    "question": "What is the capital of France?",
                    "options": ["London", "Berlin", "Paris", "Madrid"],
                    "answer": 2,
                    "explanation": "Paris is the capital and largest city of France."
                },
                {
                    "question": "Which planet is known as the Red Planet?",
                    "options": ["Venus", "Mars", "Jupiter", "Saturn"],
                    "answer": 1,
                    "explanation": "Mars is called the Red Planet due to iron oxide on its surface."
                },
                {
                    "question": "What is 7 × 8?",
                    "options": ["54", "56", "58", "64"],
                    "answer": 1,
                    "explanation": "7 × 8 = 56"
                }
            ],
            "Programming 💻": [
                {
                    "question": "Which language is primarily used for web development?",
                    "options": ["Python", "JavaScript", "Java", "C++"],
                    "answer": 1,
                    "explanation": "JavaScript is the primary language for client-side web development."
                },
                {
                    "question": "What does 'HTML' stand for?",
                    "options": ["High Tech Modern Language", "HyperText Markup Language", 
                             "Home Tool Markup Language", "Hyperlink Text Management Language"],
                    "answer": 1,
                    "explanation": "HTML stands for HyperText Markup Language."
                },
                {
                    "question": "Which is a version control system?",
                    "options": ["Git", "Python", "MySQL", "CSS"],
                    "answer": 0,
                    "explanation": "Git is a distributed version control system."
                }
            ]
        }
        
        # Initialize quiz state
        if 'quiz_game' not in st.session_state:
            st.session_state.quiz_game = {
                'category': 'General Knowledge 🌍',
                'current_question': 0,
                'score': 0,
                'answers': [],
                'quiz_active': False,
                'quiz_complete': False
            }
        
        game = st.session_state.quiz_game
        
        # Category selection
        if not game['quiz_active']:
            col1, col2 = st.columns([2, 1])
            with col1:
                category = st.selectbox("Choose Quiz Category:", list(quiz_data.keys()))
                game['category'] = category
            
            with col2:
                if st.button("🚀 Start Quiz", use_container_width=True):
                    game['quiz_active'] = True
                    game['current_question'] = 0
                    game['score'] = 0
                    game['answers'] = []
                    game['quiz_complete'] = False
                    st.rerun()
        
        if game['quiz_active'] and not game['quiz_complete']:
            questions = quiz_data[game['category']]
            current_q = questions[game['current_question']]
            
            # Progress bar
            progress = (game['current_question']) / len(questions)
            st.progress(progress, text=f"Question {game['current_question'] + 1}/{len(questions)}")
            
            # Question display
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #74b9ff, #0984e3); padding: 2rem; border-radius: 15px; margin: 2rem 0;">
                <h2 style="color: white; text-align: center;">Question {game['current_question'] + 1}</h2>
                <h3 style="color: white; text-align: center;">{current_q['question']}</h3>
            </div>
            """, unsafe_allow_html=True)
            
            # Answer options
            selected_answer = st.radio(
                "Choose your answer:",
                current_q['options'],
                key=f"quiz_answer_{game['current_question']}"
            )
            
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                if st.button("📝 Submit Answer", use_container_width=True):
                    selected_index = current_q['options'].index(selected_answer)
                    is_correct = selected_index == current_q['answer']
                    
                    if is_correct:
                        game['score'] += 10
                        st.success("✅ Correct! " + current_q['explanation'])
                    else:
                        correct_answer = current_q['options'][current_q['answer']]
                        st.error(f"❌ Wrong! The correct answer was: {correct_answer}")
                        st.info(current_q['explanation'])
                    
                    game['answers'].append({
                        'question': current_q['question'],
                        'selected': selected_answer,
                        'correct': current_q['options'][current_q['answer']],
                        'is_correct': is_correct
                    })
                    
                    if game['current_question'] < len(questions) - 1:
                        game['current_question'] += 1
                        time.sleep(2)
                        st.rerun()
                    else:
                        game['quiz_complete'] = True
                        game['quiz_active'] = False
                        st.rerun()
        
        # Quiz results
        if game['quiz_complete']:
            total_questions = len(quiz_data[game['category']])
            percentage = (game['score'] / (total_questions * 10)) * 100
            
            self.update_stats('Quiz Game', game['score'])
            
            # Results display with beautiful styling
            if percentage >= 80:
                grade = "🌟 Excellent!"
                color = "#00b894"
            elif percentage >= 60:
                grade = "👍 Good Job!"
                color = "#fdcb6e"
            else:
                grade = "📚 Keep Studying!"
                color = "#e17055"
            
            st.markdown(f"""
            <div style="text-align: center; padding: 3rem; background: linear-gradient(135deg, #a8edea, #fed6e3); border-radius: 20px; margin: 2rem 0;">
                <h1>🏆 Quiz Complete!</h1>
                <h2>Score: {game['score']}/{total_questions * 10}</h2>
                <h2>Percentage: {percentage:.1f}%</h2>
                <h1 style="color: {color};">{grade}</h1>
            </div>
            """, unsafe_allow_html=True)
            
            # Results breakdown
            st.markdown("### 📊 Detailed Results:")
            for i, answer in enumerate(game['answers'], 1):
                icon = "✅" if answer['is_correct'] else "❌"
                st.write(f"{icon} **Q{i}:** {answer['question']}")
                st.write(f"Your answer: {answer['selected']}")
                if not answer['is_correct']:
                    st.write(f"Correct answer: {answer['correct']}")
                st.write("---")
            
            if st.button("🔄 Take Another Quiz"):
                del st.session_state.quiz_game
                st.rerun()
    
#tic tac toe
    def tic_tac_toe(self):
        """
        Beautiful Tic-Tac-Toe with Streamlit
        Author: Rahul Trimukhe
        """
        st.markdown("## ❌⭕ Tic-Tac-Toe")
        st.markdown("*Classic game for two players!*")
        
        # Initialize game state
        if 'ttt_game' not in st.session_state:
            st.session_state.ttt_game = {
                'board': [' '] * 9,
                'current_player': 'X',
                'game_over': False,
                'winner': None,
                'x_wins': 0,
                'o_wins': 0,
                'draws': 0
            }
        
        game = st.session_state.ttt_game
        
        # Score display
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("❌ X Wins", game['x_wins'])
        with col2:
            st.metric("⭕ O Wins", game['o_wins'])
        with col3:
            st.metric("🤝 Draws", game['draws'])
        
        # Current player indicator
        if not game['game_over']:
            st.markdown(f"""
            <div style="text-align: center; padding: 1rem; background: linear-gradient(135deg, #6c5ce7, #a29bfe); 
                        border-radius: 10px; margin: 1rem 0;">
                <h2 style="color: white;">Current Player: {game['current_player']}</h2>
            </div>
            """, unsafe_allow_html=True)
        
        # Game board
        st.markdown("### Game Board:")
        
        # Create 3x3 grid
        for row in range(3):
            cols = st.columns(3)
            for col in range(3):
                position = row * 3 + col
                cell_value = game['board'][position]
                
                # Display cell content with beautiful styling
                if cell_value == ' ':
                    display_value = str(position + 1)
                    button_style = "background: linear-gradient(135deg, #ddd6fe, #e0e7ff);"
                else:
                    display_value = cell_value
                    if cell_value == 'X':
                        button_style = "background: linear-gradient(135deg, #fecaca, #f87171);"
                    else:
                        button_style = "background: linear-gradient(135deg, #bfdbfe, #60a5fa);"
                
                with cols[col]:
                    if st.button(
                        display_value,
                        key=f"cell_{position}",
                        disabled=game['board'][position] != ' ' or game['game_over'],
                        use_container_width=True
                    ):
                        game['board'][position] = game['current_player']
                        
                        # Check for winner
                        winner = self.check_ttt_winner(game['board'])
                        if winner:
                            game['winner'] = winner
                            game['game_over'] = True
                            if winner == 'X':
                                game['x_wins'] += 1
                            else:
                                game['o_wins'] += 1
                            self.update_stats('Tic-Tac-Toe', 10)
                        elif ' ' not in game['board']:
                            game['game_over'] = True
                            game['winner'] = 'Draw'
                            game['draws'] += 1
                            self.update_stats('Tic-Tac-Toe', 5)
                        else:
                            game['current_player'] = 'O' if game['current_player'] == 'X' else 'X'
                        
                        st.rerun()
        
        # Game result
        if game['game_over']:
            if game['winner'] == 'Draw':
                st.markdown('<div class="winner-animation">🤝 It\'s a Draw!</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="winner-animation">🎉 Player {game["winner"]} Wins!</div>', unsafe_allow_html=True)
                st.balloons()
            
            if st.button("🔄 New Game", use_container_width=True):
                game['board'] = [' '] * 9
                game['current_player'] = 'X'
                game['game_over'] = False
                game['winner'] = None
                st.rerun()
    
    def check_ttt_winner(self, board):
        """Check for Tic-Tac-Toe winner"""
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        
        for combo in win_combinations:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
                return board[combo[0]]
        return None
    

    ###Written by Arya
    def update_stats(self, game_name, score):
        """Update player statistics"""
        st.session_state.game_stats['games_played'] += 1
        st.session_state.game_stats['total_score'] += score
        
        # Add to play history
        st.session_state.game_stats['play_history'].append({
            'game': game_name,
            'score': score,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
        
        # Update favorite game based on frequency
        game_counts = {}
        for game_record in st.session_state.game_stats['play_history']:
            game_counts[game_record['game']] = game_counts.get(game_record['game'], 0) + 1
        
        if game_counts:
            st.session_state.game_stats['favorite_game'] = max(game_counts, key=game_counts.get)
    
    def display_analytics(self):
        """Display beautiful game analytics"""
        st.markdown("## 📊 Game Analytics")
        
        if not st.session_state.game_stats['play_history']:
            st.info("🎮 Play some games to see your analytics!")
            return
        
        # Create DataFrames for analysis
        df = pd.DataFrame(st.session_state.game_stats['play_history'])
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        
        col1, col2 = st.columns(2)
        
        # Games played by type
        with col1:
            game_counts = df['game'].value_counts()
            fig_pie = px.pie(
                values=game_counts.values, 
                names=game_counts.index, 
                title="🎯 Games Played by Type",
                color_discrete_sequence=px.colors.qualitative.Set3
            )
            fig_pie.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig_pie, use_container_width=True)
        
        # Score progression over time
        with col2:
            df_sorted = df.sort_values('timestamp')
            df_sorted['cumulative_score'] = df_sorted['score'].cumsum()
            
            fig_line = px.line(
                df_sorted, 
                x='timestamp', 
                y='cumulative_score',
                title='📈 Score Progression Over Time',
                markers=True
            )
            fig_line.update_layout(
                xaxis_title="Time",
                yaxis_title="Cumulative Score",
                showlegend=False
            )
            st.plotly_chart(fig_line, use_container_width=True)
        
        # Recent games table
        st.markdown("### 🕒 Recent Games")
        recent_df = df.tail(10).sort_values('timestamp', ascending=False)
        st.dataframe(
            recent_df[['game', 'score', 'timestamp']], 
            use_container_width=True,
            hide_index=True
        )
    
    def display_home_page(self):
        """Display simplified and elegant home page"""
        st.markdown("""
        <div class="welcome-section">
            <h2>🌟 Welcome to the Mini Games Collection!</h2>
            <p>Choose from our exciting collection of games and start playing!</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Game grid layout
        st.markdown("""
        <div class="game-grid">
            <div class="game-item">
                <h3>🎯 Number Guessing</h3>
                <p>Test your intuition!</p>
            </div>
            <div class="game-item">
                <h3>✂️ Rock Paper Scissors</h3>
                <p>Battle the computer!</p>
            </div>
            <div class="game-item">
                <h3>🔤 Word Scramble</h3>
                <p>Unscramble words!</p>
            </div>
            <div class="game-item">
                <h3>🧠 Quiz Game</h3>
                <p>Test your knowledge!</p>
            </div>
            <div class="game-item">
                <h3>❌⭕ Tic-Tac-Toe</h3>
                <p>Classic strategy!</p>
            </div>
            <div class="game-item">
                <h3>📊 Analytics</h3>
                <p>Track your progress!</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Display recent achievements if any
        if st.session_state.game_stats['play_history']:
            st.markdown("### 🏆 Recent Achievement")
            recent_game = st.session_state.game_stats['play_history'][-1]
            st.success(f"🎮 Last played: {recent_game['game']} - Score: {recent_game['score']} points!")
    
    def run(self):
        """Main application runner"""
        # Enhanced sidebar navigation
        selected_game = self.display_enhanced_sidebar()
        
        # Display header on all pages except analytics
        if selected_game != "analytics":
            self.display_header()
        
        # Game routing
        if selected_game == "home":
            self.display_home_page()
        elif selected_game == "number_guessing":
            self.number_guessing_game()
        elif selected_game == "rock_paper_scissors":
            self.rock_paper_scissors()
        elif selected_game == "word_scramble":
            self.word_scramble_game()
        elif selected_game == "quiz":
            self.simple_quiz_game()
        elif selected_game == "tic_tac_toe":
            self.tic_tac_toe()
        elif selected_game == "analytics":
            self.display_analytics()
        
        # Enhanced footer
        st.markdown("""
        <div class="footer">
            🎮 <strong>Mini Games Collection</strong> | Built with ❤️ using Streamlit<br>
            <em>Collaborative Coding Project - Beautiful Gaming Experience</em>
        </div>
        """, unsafe_allow_html=True)


# Application entry point
if __name__ == "__main__":
    # Initialize and run the app
    games_app = StreamlitMiniGames()
    games_app.run()
