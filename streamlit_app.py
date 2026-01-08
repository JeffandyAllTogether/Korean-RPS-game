import streamlit as st
import random

# ASCII Art
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Map choices to art
art = {"R": rock, "P": paper, "S": scissors}
names = {"R": "보 (Rock)", "P": "바위 (Paper)", "S": "가위 (Scissors)"}

# Page config
st.set_page_config(page_title="가위 바위 보!", page_icon="✊🏾")

st.markdown("""
<style>
    .code-editor {
        background-color: #1e1e1e;
        border-radius: 8px;
        padding: 20px;
        font-family: 'Courier New', monospace;
        font-size: 0.9rem;
        color: #d4d4d4;
        max-height: 500px;
        overflow-y: auto;
    }
    .code-header {
        background-color: #2d2d2d;
        padding: 10px;
        border-radius: 8px 8px 0 0;
        color: #cccccc;
        font-family: 'Courier New', monospace;
    }
    .line-number {
        color: #858585;
        display: inline-block;
        width: 50px;
        min-width: 50px;
        text-align: left;
        margin-right: 20px;
        padding-right: 10px;
        border-right: 1px solid #3e3e3e;
        user-select: none;
    }
    .keyword {
        color: #569cd6;
    }
    .string {
        color: #ce9178;
    }
    .function {
        color: #dcdcaa;
    }
    .comment {
        color: #6a9955;
    }
</style>
""", unsafe_allow_html=True)


ORIGINAL_CODE = """import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print(f"Welcome to 가위 바위 보!")

decision = ["S","P","R"]
player = str.upper(input("choose S for 가위 (scissors), P for 바위 (paper), or R for 보 (rock)! "))
cpu = random.choice(decision)


#player visual output
if player == "S":
    print(scissors)
if player == "P":
    print(paper)
if player == "R":
    print(rock)

#cpu visual output
if cpu == "S":
    print(scissors)
if cpu == "P":
    print(paper)
if cpu == "R":
    print(rock)

#win or loose

if player == cpu:
    print("it's a DRAW... BOOORING!")
elif player == "S" and cpu == "P":
    print('''    
    ★★★★★★★★★★★★★★★★★★★★★★★★★★
          당신이 이겼어요!
           YOU WIN!
    ★★★★★★★★★★★★★★★★★★★★★★★★★★''')
elif player == "P" and cpu == "R":
    print('''    
        ★★★★★★★★★★★★★★★★★★★★★★★★★★
              당신이 이겼어요!
               YOU WIN!
        ★★★★★★★★★★★★★★★★★★★★★★★★★★''')
elif player == "R" and cpu == "S":
    print('''     
        ★★★★★★★★★★★★★★★★★★★★★★★★★★
              당신이 이겼어요!
               YOU WIN!
        ★★★★★★★★★★★★★★★★★★★★★★★★★★''')
else:
    print('''
    ╔══════════════════════════════╗
    ║        GAME OVER             ║
    ║                              ║
    ║      당신이 졌어요               ║
    ║   (YOU LOOSE!!!!)            ║
    ║                              ║
    ╚══════════════════════════════╝''')
"""

# Initialize session state for scores (persists across button clicks)
if "player_score" not in st.session_state:
    st.session_state.player_score = 0
if "cpu_score" not in st.session_state:
    st.session_state.cpu_score = 0
if "games_played" not in st.session_state:
    st.session_state.games_played = 0
if "streak" not in st.session_state:
    st.session_state.streak = 0

st.title("✌🏾 ✋🏾 ✊🏾 가위 바위 보!")
st.subheader("Rock Paper Scissors - Korean Style")

st.markdown("---")

# 🔴 MULTIPLE PLACEHOLDERS - Reserve spots at the top
score_placeholder = st.empty()
result_placeholder = st.empty()
streak_placeholder = st.empty()
hands_placeholder = st.empty()

st.markdown("---")

# Display current score (before any game is played)
score_placeholder.markdown(
    f"### 🎮 Score: You **{st.session_state.player_score}** - **{st.session_state.cpu_score}** CPU"
)

# Player choice
choice = st.radio(
    "Choose your weapon:",
    options=["S", "P", "R"],
    format_func=lambda x: names[x],
    horizontal=True
)

# Two columns for buttons
col_play, col_reset = st.columns([1, 1])

with col_play:
    play_button = st.button("Play! 시작!", type="primary", use_container_width=True)

with col_reset:
    reset_button = st.button("Reset Score 🔄", use_container_width=True)

# Reset logic
if reset_button:
    st.session_state.player_score = 0
    st.session_state.cpu_score = 0
    st.session_state.games_played = 0
    st.session_state.streak = 0
    st.rerun()

# Play logic
if play_button:
    cpu = random.choice(["S", "P", "R"])
    st.session_state.games_played += 1
    
    # Determine winner
    if choice == cpu:
        result = "draw"
        st.session_state.streak = 0
    elif (choice == "S" and cpu == "P") or \
         (choice == "P" and cpu == "R") or \
         (choice == "R" and cpu == "S"):
        result = "win"
        st.session_state.player_score += 1
        st.session_state.streak += 1
    else:
        result = "lose"
        st.session_state.cpu_score += 1
        st.session_state.streak = 0

        # Update score placeholder
    score_placeholder.markdown(
        f"### 🎮 Score: You **{st.session_state.player_score}** - **{st.session_state.cpu_score}** CPU"
    )

    # Update result placeholder
    if result == "draw":
        result_placeholder.warning("## 🤝 It's a DRAW... BOOORING!")
    elif result == "win":
        result_placeholder.success("## ★ 당신이 이겼어요! YOU WIN! ★")
        st.balloons()
    else:
        result_placeholder.error("## 💀 당신이 졌어요... YOU LOSE!")

    # Update streak placeholder
    if st.session_state.streak >= 2:
        streak_placeholder.info(f"🔥 {st.session_state.streak} game win streak!")
    elif st.session_state.streak == 0 and result == "lose":
        streak_placeholder.caption("💔 Streak broken...")
    else:
        streak_placeholder.empty()
    
    # Display ASCII art hands using a container inside the placeholder
    with hands_placeholder.container():
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### You chose:")
            st.code(art[choice], language=None)
            st.caption(names[choice])
        
        with col2:
            st.markdown("### CPU chose:")
            st.code(art[cpu], language=None)
            st.caption(names[cpu])
    
    st.markdown("---")
    
    # # Determine winner
    # if choice == cpu:
    #     st.warning("## 🤝 It's a DRAW... BOOORING!")
    # elif (choice == "S" and cpu == "P") or \
    #      (choice == "P" and cpu == "R") or \
    #      (choice == "R" and cpu == "S"):
    #     st.success("## ★ 당신이 이겼어요! YOU WIN! ★")
    #     st.balloons()
    # else:
    #     st.error("## 💀 당신이 졌어요... YOU LOSE!")

st.markdown("---")

# Stats footer
if st.session_state.games_played > 0:
    win_rate = (st.session_state.player_score / st.session_state.games_played) * 100
    st.caption(f"Games played: {st.session_state.games_played} | Win rate: {win_rate:.1f}%")

st.caption("Built by Jeffandy | Day 4 of 100 Days to Hireable")

st.markdown("---")

# ============================================
# YOUTUBE
# ============================================

# Embedded YouTube video
st.markdown("## 🎥 Day 4 / 100 Days Coding")
st.markdown("""
<iframe width="560" height="315"
src="https://www.youtube.com/embed/v3hlczbSRIg?si=tk08BJyYklaQDFYR" 
title="YouTube video player" frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
""", unsafe_allow_html=True)

st.markdown("---")


# ============================================
# CODE VIEWER SECTION
# ============================================

st.markdown("## 👨‍💻 Original Python Code")
st.markdown("**Day 4 Project:** Showcasing the random module, lists and string manipulation to create a korean rock paper scissors game")

# Fake code editor with syntax highlighting
st.markdown('<div class="code-header">📄 Korean-RPS-game.py</div>', unsafe_allow_html=True)

# Split code into lines for line numbers
code_lines = ORIGINAL_CODE.split('\n')

code_html = '<div class="code-editor" style="white-space: pre; font-family: \'Courier New\', monospace;">'
for i, line in enumerate(code_lines, 1):
    # Escape HTML characters first
    highlighted_line = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    
    # Python keywords (blue)
    for keyword in ['def ', 'while ', 'if ', 'elif ', 'else:', 'break', 'return', 'True:', 'False']:
        highlighted_line = highlighted_line.replace(keyword, f'<span class="keyword">{keyword}</span>')
    
    # Function calls (yellow)
    highlighted_line = highlighted_line.replace('print(', '<span class="function">print</span>(')
    highlighted_line = highlighted_line.replace('input(', '<span class="function">input</span>(')
    highlighted_line = highlighted_line.replace('main_game()', '<span class="function">main_game</span>()')
    highlighted_line = highlighted_line.replace('.lower()', '.<span class="function">lower</span>()')
    
    # Strings - handle triple quotes and regular strings
    import re
    # Triple quoted strings
    highlighted_line = re.sub(r"('''.*?''')", r'<span class="string">\1</span>', highlighted_line, flags=re.DOTALL)
    highlighted_line = re.sub(r'(""".*?""")', r'<span class="string">\1</span>', highlighted_line, flags=re.DOTALL)
    # Regular strings
    highlighted_line = re.sub(r'(".*?")', r'<span class="string">\1</span>', highlighted_line)
    
    # Comments (green)
    if '#' in highlighted_line and '<span' not in highlighted_line.split('#')[1] if len(highlighted_line.split('#')) > 1 else False:
        parts = highlighted_line.split('#', 1)
        highlighted_line = parts[0] + '<span class="comment"># ' + parts[1] + '</span>'
    
    # Format line with proper number alignment
    code_html += f'<div style="display: flex;"><span class="line-number">{i:>3}</span><span>{highlighted_line}</span></div>'

code_html += '</div>'
st.markdown(code_html, unsafe_allow_html=True)

# Project Info
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🎯 Learning Goals")
    st.markdown("""
    - random module utilization
    - list iteration
    - if-else logic
    - String manipulation
    """)

with col2:
    st.markdown("### 🛠️ Technologies")
    st.markdown("""
    - Python
    - Streamlit
    - Custom CSS
    - HTML
    - pycharm
    - VScode
    - github
    """)

with col3:
    st.markdown("### 📅 Project Details")
    st.markdown("""
    - **Day:** 4 of 100
    - **Date:** December 2025
    - **Focus:** randomization
    - **Type:** Interactive Game
    """)




