# Chatbot with Streamlit and Gemini AI

This project is a simple chatbot application built with [Streamlit](https://streamlit.io/) and Gemini AI, designed to interact with users in a conversational manner.

## Table of Contents

- [Features](#features)
- [Screenshots](#screenshots)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)

## Features

- **Conversational Interface**: Engage in natural language conversations with the chatbot.
- **Real-time Responses**: Get instant responses powered by Gemini AI's language model.
- **User-friendly UI**: Intuitive interface built with Streamlit, allowing easy deployment and interaction.
- **Microphone Integration**: Interact with the chatbot using voice.

## Screenshots



## Getting Started

### Prerequisites

Ensure you have the following installed on your system:

- Python 3.8 or higher
- pip (Python package manager)
- A Gemini AI API key

### Installation

1. **Clone the Repository and Switch to `dev` Branch**

First, clone the repository and switch to the `dev` branch:

```bash
git clone https://github.com/MielAndMoon/chatbot-gemini.git
cd chatbot-gemini
git checkout dev
```

2. **Create a Virtual Environment**

Next, create a virtual environment in the project directory:

- On **Windows**:

  ```bash
  python -m venv venv
  ```

- On **macOS/Linux**:

  ```bash
  python3 -m venv venv
  ```

This will create a directory named `venv` containing the virtual environment.

3. **Activate the Virtual Environment**

Activate the virtual environment:

- On **Windows**:

  ```bash
  .\venv\Scripts\activate
  ```

- On **macOS/Linux**:

  ```bash
  source venv/bin/activate
  ```

Once activated, your terminal prompt should change to indicate that you are now working within the virtual environment.

4. **Install Dependencies**

Install the project dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

5. **Set up environment variables:**

   Create a `.streamlit/secrets.toml` file in the root directory of the project and add your Gemini AI API key:

   ```bash
   API_KEY = "your_gemini_api_key_here"
   ```

### Running the Application

1. **Start the Streamlit server:**

   ```bash
   streamlit run app/main.py
   ```

2. **Open your browser:**

   Once the server is running, open your browser and go to `http://localhost:8501` to interact with the chatbot.
