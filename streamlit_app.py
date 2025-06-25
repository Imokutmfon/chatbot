#Import required libraries
import time
from groq import Groq
import streamlit as st
# Setup Groq client
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
groq_client = Groq(api_key=GROQ_API_KEY)
#Define the system message for the chatbot
system_message = (
    "You are a highly relatable personal productivity coach for teenagers."
    "Your name is Pep (short for Pep Talker)."
    "Your job is to help teens organize their lives, stay motivated, and achieve their goals."
    "Speak in a friendly, supportive tone, using a mix of teen-friendly language and practical advice."
    "Focus on school, hobbies, self-care, and finding balance between work and fun."
    "Be motivational, empathetic, and slightly witty but always positive."
    "Avoid being overly formal; keep your responses very short, fun, actionable, and encouraging."
    "REMEMBER: Always keep your responses short and concise - Less than 100 words."
)
system_prompt = {
    "role": "system",
    "content": system_message
}
#Define the function to get a response from the Groq model
def get_response(chat_history):
    response = groq_client.chat.completions.create(
        model="llama3-70b-8192",
        messages=chat_history,
        max_tokens=200,
        temperature=1.2
    )
    chat_response = response.choices[0].message.content
    for word in chat_response.split():
        yield word + " "
        time.sleep(0.05)
#Define the main function to run the Streamlit app
def main():
    #Title and About section
    st.title("Pep Talker - Your Personal Productivity Coach")
    with st.expander("About Pep Talker"):
        st.write(
            "Pep Talker is your friendly personal productivity coach, here to help you stay organized, motivated, and achieve your goals. "
            "Whether it's schoolwork, hobbies, or self-care, Pep is here to support you with practical advice and a positive attitude."
        )
    #Initialize session state for chat messages
    if "messages" not in st.session_state:
        st.session_state.messages = [system_prompt]
    for message in st.session_state.messages:
        if message != system_prompt:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
    # Chat input and response handling
    if prompt := st.chat_input("Ask Pep for advice!"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        response = get_response(st.session_state.messages)
        with st.chat_message("assistant"):
            chat_response = st.write_stream(response)
        st.session_state.messages.append({"role": "assistant", "content": chat_response})
# Run the main function when the script is executed
if __name__ == "__main__":
    main()