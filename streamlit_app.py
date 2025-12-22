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

st.title("✌🏾 ✋🏾 ✊🏾 가위 바위 보!")
st.subheader("Rock Paper Scissors - Korean Style")

st.markdown("---")

# Player choice
choice = st.radio(
    "Choose your weapon:",
    options=["S", "P", "R"],
    format_func=lambda x: names[x],
    horizontal=True
)

# Play button
if st.button("Play! 시작!", type="primary"):
    
    cpu = random.choice(["S", "P", "R"])
    
    # Display choices
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
    
    # Determine winner
    if choice == cpu:
        st.warning("## 🤝 It's a DRAW... BOOORING!")
    elif (choice == "S" and cpu == "P") or \
         (choice == "P" and cpu == "R") or \
         (choice == "R" and cpu == "S"):
        st.success("## ★ 당신이 이겼어요! YOU WIN! ★")
        st.balloons()
    else:
        st.error("## 💀 당신이 졌어요... YOU LOSE!")

st.markdown("---")
st.caption("Built by Jeffandy | Day 4 of 100 Days to Hireable")
