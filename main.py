import streamlit as st
import google.generativeai as genai

# Configure the Google Gemini API with your API key
genai.configure(api_key="AIzaSyC32Dv0Ph-6778qF2dN7h6HqCDzfHr-e_c")

def generate_response(prompt):
    # Function to generate response from the API
    response = genai.chat(messages=[{"content": prompt}])
    if hasattr(response, 'last'):
        return response.last.strip()
    return "Error: Unable to retrieve content from response."

def fetch_response(prompt, session_key):
    try:
        response = generate_response(prompt)
        st.session_state[session_key] = response
    except Exception as e:
        st.session_state[session_key] = f"Error: {str(e)}"

def main():
    # Apply custom CSS for cursor change and background styling
    st.markdown(
        """
        <style>

        .stSelectbox div[data-baseweb="select"] {
            cursor: pointer;
        }
        .loading-spinner {
            border: 4px solid #f3f3f3;
            border-radius: 50%;
            border-top: 4px solid #3498db;
            width: 20px;
            height: 20px;
            -webkit-animation: spin 2s linear infinite;
            animation: spin 2s linear infinite;
            margin-left: 5px;
        }
        @-webkit-keyframes spin {
            0% { -webkit-transform: rotate(0deg); }
            100% { -webkit-transform: rotate(360deg); }
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("🎼 Lyrics×Hunter 🔍")
    st.subheader("Familiar lyrics but struggling to find the song title? 🧐This app is your guardian angel! 😉 Just enter a phrase or word and we'll generate some lyrics.")
    st.text("Asie Jay E. Fondales\n"
            "BSCS 3-B AI\n"
            "College of ICT\n"
            "West Visayas State University")

    phrase = st.text_input("Enter a phrase or word of the song:")

    if st.button("Find Songs"):
        if phrase:
            st.write("🔍 Searching for songs...")
            session_key = "song_data"
            fetch_response(f"Find song titles, artists, and release dates for songs that contain the phrase '{phrase}'. List them in the format: Title by Artist (Released on Date).", session_key)

    if "song_data" in st.session_state:
        song_data = st.session_state["song_data"]
        if "Error" not in song_data:
            songs = song_data.split("\n")
            st.write("🎶 Found the following songs:")
            selected_song = st.selectbox("Choose a song to view the lyrics:", songs, key="song_select")

            if selected_song:
                

                # Set a flag to indicate that lyrics are being loaded
                if "loading_lyrics" not in st.session_state:
                    st.session_state["loading_lyrics"] = True

                if st.session_state["loading_lyrics"]:
                    st.markdown('<div class="loading-spinner"></div> Loading lyrics...', unsafe_allow_html=True)

                session_key = "lyrics_data"
                song_title = selected_song.split(' by ')[0]
                fetch_response(f"Generate the exact lyrics for the song titled '{song_title}'.", session_key)

                # Check if lyrics are loaded
                if "lyrics_data" in st.session_state:
                    st.write(f"🎵 Selected Song: {selected_song}")
                    lyrics = st.session_state["lyrics_data"]
                    st.session_state["loading_lyrics"] = False
                    st.write("📜 Lyrics:")
                    st.write(lyrics)
                else:
                    st.write("❌ Lyrics not found.")
        else:
            st.write("❌ Browse the songs you want to find lyrics for.")

if __name__ == "__main__":
    main()
