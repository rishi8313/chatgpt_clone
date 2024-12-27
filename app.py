import streamlit as st

# st.experimental_set_page_config(page_title="ChatGPT Clone", layout="wide")

# Add custom CSS to style the buttons with the same background color
st.markdown("""
    <style>
    .chat-container {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 10px;
        margin: 5px 0;
        background-color: #f0f0f0;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .chat-container:hover {
        background-color: #e0e0e0;
    }
    .chat-container:active {
        background-color: #d0d0d0;
    }
    .stTextInput > label {
        display: none;
    }
    </style>
""", unsafe_allow_html=True)

# ...existing code...

def main():
    
    if 'chats' not in st.session_state:
        st.session_state['chats'] = {}
        st.session_state['current_chat'] = None

    with st.sidebar.container():
        col1, col2 = st.columns([0.8, 0.2])
        with col2:
            if st.button("➕"):
                new_chat_id = len(st.session_state['chats']) + 1
                chat_key = f"Chat {new_chat_id}"
                st.session_state['chats'][chat_key] = []
                st.session_state['current_chat'] = chat_key
                st.rerun()
        with col1:
            search_query = st.text_input("", placeholder="🔍")
    
    if search_query:
        search_results = [chat for chat in st.session_state['chats'].keys() if search_query.lower() in chat.lower()]
    else:
        search_results = list(st.session_state['chats'].keys())

    for chat in search_results:
        with st.sidebar.container():
            col1, col2 = st.columns([0.8, 0.2])
            with col1:
                if st.button(chat, key=f"select_{chat}", use_container_width=True):
                    st.session_state['current_chat'] = chat
            with col2:
                if st.button("X", key=f"remove_{chat}"):
                    del st.session_state['chats'][chat]
                    st.session_state['current_chat'] = None
                    st.rerun()
                    
    st.markdown("""
        <style>
        .stContainer {
            background-color: white;
        }
        </style>
    """, unsafe_allow_html=True)
    
    if st.session_state['current_chat']:
        chat_history = st.session_state['chats'][st.session_state['current_chat']]
        for message in chat_history:
            if message.startswith("You:"):
                st.chat_message("user").write(message[5:])
            else:
                st.chat_message("assistant").write(message[5:])

        # Input for new message
        user_input = st.chat_input("You: ")
        if user_input:
            chat_history.append(f"You: {user_input}")
            # Here you would add the logic to get the response from the model
            response = "This is a placeholder response."
            chat_history.append(f"Bot: {response}")
            st.session_state['chats'][st.session_state['current_chat']] = chat_history
            st.rerun()

if __name__ == "__main__":
    main()
