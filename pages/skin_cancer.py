import streamlit as st
from PIL import Image
from streamlit_TTS import text_to_speech

st.title("🔬 피부암 진단 보조 시스템")
st.warning("⚠️ 이 서비스는 진단 보조 도구로, 의료진 상담을 대체할 수 없습니다.")

# 채팅 형태 UI
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "안녕하세요! 피부 사진을 업로드해주시면 AI가 분석해드립니다."}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

uploaded_image = st.file_uploader("피부 사진 업로드", type=['jpg', 'jpeg', 'png'])

if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="업로드된 피부 사진", width=300)

    if st.button("진단 분석 시작"):
        with st.spinner("AI가 피부 상태를 분석하고 있습니다..."):
            # 예시 결과
            benign_prob = 0.75
            malignant_prob = 0.25
            if malignant_prob < 0.5:
                result_msg = "양성일 확률이 75퍼센트, 악성일 확률이 25퍼센트입니다. 현재 결과는 양성에 가깝지만, 정확한 진단을 위해 피부과 전문의 상담을 권장합니다."
            else:
                result_msg = "악성 가능성이 높습니다. 즉시 피부과 전문의 상담이 필요합니다."

            st.session_state.messages.append({"role": "assistant", "content": result_msg})
            # TTS 안내
            st.audio(text_to_speech(result_msg, language='ko')["bytes"], format="audio/wav")
            st.rerun()