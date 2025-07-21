import streamlit as st

dog_list = ["汪太郎", "莉莉", "狗"]

st.write("歡迎")
st.write("我是這裡的飼養員")
name = st.text_input("請問你叫什麼呢？")
if name:
    if name in dog_list:
    st.success("汪汪你好")
    else:
    st.warning("這裡只歡迎狗")
