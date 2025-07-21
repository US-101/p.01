import streamlit as st

dog_list = ["汪太郎", "莉莉", "狗"]

# 初始化狀態
if "passed" not in st.session_state:
    st.session_state.passed = False
if "toy_result_shown" not in st.session_state:
    st.session_state.toy_result_shown = False

st.markdown("## 歡迎")
st.markdown("我是這裡的飼養員")

name = st.text_input("請問你叫什麼呢？")

# 按下確認後，儲存通過狀態
if st.button("確認"):
    if name:
        if name in dog_list:
            st.success("汪汪你好")
            st.session_state.passed = True
        else:
            st.warning("這裡只歡迎狗")
    else:
        st.info("請先輸入名字再按確認喔")

# 如果通過第一關，顯示第二題
if st.session_state.passed:
    toy = st.radio("你最喜歡哪種玩具？", ["球", "骨頭", "狗男友"], key="toy")

    if st.button("回答"):
        if toy == "狗男友":
            st.success("我相信你是一隻狗 ❤️🐶")
        else:
            st.warning("你不是真的狗吧？🐾")
        st.session_state.toy_result_shown = True

    # 如果之前已經回答過一次（點過按鈕），則持續顯示結果
    elif st.session_state.toy_result_shown:
        if toy == "狗男友":
            st.success("我相信你是一隻狗 ❤️🐶")
        else:
            st.warning("你不是真的狗吧？🐾")
