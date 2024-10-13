import streamlit as st
import pandas as pd

st.title("Football Scouting Dashboard")

# 선수 이름 입력 받기
player_name = st.text_input("Enter player's name", "Lionel Messi")

# 기본적인 예시 데이터 (추후에 크롤링 데이터로 대체 가능)
data = {
    "Stat": ["Goals", "Assists", "Matches Played"],
    "Value": [30, 10, 50]
}

# 데이터프레임 표시
df = pd.DataFrame(data)
st.write(f"Stats for {player_name}")
st.dataframe(df)
