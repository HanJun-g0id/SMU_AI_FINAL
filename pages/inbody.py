import streamlit as st
import pandas as pd
from streamlit_TTS import text_to_speech

st.title("💪 인바디 결과 맞춤 건강관리")

uploaded_pdf = st.file_uploader("인바디 결과 PDF를 업로드해주세요", type=['pdf'])

if uploaded_pdf:
    st.success("인바디 결과가 업로드되었습니다!")
    if st.button("분석 시작"):
        with st.spinner("PDF를 분석하고 있습니다..."):
            # 예시 결과 (실제 분석 텍스트로 교체 가능)
            main_result = "체중 70.5kg, 근육량 30.2kg, 체지방률 18.5퍼센트, BMI 23.1, 기초대사율 1650kcal입니다."
            guide = "근육량이 약간 부족하니 주 3회 근력 운동을 추천합니다. 단백질은 체중 곱하기 1.5g씩 섭취하고, 충분한 수분을 드세요."
            full_txt = main_result + " " + guide

            st.subheader("📋 체성분 분석 결과")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("체중", "70.5kg", "2.3kg")
                st.metric("근육량", "30.2kg", "-0.8kg")
            with col2:
                st.metric("체지방률", "18.5%", "-1.2%")
                st.metric("BMI", "23.1", "0.5")
            with col3:
                st.metric("기초대사율", "1650kcal")
                st.metric("내장지방", "레벨 5")

