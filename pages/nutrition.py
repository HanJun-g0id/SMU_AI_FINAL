import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="맞춤형 식단 추천", page_icon="🥗")

st.title("🥗 맞춤형 식단 추천 서비스")
st.markdown(
    """
    사용자의 나이, 건강 상태, 활동량 정보를 바탕으로  
    AI가 최적의 맞춤 식단을 추천해드립니다.  
    건강한 식습관을 시작해 보세요!  
    """
)

# 사용자 건강 정보 입력 섹션 박스로 구분
with st.form("user_info_form"):
    st.header("개인 건강 정보 입력")
    age = st.number_input("나이", min_value=10, max_value=100, value=30, help="10세 이상 입력하세요")
    health_condition = st.selectbox(
        "건강 상태",
        options=["정상", "당뇨병", "고혈압", "심장질환", "신장질환"],
        help="본인 건강 상태에 가장 가까운 항목 선택"
    )
    activity_level = st.selectbox(
        "활동량",
        options=["낮음", "보통", "높음"],
        help="현재 신체 활동량을 선택하세요"
    )
    submit = st.form_submit_button("식단 추천 받기")

def generate_diet_plan(age, health_condition, activity_level):
    prompt = (
        f"사용자 나이: {age}세, 건강 상태: '{health_condition}', 활동량: '{activity_level}'.\n"
        "아래 형식에 맞춰 맞춤형 식단을 작성하세요.\n\n"
        "🍽️ 맞춤 식단 추천\n"
        "- 아침: \n"
        "- 점심: \n"
        "- 저녁: \n"
        "- 간식: \n\n"
        "✅ 영양 균형과 건강 상태에 맞는 조언도 포함해 주세요."
    )
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()

if submit:
    with st.spinner("AI가 맞춤 식단을 생성 중입니다..."):
        diet_plan = generate_diet_plan(age, health_condition, activity_level)
    st.success("✅ 맞춤 식단이 준비되었습니다!")
    st.markdown("### 🍽️ 맞춤 식단 추천")
    st.markdown(diet_plan)

    # 선택적으로 추가 정보 혹은 다음 단계 안내
    st.info("궁금하신 점은 언제든 질문해주세요!")
