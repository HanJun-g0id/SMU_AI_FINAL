import streamlit as st

st.title("🏥 AI 건강 도움 서비스")
st.markdown("---")

st.markdown("""
### 🌟 서비스 소개
AI 기술을 활용하여 개인 맞춤형 건강 관리를 지원하는 종합 플랫폼입니다.

### 🔧 주요 기능
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    #### 🥗 음식 영양 분석
    - 음식 사진 업로드
    - AI 영양성분 분석
    - 개인 건강상태 맞춤 조언
    - 칼로리 및 영양소 정보
    """)

with col2:
    st.markdown("""
    #### 💪 인바디 결과 분석
    - 인바디 PDF 업로드
    - 체성분 상세 분석
    - 맞춤 운동/식단 추천
    - 건강 목표 설정 가이드
    """)

with col3:
    st.markdown("""
    #### 🔬 피부암 진단 보조
    - 피부 사진 업로드
    - AI 피부암 위험도 분석
    - 진단 보조 및 상담 권유
    - 조기 발견 지원
    """)

col4, col5 = st.columns(2)

with col4:
    st.markdown("""
    #### 🚑 응급상황 대처/자가진단 챗봇
    - 증상에 따른 실시간 응급 대처 및 병원 방문 안내
    - 119 신고 필요성 즉시 제안
    """)

with col5:
    st.markdown("""
    #### 🧘 정신건강/마음챙김 챗봇
    - 스트레스, 우울감 등 대화형 체크 및 위로/응원
    - 마음챙김, 명상, 쉬는 팁 안내
    - TTS로 치유 메시지 제공
    """)

st.markdown("---")
st.info("⚠️ 본 서비스는 의료진 상담을 대체할 수 없으며, 참고용으로만 사용하시기 바랍니다.")