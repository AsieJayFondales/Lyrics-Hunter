# Lyrics×Hunter 🎶🔍

**Lyrics×Hunter** is a Streamlit application designed to help users find song titles, artists, release dates, and lyrics based on a phrase or word they provide. Leveraging the power of Google Gemini's generative AI, the app provides a seamless experience for discovering and viewing song lyrics.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Lyrics×Hunter Features ✨
- **Phrase or Word Search**: Enter any phrase or word to find relevant song titles, artists, and release dates.
- **Lyrics Viewing**: Select a song to view its full lyrics.
- **Generative AI Integration**: Utilizes Google Gemini's generative AI to fetch and display song information and lyrics.

## Installation 🛠️
Kindly follow these steps to set up and run the application locally.

### Prerequisites 📋
- Python 3.9 or higher
- Pip (Python package installer)
- A Google Gemini API key 

### Project Setup ⚙️

1. **Clone the Repository** (if applicable):
    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2. **Create a Virtual Environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  
    venv\Scripts\activate or ./venv/Scripts/activate # On Windows terminal
    ```

3. **Install Required Libraries**:
    ```bash
    pip install -r requirements.txt
    ```

### Configuration 🔧

1. **Set Up Streamlit Secrets**:
    - Create a `secrets.toml` file in the `.streamlit` directory.
    - Add your Google Gemini API key in the `secrets.toml` file as follows:
    ```toml
    [API_key]
    api_key = "your_gemini_api_key_here"
    ```

## Usage 🚀

1. **Run the Streamlit App**:
    ```bash
    streamlit run main.py
    ```

2. **Interact with the App**:
    - Open the app in your web browser.
    - Enter a phrase or word in the input box.
    - Click "Find Songs" to generate and display the list of songs.
    - Select a song from the list to view its full lyrics.

## Contributing 🤝

Contributions are welcome! If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

1. Fork the Repository
2. Create your feature branch (`git checkout -b feature/sheeshfeature`)
3. Commit your changes (`git commit -m 'added some sheeshfeature'`)
4. Push to the branch (`git push origin feature/sheeshfeature`)
5. Open a Pull Request

## HAPPY CODING 
