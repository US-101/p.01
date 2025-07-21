import streamlit as st

dog_list = ["汪太郎", "莉莉", "狗"]

# 初始化題目階段
if "stage" not in st.session_state:
    st.session_state.stage = 1

st.markdown("## 狗狗入會測驗 🐾")

# 第一題
if st.session_state.stage == 1:
    name = st.text_input("請問你叫什麼呢？", key="q1")
    if st.button("確認"):
        if name in dog_list:
            st.session_state.stage = 2
        elif name:
            st.error("這裡只歡迎狗")
        else:
            st.warning("請輸入名字")

# 第二題
elif st.session_state.stage == 2:
    toy = st.radio("你最喜歡哪種玩具？", ["球", "骨頭", "狗男友"], key="q2")
    if st.button("回答"):
        st.session_state.toy = toy
        st.session_state.stage = 3

# 第三題：結果
elif st.session_state.stage == 3:
    toy = st.session_state.get("toy")
    if toy == "狗男友":
        st.success("我相信你是一隻狗 ❤️🐶")
    else:
        st.warning("你不是真的狗吧？🐾")

    if st.button("重新開始"):
        st.session_state.clear()  # 清空所有記憶
        st.experimental_rerun()   # 🔄 重新跑整個 app
