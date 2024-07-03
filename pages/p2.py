import streamlit as st

with st.form(key="names"):   
    name = st.text_input("name")
    name2 = st.text_input("name2")
    
    agecate = st.selectbox(
        "ages",
        ("10s", "20s", "30s")
    )
    
    weapons = st.multiselect(
        "wep",
        ("シューター", "チャージャー", "ローラー", "ワイパー")
        )

    submitbtn = st.form_submit_button("送信")
    if submitbtn:
        st.text(f"ようこそ{name}、{name2}さん！")
        st.text(f"あなたは{agecate}です")