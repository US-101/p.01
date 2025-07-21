import streamlit as st

dog_list = ["汪太郎", "莉莉", "狗"]

st.markdown("## 歡迎")
st.markdown("我是這裡的飼養員")

name = st.text_input("請問你叫什麼呢？")
submitted = st.button("確認")

if submitted:
    if name:
        if name in dog_list:
            st.success("汪汪你好")
        else:
            st.warning("這裡只歡迎狗")
    else:
        st.info("請先輸入名字再按確認喔")
