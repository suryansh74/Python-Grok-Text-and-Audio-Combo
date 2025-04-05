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

   ### This file does:
   
   A voice assistant that:
   - Listens to your voice on `Alt + L`
   - Stops listening on `Right Shift`
   - Sends transcription to Groq for an easy-to-understand explanation
   - Plays the response out loud using Edge TTS and ffplay
   
   ---
   
   ### Configuration Section
   
   #### `GROQ_API_KEY`, `MODEL`, `VOICES`, `VOICE`
   
   Sets up the API key, model name, and available voices. You can change the voice by modifying the `VOICE` variable.
   
   ---
   
   ### Initialization Section
   
   #### `console`, `recognizer`
   
   Initializes the `rich.console.Console` and the speech recognizer object from `speech_recognition`.
   
   #### State Variables
   
   Flags used to track whether the assistant is listening and which keys are pressed.
   
   ---
   
   ### `clean_text(text)`
   
   #### Functionality:
   - Cleans Groq's response
   - Removes symbols, emojis, markdown, and extra spaces
   - Keeps only readable characters for better speech output
   
   ---
   
   ### `send_to_groq(prompt)`
   
   #### Functionality:
   - Sends transcribed speech to Groq API
   - Adds an instruction to generate short, easy-to-understand replies
   - Cleans the response using `clean_text`
   - Removes any `<think>...</think>` tags
   
   ---
   
   ### `speak_streaming(text, pause_duration=0.01)`
   
   #### Functionality:
   - Splits text into sentences
   - Uses Edge TTS to generate audio for each sentence
   - Plays audio using `ffplay`
   - Optionally waits after each sentence for natural pacing
   
   ---
   
   ### `listen_loop()`
   
   #### Functionality:
   - Activates the microphone and starts collecting audio
   - Recognizes and prints each spoken segment
   - On `Right Shift`, stops listening
   - Displays full transcription and sends it to Groq
   - Speaks the response using `speak_streaming`
   
   ---
   
   ### Keyboard Event Handlers
   
   #### `on_press(key)`
   
   - Tracks key presses
   - If `Alt + L` is pressed, starts `listen_loop` in a new thread
   - If `Right Shift` is pressed while listening, stops the listener
   
   #### `on_release(key)`
   
   - Resets Alt key state when released
   
   ---
   
   ### `__main__` Block
   
   #### Functionality:
   - Prints startup message with hotkey instructions
   - Starts the keyboard listener to detect `Alt + L` and `Right Shift`
   
   ---
   
   ### How to Use
   
   1. Run the script.
   2. Press `Alt + L` to start speaking.
   3. Say something.
   4. Press `Right Shift` to stop.
   5. The script will transcribe, fetch a response from Groq, and speak the reply.

