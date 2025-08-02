import streamlit as st
from transformers import pipeline
from pykakasi import kakasi

# 初始化翻譯模型
@st.cache_resource
def load_translator():
    return pipeline("translation", model="staka/fugumt-ja-en", src_lang="zh", tgt_lang="ja")

translator = load_translator()

# 轉換漢字為帶平假名的日文
def add_furigana(japanese_text):
    kakasi_obj = kakasi()
    kakasi_obj.setMode("H", "a")  # 漢字→平假名
    kakasi_obj.setMode("K", "a")  # カタカナ→平假名
    kakasi_obj.setMode("J", "a")  # 漢字→平假名
    kakasi_obj.setMode("r", "Hepburn")
    conv = kakasi_obj.getConverter()

    result = ""
    for word in japanese_text:
        if '\u4e00' <= word <= '\u9fff':  # 如果是漢字
            hira = conv.do(word)
            result += f"{word}({hira})"
        else:
            result += word
    return result

# UI
st.title("🌸 中文 → 日文翻譯器（附平假名）")

user_input = st.text_input("請輸入中文：")

if user_input:
    # 翻譯
    result = translator(user_input)[0]["translation_text"]
    with_furigana = add_furigana(result)

    st.markdown("### 📘 翻譯結果：")
    st.write(result)
    st.markdown("### 🈁 平假名標註：")
    st.write(with_furigana)
