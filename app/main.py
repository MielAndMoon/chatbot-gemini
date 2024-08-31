import streamlit as st
import google.generativeai as genai
from streamlit_mic_recorder import speech_to_text

genai.configure(api_key=st.secrets["API_KEY"])

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

if "gemini_model" not in st.session_state:
    st.session_state["gemini_model"] = "gemini-1.5-flash"

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["parts"])

model = genai.GenerativeModel(st.session_state["gemini_model"])

with c3:
    message_received = speech_to_text(language='es', use_container_width=True,
                                      just_once=True, key='STT', start_prompt="Hablar", stop_prompt="Finalizar")

if prompt := st.chat_input("Hazme una pregunta") or message_received:
    if st.session_state.text_received and not (prompt):
        st.session_state.text_received.append(message_received)
        prompt = st.session_state.text_received.pop(0)

    st.session_state.messages.append({"role": "user", "parts": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        chat = model.start_chat(
            history=[
                {"role": m["role"], "parts": m["parts"]}
                for m in st.session_state.messages
            ]
        )

        stream = chat.send_message(
            prompt,
            generation_config=genai.types.GenerationConfig(
                max_output_tokens=40
            ),
        )
        text = stream.to_dict()["candidates"][0]["content"]["parts"][0]["text"]
        st.write(text)

    st.session_state.messages.append(
        {"role": "model", "parts": text})
