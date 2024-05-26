import streamlit as st
import google.generativeai as genai
import pandas as pd

# Debug statement to print secrets (comment out in production)
st.write(st.secrets)

# Configure the Google Gemini API with your API key
genai.configure(api_key=st.secrets["API_key"]["api_key"])

def generate_song_data(phrase):
    prompt = f"Find song titles, artists, and release dates for songs that contain the phrase '{phrase}'. List them in the format: Title by Artist (Released on Date)."
    response = genai.generate(prompt)
    
    if response and response['choices']:
        return response['choices'][0]['text'].strip()
    else:
        return "No songs found."

def generate_lyrics(song_title):
    prompt = f"Generate the lyrics for the song titled '{song_title}'."
    response = genai.generate(prompt)
    
    if response and response['choices']:
        return response['choices'][0]['text'].strip()
    else:
        return "Lyrics not found."

def main():
    st.title("Lyrics×Hunter")
    st.subheader("Familiar lyrics but struggling to find the song title? This app is a guardian angel! Just enter a phrase or word and we'll generate some lyrics.")
    st.text("Asie Jay E. Fondales\n"
            "BSCS 3-B AI\n"
            "College of Information Communication and Technology\n"
            "West Visayas State University")

    phrase = st.text_input("Enter a phrase or word:")

    if st.button("Find Songs"):
        if phrase:
            st.write("Searching for songs...")
            song_data = generate_song_data(phrase)

            if song_data and song_data != "No songs found.":
                songs = song_data.split("\n")
                st.write("Found the following songs:")
                selected_song = st.selectbox("Choose a song to view the lyrics:", songs)

                if selected_song:
                    lyrics = generate_lyrics(selected_song.split(" by ")[0])
                    st.write("Lyrics:")
                    st.write(lyrics)
            else:
                st.write("No songs found with the given phrase or word.")
        else:
            st.write("Please enter a phrase or a word.")

if __name__ == "__main__":
    main()
