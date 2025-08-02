import streamlit as st
from transformers import pipeline
import pykakasi

@st.cache_resource
def load_tools():
    translator = pipeline("translation_zh_to_ja", model="Helsinki-NLP/opus-mt-zh-ja")
    kakasi = pykakasi.kakasi()
    kakasi.setMode("J", "H")  # 漢字轉平假名
    conv = kakasi.getConverter()
    return translator, conv

translator, conv = load_tools()

st.title("中文 ➜ 日文翻譯（附平假名）")

input_text = st.text_area("請輸入中文：")

if input_text:
    translation = translator(input_text)[0]['translation_text']
    furigana = conv.do(translation)
    st.write("### 翻譯結果（日文）")
    st.success(translation)
    st.write("### 平假名版本")
    st.info(furigana)
