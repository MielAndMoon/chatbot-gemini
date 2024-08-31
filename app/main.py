import streamlit as st

st.set_page_config(
    page_title="Turismo Verde | Chatbot",
    page_icon="four_leaf_clover"
)

c1, c2, c3 = st.columns([5, 2, 2], vertical_alignment='bottom')
c1.title("Turismo Verde")

if "text_received" not in st.session_state:
    st.session_state["text_received"] = []

if "messages" not in st.session_state:
    st.session_state.messages = []
