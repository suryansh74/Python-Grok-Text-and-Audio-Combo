# Python-Grok-Text-and-Audio-Combo
It is completely free to use. In this folder there are 3 python files:  
For Input_Audio-->Text-->Groq_API-->Text_Response-->Output_Audio 

## Note:
Completely free to use and feel no limit if using for personal use only because:
Grok provides free api, very fast, and 30 request per minute(RPM) which is enough for human personal manual usuage. 

### How to make groq api free:
Go to groq official website, register it, get api, and in dashboard > limits you can also see many models you can choose and implement in this script

### Google Free Quota:
It Also uses Google Quota you can check it limit also use freely for human manual usage its also too much 

## About the code:

There are mainly three files 
1. audio2audio_complete.py: In this it listens to  *input_audio-->Google quota-->Text-->Grok_Api_hit-->Response_Text-->edge_tts(python library)-->output_audio
   This is documentation:
Voice Assistant Using Groq API and Edge TTS

This script creates a voice assistant that listens to your speech when you press Alt + L, transcribes it using Google's speech recognition, sends the transcription to Groq's language model for a response, and speaks the reply using Edge TTS.

Features:

Activation with Alt + L and deactivation with Right Shift

Real-time speech recognition and transcription

Cleans and simplifies AI response text

Streams text-to-speech using Edge TTS

Displays transcription and response using rich console UI

Threaded listening to avoid UI blocking

Hotkeys:

Alt + L: Start voice input

Right Shift: Stop voice input

Main Components:

Speech Recognition: Captures and transcribes speech using a microphone.

Groq API: Sends transcribed text and receives a brief, user-friendly explanation.

Text Cleaner: Removes special characters, emojis, and formatting for better TTS playback.

Streaming TTS: Breaks text into sentences and plays them one by one using Edge TTS and ffplay.

Keyboard Listener: Handles key combinations using pynput.

Core Logic:

Waits for Alt + L key combo to trigger recording.

Captures audio and builds a full transcription.

On Right Shift, stops listening and sends the collected text to Groq.

Receives a cleaned and short explanation from Groq API.

Converts response to speech and plays it sentence by sentence.

Configuration Options:

GROQ_API_KEY: Replace with your own Groq API key.

MODEL: Set to desired Groq model.

VOICES: Array of voices supported by Edge TTS. You can change the default one by modifying the VOICE variable.

pause_duration: Adjust pause after sentences while speaking.

Note:

The script uses threading and async to ensure smooth interaction and playback.

Make sure Edge TTS and FFmpeg (ffplay) are accessible in your system's PATH.

 
