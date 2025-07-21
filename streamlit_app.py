import streamlit as st

name_list = ["小猴", "太郎", "汪太郎"]

st.write("歡迎")

for name in name_list:
    st.write(name + "說你好")

name = st.text_input("請問你叫什麼呢？")
if name:
    if name == "汪太郎":
        st.success("汪汪你好")
    else:
        st.warning("這裡只歡迎狗")
