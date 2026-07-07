import pathlib

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="AESTURA · 브랜드 제품 라인업 대시보드",
    page_icon="🧴",
    layout="wide",
)

# Streamlit 기본 여백/패딩을 최소화해서 원본 HTML 디자인이 그대로 보이게 함
st.markdown(
    """
    <style>
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
            max-width: 100%;
        }
        header[data-testid="stHeader"] {
            background: transparent;
        }
        iframe {
            width: 100%;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# 같은 폴더의 index.html 파일을 읽어서 그대로 렌더링
html_path = pathlib.Path(__file__).parent / "index.html"
html_content = html_path.read_text(encoding="utf-8")

components.html(html_content, height=2400, scrolling=True)
