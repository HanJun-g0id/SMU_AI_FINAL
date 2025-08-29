# 🏥 AI 건강 도움 서비스

**AI·ML, Streamlit, OpenAI, gTTS 기반의 개인 맞춤 건강관리 웹앱**

---

## 📋 프로젝트 개요
앱 전체 Home 화면 예시  
![앱 메인 화면](Image/Main.png)
AI 기술을 심플한 UI와 통합하여 개인 건강관리와 의료 정보 접근성을 높인 종합 서비스입니다.  
- **Streamlit** 프레임워크로 개발된 직관적 웹 환경
- *응급상황 대처/자가진단 챗봇* 및 *정신건강/마음챙김 챗봇* 등 다양한 AI 챗봇 서비스  
- OpenAI LLM과 gTTS(TTS)로 시각·청각 정보를 동시에 제공  
- 의료 상담 대체 X, 정보·가이드 제공 목적

---

## 🎯 주요 기능
### 🍽️ 맞춤형 식단 추천
- **사용자 신체 상태 분석:** 신체 상태 입력, 식사별 추천 식단 안내, 개인 건강 조언  
- 영양 분석 메인 화면  
  ![영양 분석 메인](Image/CustomizedMealRecommendation_Main.png)
- 분석 결과 화면  
  ![](Image/CustomizedMealRecommendation_Display.png)

### 💪 인바디 결과 분석
- **인바디 결과 분석:** PDF 업로드, 체성분 분석, 맞춤 운동·식단 추천 
- 인바디 메인 화면  
  ![인바디 메인](Image/Inbody_Main.png)
- 인바디 결과 예시  
  ![인바디 결과](Image/Inbody_display.png)

### 🩺 피부암 진단 보조
- **피부암 진단 보조:** 이미지 업로드, AI 판단·상담 
- 진단 메인 화면  
  ![피부암 진단 메인](Image/SkincancerDiagnosis_main.png)
- 피부 사진 업로드 및 AI 분석  
  ![양성비율이 큰 경우](Image/SkincancerDiagnosis_Display.png)
  ![악성비율이 큰 경우](Image/SkincancerDiagnosis_Display2.png)

### 🚑 응급 상황 챗봇
- **응급 상황 챗봇:** 실시간 증상 입력, 행동 지침/병원 안내 
- 응급 챗봇 메인 화면  
  ![응급 챗봇 메인](Image/EmergencyChatbot_Main.png)
- 챗봇 대화 예시  
  ![응급 챗봇 대화](Image/EmergencyChatbot_Display.png)

### 🧠 정신건강/마음챙김 챗봇
- **정신건강/마음챙김 챗봇:** 고민·스트레스 대화, 위로 메시지, TTS 음성 변환
- 정신건강 챗봇 메인 화면  
  ![정신건강 챗봇 메인](Image/MentalHealthChatbot_Main.png)
- 대화·TTS 결과 예시  
  ![정신건강 챗봇 대화](Image/MentalHealthChatbot_Display.png)

---

## 🛠️ 기술 스택

### 📄 프론트엔드

- **Streamlit**: 빠르고 직관적인 웹 UI 프레임워크
- **Streamlit 멀티 페이지 구조**: 다양한 기능(챗봇, 피부암 진단 등)을 분리된 페이지로 구현
- **Pillow**: 이미지 업로드 및 처리(리사이즈, 변환 등)
- **사용자 Interaction 컴포넌트**: 파일 업로더, 대화 UI, 진행률 바, 상태 표시 등

### ⚙️ 백엔드

- **Python 3.8+**: 전체 앱 및 AI 기능 개발
- **TensorFlow/Keras**: 이미지 진단 모델(h5) 및 AI 챗봇 연동
    - .h5 모델 파일 관리 및 자동 캐싱
- **OpenAI API (GPT-3.5/4)**: 챗봇 자연어 처리
- **NumPy/Pandas**: 데이터 연산, 파이프라인 관리
- **PyPDF2**: 인바디 결과/문서 파싱(기능에 따라)

### 🔈 기타/음성 및 부가 기능

- **gTTS(Google Text-to-Speech)**: AI 답변을 실시간 음성(mp3) 안내로 변환
- **requirements.txt**: 모든 라이브러리 관리 및 환경 통일
- **.streamlit/secrets.toml**: OpenAI 등 민감 정보 보안 관리
- **.gitignore**: 보안 파일, 불필요 파일 깃 추적 방지 (models, secrets, venv 등)

### 🛠️ 데이터 및 모델 관리

- **skin_cancer_models.h5**: 피부암 진단용 CNN/XAI 모델 파일 관리
- **프로젝트 폴더 관리**: /pages, /models, /venv, /app.py, /README.md 등

### 🌐 배포 및 협업

- **GitHub**: 코드 버전관리 및 팀원 협업 (커밋 컨벤션, 브랜치 등)
- **Streamlit Cloud/로컬 실행**: 빠른 배포·테스트 환경
- **README.md/사용자 설명서**: 기능, 사용법, 기술 스택 문서화


---

## 💡 사용 방법

1. 프로젝트 폴더에서 아래 명령어로 필수 패키지를 설치합니다.
- `pip install -r requirements.txt`

2. `.streamlit/secrets.toml` 파일에 본인의 OpenAI API 키를 입력합니다.
- OPENAI_API_KEY = “sk-…”

3. 프로젝트 루트에서 Streamlit 앱을 실행합니다.
- `streamlit run app.py`

4. 웹 브라우저에서 [http://localhost:8501](http://localhost:8501)로 접속하여
챗봇, 피부암 진단 등 다양한 기능을 직접 사용할 수 있습니다.

5. TTS(음성 안내) 기능은 gTTS 기반이며, ffmpeg가 운영체제에 설치되어 있어야 합니다.
- MacOS: `brew install ffmpeg`
- Ubuntu: `sudo apt install ffmpeg`
- Windows: ffmpeg 공식 사이트에서 설치 후 환경변수에 등록

---

## 🧬 모델 설명

이 프로젝트에서 사용된 피부암 진단 모델은 TensorFlow/Keras 기반의 CNN(Convolutional Neural Network) 구조를 활용하여,  
피부 병변 이미지(224x224)로 양성/악성을 분류하는 딥러닝 모델입니다.

- 학습 데이터: 공개 피부암 이미지 데이터셋(Kaggle, ISIC 등)
- 입력: (224, 224, 3) RGB 피부 병변 이미지
- 출력: 클래스별 확률(예: [benign, malignant])
- 저장 포맷: `skin_cancer_models.h5` (Keras h5 파일)
- 사용 목적: 피부 사진 업로드 시, AI가 양성/악성 확률로 예측 결과 안내.  
  주의: 실제 진단·치료 시 반드시 의료 전문가의 판정과 병행해야 함.

모델 상세 구조/성능 등은 코드와 함께 제공된 학습 코드, 평가 결과 참고.

---

## 🚨 주의 사항

- 이 서비스의 모든 안내, 진단 결과, 조언은 참고용 정보이며,
실제 질병 진단·치료는 반드시 **의료 전문가와 상담**해야 합니다.

- **API 키(.streamlit/secrets.toml), 모델 파일(.h5), 환경 설정 등
주요 파일은 깃허브에 업로드하지 마세요!**
- `.gitignore`에 반드시 포함하여 보안 사고와 파일 크기 이슈를 예방하세요.

- TTS 및 챗봇 AI 답변은 자동 생성된 결과이며,
실제 의료 또는 심리 상담과 다를 수 있으므로,
반드시 최종 판단은 전문가에게 문의하시기 바랍니다.

---

## 👨‍💻 개발자 소개

### SMU 소프트웨어학과
- 금한준 (개발총괄, 기획)
- 박세호 (모델개발, 리서치)
- 오형민 (모델개발, 리서치)
- 오현기 (데이터 전처리, 기획)

---
