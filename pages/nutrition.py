import streamlit as st
from PIL import Image
from streamlit_TTS import text_to_speech

st.title("🥗 식사 영양성분 분석")

# 사용자 건강 정보 입력
st.sidebar.header("개인 건강 정보")
age = st.sidebar.number_input("나이", 20, 100, 30)
health_condition = st.sidebar.selectbox(
    "건강 상태",
    ["정상", "당뇨병", "고혈압", "심장질환", "신장질환"]
)
activity_level = st.sidebar.selectbox(
    "활동량",
    ["낮음", "보통", "높음"]
)

# 이미지 업로드
uploaded_file = st.file_uploader("식단 사진을 업로드해주세요", type=['jpg', 'jpeg', 'png'])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="업로드된 음식", use_column_width=True)

    if st.button("영양성분 분석하기"):
        with st.spinner("AI가 분석 중입니다..."):
            # AI 분석 결과 예시
            result_txt = "칼로리: 350kcal. 탄수화물: 45g. 단백질: 25g. 지방: 12g."
            if health_condition == "당뇨병":
                tip_txt = "주의: 당뇨 환자에게는 탄수화물 함량이 높을 수 있습니다. 혈당 관리를 위해 채소를 더 드세요."
            else:
                tip_txt = "균형잡힌 영양소 구성입니다."

            st.success("분석 완료!")
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("📊 영양성분")
                st.metric("칼로리", "350 kcal")
                st.metric("탄수화물", "45g")
                st.metric("단백질", "25g")
                st.metric("지방", "12g")
            with col2:
                st.subheader("💡 개인 맞춤 조언")
                if health_condition == "당뇨병":
                    st.warning("⚠️ " + tip_txt)
                else:
                    st.success("✅ " + tip_txt)
            # TTS 음성 안내
            st.audio(text_to_speech(result_txt + " " + tip_txt, language='ko')["bytes"], format="audio/wav")