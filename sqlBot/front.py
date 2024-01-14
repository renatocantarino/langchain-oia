import chat_db as helper
import streamlit as st


if "history" not in st.session_state:
    st.session_state["history"] = []

st.title("AI Chat")


def send_message():
     if st.session_state.user_input:
        user_message = st.session_state.user_input
        response = helper.handler(user_message)
        st.session_state["history"].append(("Voce", user_message))
        st.session_state["history"].append(("AI", response))
        

user_input = st.text_input(
    "Enter your message:", key="user_input", on_change=send_message
)        


send_button = st.button("Send")

if send_button and st.session_state.user_input:
    send_message()

for idx, (user, message) in enumerate(reversed(st.session_state["history"])):
    if user == "Voce":
        st.text_area(f"Voce: {idx}", message, key=f"msg{idx}u", disabled=True)
    else:
        st.text_area(f"AI: {idx}", message, key=f"msg{idx}b", disabled=True)

st.markdown("---")
