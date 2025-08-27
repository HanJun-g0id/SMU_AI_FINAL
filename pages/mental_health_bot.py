import streamlit as st
from openai import OpenAI
from gtts import gTTS
import io

st.title("🧘 정신건강 · 마음챙김 챗봇")
st.info("스트레스, 우울, 불안 등 상태를 자유롭게 입력해주면 AI가 위로와 조언, 간단한 명상·이완법·응원 메시지를 전달해주고, 음성으로 안내해줍니다.")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def ask_mental_bot(user_msg):
    prompt = (
        "사용자: " + user_msg +
        "\n마음챙김 상담사 챗봇: 정신건강 전문 상담사처럼 위로와 공감, 실질적 마음챙김 팁(CBT, 명상법, 쉬운 생활조언 등)을 한국어로 아주 따뜻하게 해줘. 마지막엔 응원 메시지도 함께."
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400,
    )
    # 에러 처리: 응답이 없거나 content가 None일 때
    if not response or not hasattr(response, "choices") or not response.choices:
        return "AI로부터 응답을 받지 못했습니다. 다시 시도해 주세요."
    msg = response.choices[0].message.content
    if not msg:
        return "챗봇이 답변을 하지 못했습니다. 입력을 다시 해주세요."
    return msg.strip()

def tts_gtts(text, lang='ko'):
    try:
        tts = gTTS(text=text, lang=lang)
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        return fp.read()
    except Exception as e:
        st.warning(f"gTTS 변환 오류: {str(e)}")
        return None

if "mental_chat" not in st.session_state:
    st.session_state["mental_chat"] = []

user_input = st.chat_input("지금 마음 상태, 고민, 질문을 자유롭게 입력하세요")
if user_input:
    with st.spinner("AI 상담 중..."):
        bot_ans = ask_mental_bot(user_input)
        st.session_state["mental_chat"].append(("user", user_input))
        st.session_state["mental_chat"].append(("assistant", bot_ans))

for role, msg in st.session_state["mental_chat"]:
    with st.chat_message(role):
        st.write(msg)
        if role == "assistant":
            try:
                if not msg or not isinstance(msg, str) or len(msg.strip()) < 2:
                    st.warning("TTS를 들려줄 내용이 없습니다.")
                else:
                    audio_bytes = tts_gtts(msg, lang='ko')
                    if not audio_bytes:
                        st.warning("TTS 변환에 실패했습니다.")
                    else:
                        st.audio(audio_bytes, format="audio/mp3")
            except Exception as e:
                st.warning(f"TTS 오류: {str(e)}")
