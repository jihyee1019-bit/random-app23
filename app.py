
import random
import streamlit as st

# 웹앱 제목
st.title("🍱 오늘의 점심 메뉴 추천")
st.write("오늘 점심은 무엇을 먹을까요?")
st.write("버튼을 눌러 랜덤으로 메뉴를 추천받아 보세요!")

# 점심 메뉴 리스트
menu_list = [
    "🍚 김치볶음밥",
    "🍜 짜장면",
    "🍲 순두부찌개",
    "🍗 치킨",
    "🍔 햄버거",
    "🍝 파스타",
    "🍣 초밥",
    "🥩 제육볶음",
    "🍛 카레라이스",
    "🌮 떡볶이",
    "🥗 샐러드",
    "🍖 돈가스",
    "🍜 쌀국수",
    "🥘 부대찌개",
    "🍙 김밥"
]

# 메뉴 추천 버튼
if st.button("🎲 오늘의 점심 메뉴 뽑기!"):

    # 랜덤으로 메뉴 선택
    today_menu = random.choice(menu_list)

    # 추천 결과 출력
    st.success("오늘의 추천 메뉴는?")
    st.header(today_menu)

    st.balloons()
