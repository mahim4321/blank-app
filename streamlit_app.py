import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st
from streamlit_mic_recorder import speech_to_text
from gtts import gTTS
import os

st.title("🎙️ আমার ভয়েস অ্যাসিস্ট্যান্ট")

# ইউজারের কথা শোনার জন্য বাটন
text_input = speech_to_text(
    language='bn', 
    start_prompt="কথা বলতে এখানে চাপ দিন", 
    stop_prompt="থামুন", 
    just_once=True, 
    key='STT'
)

# ইউজার কথা বললে অ্যাপ উত্তর দেবে
if text_input:
    st.write(f"আপনি বলেছেন: {text_input}")
    
    # অ্যাপ যা বলবে (এটি আপনি আপনার মতো পরিবর্তন করতে পারেন)
    reply_text = f"আপনি বললেন {text_input}, আমি আপনাকে কিভাবে সাহায্য করতে পারি?"
    
    # টেক্সট থেকে অডিও তৈরি
    tts = gTTS(text=reply_text, lang='bn')
    tts.save("response.mp3")
    
    # অডিও প্লে করা
    audio_file = open("response.mp3", "rb")
    st.audio(audio_file.read(), format="audio/mp3", autoplay=True)
    audio_file.close()
