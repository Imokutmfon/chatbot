
# Pep Talker - Your Personal Productivity Coach

A friendly, supportive LLM-powered chatbot designed to help you organize their lives, stay motivated, and achieve their goals. Built with Streamlit and powered by Groq's fast AI inference engine.

## About Pep Talker

Pep Talker is your friendly personal productivity coach, here to help you stay organized, motivated, and achieve your goals. Whether it's schoolwork, hobbies, or self-care, Pep is here to support you with practical advice and a positive attitude.

## Features

- **Friendly interface**: Clean, easy-to-use chat interface built with Streamlit
- **Contextual conversations**: Maintains chat history for coherent, ongoing discussions
- **Streaming responses**: ChatGPT-style streaming text for better user experience
- **Motivational coaching**: Focuses on school, hobbies, self-care, and work-life balance
- **Fast responses**: Powered by Groq's high-speed AI inference engine
- **Secure API handling**: API keys stored securely using Streamlit secrets

## Quick Start

### Prerequisites

- Python 3.7+
- A free Groq API key from [Groq Cloud](https://console.groq.com/)
- Git (for deployment)

### [Access the chatbot](https://peptalkbymomo.streamlit.app)

## Project Structure

```
peptalk-chatbot/
│
├── .streamlit/
│   └── secrets.toml          # API key storage (not tracked by git)
├── .gitignore               # Git ignore file
├── requirements.txt         # Python dependencies
├── streamlit_app.py        # Main application file
└── README.md               # This file
```

## Technical Details

### Dependencies

- `streamlit` - Web app framework for the user interface
- `groq` - Groq API client for LLM interactions

### Model Configuration

- **Model**: Llama 3-70B-8192
- **Max tokens**: 200 (configurable)
- **Temperature**: 1.2 (creative responses)
- **Streaming**: Word-by-word response streaming

### Key Components

1. **LLM Wrapper** (`get_response`): Handles API calls to Groq and implements streaming
2. **Session State Management**: Maintains conversation history for context
3. **System Prompt**: Defines Pep's personality and behavior guidelines
4. **Streamlit Interface**: Provides the chat UI and user interactions

## Usage Tips

- Ask Pep about study strategies, time management, or motivation
- Share your goals and challenges for personalized advice
- Use it for daily check-ins and accountability
- Ask for help with organizing schoolwork or personal projects


## License

This project is open source and available under the [MIT License](LICENSE).


## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [Groq](https://groq.com/) AI inference
- Uses Meta's Llama 3 model
- Inspired by the need for teen-friendly productivity coaching

---

**Ready to get organized and motivated? Start chatting with Pep today!**
