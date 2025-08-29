import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="AI 건강 도움 서비스",
    page_icon="🏥",
    layout="wide"
)

# 각 페이지 정의
page_main = st.Page("pages/main.py", title="홈", icon="🏠")
page_nutrition = st.Page("pages/nutrition.py", title="맞춤형 식단 추천", icon="🥗")
page_inbody = st.Page("pages/inbody.py", title="인바디 분석", icon="💪")
page_skin = st.Page("pages/skin_cancer.py", title="피부암 진단", icon="🔬")
page_emergency = st.Page("pages/emergency_bot.py", title="응급상황 챗봇", icon="🚑")
page_mental = st.Page("pages/mental_health_bot.py", title="마음챙김 챗봇", icon="🧘")

# 네비게이션 구성
pg = st.navigation(
    [
        page_main,
        page_nutrition,
        page_inbody,
        page_skin,
        page_emergency,
        page_mental
    ],
    position="sidebar",
    expanded=True
)
pg.run()
