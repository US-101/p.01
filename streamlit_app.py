import streamlit as st
from googletrans import Translator
import pykakasi

@st.cache_resource
def load_tools():
    translator = Translator()
    kakasi = pykakasi.kakasi()
    kakasi.setMode("J", "H")  # 將漢字轉平假名
    conv = kakasi.getConverter()
    return translator, conv

translator, conv = load_tools()

st.title("中文 ➜ 日文翻譯（附平假名）")

input_text = st.text_area("請輸入中文：")

if input_text:
    # 翻譯
    result = translator.translate(input_text, src='zh-CN', dest='ja')
    translation = result.text

    # 平假名
    furigana = conv.do(translation)

    st.write("### 翻譯結果（日文）")
    st.success(translation)

    st.write("### 平假名版本")
    st.info(furigana)
