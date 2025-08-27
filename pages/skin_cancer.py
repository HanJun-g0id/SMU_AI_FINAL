import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
from gtts import gTTS
import io
import time

st.title("🔬 피부암 진단 보조 시스템")
st.warning("⚠️ 이 서비스는 진단 보조 도구로, 의료진 상담을 대체할 수 없습니다.")

# h5 모델 로딩 (최초 한 번만)
@st.cache_resource
def load_model():
    return tf.keras.models.load_model('skin_cancer_models.h5')


model = load_model()


def preprocess_image(img):
    img = img.resize((224, 224))
    img_array = np.array(img)
    if img_array.shape[-1] == 4:
        img_array = img_array[..., :3]
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array


def tts_gtts(text, lang='ko'):
    try:
        tts = gTTS(text=text, lang=lang)
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        return fp.read()
    except Exception as e:
        st.warning(f"TTS 변환 오류: {str(e)}")
        return None


# 채팅 형식 UI
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
        progress_bar = st.progress(0, text="진단 초기화 중...")
        with st.spinner("AI가 피부 상태를 분석하고 있습니다.."):
            try:
                progress_bar.progress(10, text="이미지 전처리 중...")
                time.sleep(0.5)
                img_array = preprocess_image(image)

                progress_bar.progress(30, text="모델 추론 중...")
                time.sleep(0.5)
                prediction = model.predict(img_array)[0]

                progress_bar.progress(80, text="결과 해석 중..")
                time.sleep(0.3)
                if len(prediction) == 2:
                    benign_prob = float(prediction[0])
                    malignant_prob = float(prediction[1])
                else:
                    malignant_prob = float(prediction)
                    benign_prob = 1.0 - malignant_prob

                benign_pct = int(benign_prob * 100)
                malignant_pct = int(malignant_prob * 100)
                if malignant_prob < 0.5:
                    result_msg = f"양성일 확률이 {benign_pct}%, 악성일 확률이 {malignant_pct}%입니다. 현재 결과는 양성에 가깝지만, 정확한 진단을 위해 피부과 전문의 상담을 권장합니다."
                else:
                    result_msg = f"악성 가능성이 {malignant_pct}%로 높습니다. 즉시 피부과 전문의 상담이 필요합니다."

                progress_bar.progress(95, text="음성 안내 생성 중...")
                time.sleep(0.8)

            except Exception as e:
                result_msg = f"이미지 분석 중 오류 발생: {str(e)}. 올바른 피부 사진을 올려주세요."

            st.session_state.messages.append({"role": "assistant", "content": result_msg})

            audio_bytes = tts_gtts(result_msg, lang='ko')
            if audio_bytes:
                st.audio(audio_bytes, format="audio/mp3")

            progress_bar.progress(100, text="진단 완료!")
            time.sleep(0.5)
            progress_bar.empty()

            st.rerun()
