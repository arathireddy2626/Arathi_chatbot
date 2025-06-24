import openai
import streamlit as st


# Show title and description.
st.title("💬 Chatbot")
st.write("Welcome to Arathi chat")
openai.api_key=st.secrets["OPENAI_API_KEY"]
if "openai_model"not in st.session_state:
    st.session_state["openai_model"]="gpt-3.5-turbo"

# Ask user for their OpenAI API key via `st.text_input`.
# Alternatively, you can store the API key in `./.streamlit/secrets.toml` and access it
# via `st.secrets`, see https://docs.streamlit.io/develop/concepts/connections/secrets-management

if "messages" not in st.session_state:
    st.session_state.messages = []

    # Display the existing chat messages via `st.chat_message`.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

    # Create a chat input field to allow the user to enter a message. This will display
    # automatically at the bottom of the page.
prompt := st.chat_input("What is up?"):
if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)

        # Store and display the current prompt.
    st.session_state.messages.append({"role": "user", "content": prompt})
   
    with st.chat_message("assistant"):
        message_placeholder=st.empty()
        full_response=""
        for response in openai.chatcompletion.create(model=st.session_state["openai_model"],messages=[{"role":m["role"],"content":m["content"]}for m in st.session_state.messages],stream=True,
        st.markdown(response)
    st.session_state.messages.append({"role":"assistant","content":response})
        # Generate a response using the OpenAI API.
        stream = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ):
            full_response+=response.choices[0].delta.get("content","")
            message_placeholder.markdown(full_response+ "|")
        message_placeholder.markdown(full_response)

        # Stream the response to the chat using `st.write_stream`, then store it in 
        # session state.
        with st.chat_message("assistant"):
            response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": full_response})
