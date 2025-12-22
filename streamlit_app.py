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
