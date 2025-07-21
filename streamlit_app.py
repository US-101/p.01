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

            # ✅ 第二題
            toy = st.radio("你最喜歡哪種玩具？", ["球", "骨頭", "狗男友"])
            if toy:
                if toy == "狗男友":
                    st.success("我相信你是一隻狗 ❤️🐶")
                else:
                    st.warning("你不是真的狗吧？🐾")

        else:
            st.warning("這裡只歡迎狗")
    else:
        st.info("請先輸入名字再按確認喔")
