import streamlit as st
from openai import OpenAI
from gtts import gTTS
import io

st.title("🚑 응급상황 대처 · 자가진단 챗봇")
st.info("증상이나 상태를 입력하면 AI가 응급대처 및 병원 방문 필요 여부에 대해 안내합니다. 심각한 응급상황일 경우 즉시 119로 연락하세요.")

api_key = st.secrets.get("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

MAX_CHAT_HISTORY = 50  # 너무 길어지는 메시지 context 한계 방지용

def get_message_list(chat_history):
    messages = []
    for role, content in chat_history[-MAX_CHAT_HISTORY:]:
        if role == "user":
            messages.append({"role": "user", "content": content})
        elif role == "assistant":
            messages.append({"role": "assistant", "content": content})
    return messages

def ask_emergency_bot(chat_history, user_msg):
    temp_chat = chat_history + [("user", user_msg)]
    messages = [{
        "role": "system",
        "content": (
            "너는 친절하고 신속한 한국어 응급상황 대처 챗봇이다. "
            "응급의료 및 병원 방문, 자가처치, 119 신고 필요성 등을 간결하고 명확하게 안내해라."
        )
    }]
    messages += get_message_list(temp_chat)
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=400,
        )
        out_msg = response.choices[0].message.content.strip() if hasattr(response.choices[0], "message") else None
        return out_msg
def tts_gtts(text, lang='ko'):
    try:
        tts = gTTS(text=text, lang=lang)
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        return fp.read()

if "emergency_chat" not in st.session_state:
    st.session_state["emergency_chat"] = []

user_input = st.chat_input("현재 증상이나 상황을 입력하세요 (예: 열이 38도, 기침이 심해요 등)")
if user_input:
    with st.spinner("AI 분석 중..."):
        bot_ans = ask_emergency_bot(st.session_state["emergency_chat"], user_input)
        st.session_state["emergency_chat"].append(("user", user_input))
        st.session_state["emergency_chat"].append(("assistant", bot_ans))

for role, msg in st.session_state["emergency_chat"]:
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
