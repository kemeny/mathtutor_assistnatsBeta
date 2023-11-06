import streamlit as st
import openai
import os
import time
#from dotenv import load_dotenv

# Initialize the environment variables and OpenAI API client
#load_dotenv()
#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = st.secrets['openai']["OPENAI_API_KEY"]

# Set up the Streamlit UI with a chat-style interface
st.title('Math Tutor Assistant')

# Ensure the API key is set
if not openai.api_key:
    st.error("OpenAI API key not found. Please check your .env file.")
else:
    # Initialize chat history if not already present
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    user_query = st.chat_input("Enter your math question:", key="chat")
    if user_query:
        # Add user message to chat history and display it
        st.session_state.messages.append({"role": "user", "content": user_query})
        with st.chat_message("user"):
            st.markdown(user_query)

        # Interact with OpenAI API
        try:
            # Create the assistant with the Code Interpreter tool enabled
            assistant = openai.Client().beta.assistants.create(
                name="Math Tutor",
                instructions="Answer math questions.",
                tools=[{"type": "code_interpreter"}],
                model="gpt-4-1106-preview"
            )

            # Create a thread
            thread = openai.Client().beta.threads.create(
                messages=[{"role": "user", "content": user_query}]
            )

            # Create a run
            run = openai.Client().beta.threads.runs.create(
                thread_id=thread.id,
                assistant_id=assistant.id
            )

            # Polling for run completion
            while run.status not in ['completed', 'failed', 'cancelled']:
                time.sleep(1)
                run = openai.Client().beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)

            # Retrieve and display messages if run is completed
            if run.status == 'completed':
                messages_response = openai.Client().beta.threads.messages.list(thread_id=thread.id)
                messages = messages_response.data
                assistant_messages = [m for m in messages if m.role == 'assistant']
                if assistant_messages:
                    latest_message = assistant_messages[-1].content
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": latest_message
                    })
                    with st.chat_message("assistant"):
                        st.markdown(latest_message)

        except openai.OpenAIError as e:
            st.error(f"An error occurred with the OpenAI service: {e}")
