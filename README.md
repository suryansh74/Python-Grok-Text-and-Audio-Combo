# Python-Groq-Text-and-Audio-Combo

🎧 This is a **free, fully functional voice assistant** system using Python, Google Speech API, Groq for language processing, and Edge TTS for audio playback.

🗃️ **It includes 3 Python files**, for processing:
**Input_Audio ➜ Text ➜ Groq_API ➜ Text_Response ➜ Output_Audio**

---

### 📝 Note:
- Completely free to use for **personal/manual usage**.
- ⚡ **Groq** provides a **fast, free API** with **30 requests per minute**, which is enough for normal use.

---

### 🧪 How to get a free Groq API:
1. Go to [Groq Official Website](https://groq.com/)
2. Register an account.
3. Get your API key from the dashboard.
4. Under **Limits**, you'll find available models — choose any and update the script accordingly.

---

### 🌐 Google Free Quota:
Google's speech-to-text API (used via `speech_recognition`) also has a generous free tier for personal usage. You’re unlikely to hit limits during normal use.

---  
---
## 📦 Install Required Libraries

Make sure to install the following dependencies before running the scripts. You can use `pip` to install them all at once:

### ✅ Recommended Installation Command:

```bash
pip install speechrecognition pynput rich requests asyncio groq
```

### 📚 Included Libraries:

| Library                | Purpose                                                                 |
|------------------------|-------------------------------------------------------------------------|
| `speechrecognition`    | Captures and transcribes voice using Google Speech API                  |
| `pynput`               | Detects global keyboard shortcuts and simulates typing                  |
| `rich`                 | Provides styled terminal output with panels, colors, and formatting     |
| `requests`             | Makes HTTP requests (used for APIs or TTS services)                     |
| `asyncio`              | Manages asynchronous execution for concurrent tasks                     |
| `groq`                 | Interacts with the Groq API for generating AI responses                 |
| `shutil`, `os`, `re`, `time`, `tempfile`, `subprocess`, `threading`, `warnings` | Standard Python libraries, no installation needed |

> ✅ All scripts are compatible with **Python 3.8+**

---

### 💡 Tip:
If you're working in a virtual environment, activate it first before installing the packages.

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

You can also create a `requirements.txt` file with the following content:

```
speechrecognition
pynput
rich
requests
asyncio
groq
```

And install it using:

```bash
pip install -r requirements.txt
```

---  
---


## 📂 About the Code Files

### 1. `audio2audio_complete.py`
Performs the full pipeline:
**Input_Audio ➜ Google ➜ Text ➜ Groq ➜ Response ➜ Edge_TTS ➜ Output_Audio**

---

### 📌 This file does:
- 🎙️ Listens to your voice with `Alt + L`
- ✋ Stops listening on `Right Shift`
- 💬 Sends transcription to Groq for simplified explanation
- 🔊 Speaks the response using Edge TTS + ffplay

---

### ⚙️ Configuration Section

#### `GROQ_API_KEY`, `MODEL`, `VOICES`, `VOICE`
- Define the Groq API key and preferred model.
- You can switch TTS voices by changing the `VOICE` value from the list.

---

### 🧰 Initialization Section

#### `console`, `recognizer`
- Initializes `rich.console.Console` for UI and `speech_recognition.Recognizer`.

#### State Flags
- Controls whether the assistant is listening and tracks key states like `Alt` or `Shift`.

---

### 🧹 `clean_text(text)`

**Functionality:**
- Cleans the response from Groq.
- Removes symbols, markdown, emojis, etc.
- Outputs clean, readable text for speech.

---

### 🔁 `send_to_groq(prompt)`

**Functionality:**
- Sends your text to Groq API with an instruction to respond in short, simple explanations.
- Cleans the result using `clean_text`.
- Strips unwanted `<think>` tags.

---

### 🔊 `speak_streaming(text, pause_duration=0.01)`

**Functionality:**
- Splits the response into sentences.
- Uses **Edge TTS** to generate and play audio.
- Adds small pauses after each sentence for natural flow.

---

### 🎧 `listen_loop()`

**Functionality:**
- Activates your mic to start listening.
- Transcribes your speech in real-time.
- Stops on `Right Shift`.
- Sends full text to Groq and plays back the response using TTS.

---

### 🎹 Keyboard Event Handlers

#### `on_press(key)`
- Detects if:
  - `Alt + L` ➜ Starts listening.
  - `Right Shift` ➜ Stops listening.

#### `on_release(key)`
- Resets the `Alt` key state after release.

---

### 🚀 `__main__` Block

**Functionality:**
- Shows startup instructions in console.
- Starts the keyboard listener for hotkey interaction.

---

### ✅ How to Use

1. Run the script: `python audio2audio_complete.py`
2. Press `Alt + L` to begin speaking.
3. Speak into your microphone.
4. Press `Right Shift` to stop.
5. The assistant will:
   - Transcribe your voice,
   - Send it to Groq for explanation,
   - Speak the answer back using Edge TTS.

---  
---

## 🗣️ speech_to_ai_response.py

This script listens to your speech, transcribes it using **Google Speech Recognition**, sends the text to **Groq AI**, and displays the response in the terminal using **Rich** formatting.

---

### 🚀 Features:
- 🎙️ Listens to your voice until you press `Enter`.
- 🧠 Sends your input to Groq AI for processing.
- 💬 Streams the response and displays it in a clean terminal layout.
- 🖥️ Uses `Rich` to format output in panels with colors and styles.
- 🎧 Handles audio warnings silently using `os.environ`.

---

### 🛠️ Environment Setup

```python
os.environ["PYTHONWARNINGS"] = "ignore"
os.environ["SDL_AUDIODRIVER"] = "dummy"
os.environ["PULSE_LOG"] = "0"
```

- Suppresses Python, ALSA, and PulseAudio warnings.
- Ensures smoother CLI experience.

---

### 🔑 Configuration

#### `API_KEY` and `model_name`

```python
API_KEY = "Grok_API"
model_name = "deepseek-r1-distill-qwen-32b"
```

- Replace `"Grok_API"` with your actual **Groq API key**.
- You can switch the model depending on what’s available in your Groq dashboard.

---

### 🧠 Function: `recognize_speech()`

```python
def recognize_speech():
```

- Activates the mic and listens until Enter is pressed.
- Uses `speech_recognition` to capture audio in chunks.
- Combines audio frames for batch transcription.
- Sends recognized text to Groq via `send_to_groq()`.

📦 **Handles**:
- ✅ Ambient noise adjustment
- ⚠️ No audio detected
- ⚠️ Google API errors
- ⚠️ Unintelligible speech

---

### ⏹️ Function: `listen_for_stop()`

```python
def listen_for_stop():
```

- Waits for the `Enter` key to set `stop_listening = True`.
- Used to end the audio capture gracefully.

---

### 📡 Function: `send_to_groq(prompt)`

```python
def send_to_groq(prompt):
```

- Sends recognized text to the Groq API using the `groq` client.
- Uses `stream=True` to simulate real-time replies.
- Assembles full response and displays it using a Rich panel.

🪄 **Output**:
- Styled Groq response in `[bold magenta]💬 Groq Response[/bold magenta]` panel.

---

### 🧵 Main Loop Execution

```python
if __name__ == "__main__":
```

- Keeps running in a loop.
- For each interaction:
  1. Resets `stop_listening` flag.
  2. Starts a thread to detect Enter key.
  3. Starts the voice recognition function.
  4. Waits for Enter to proceed again.

🖼️ **UI Enhancements**:
- Uses `shutil.get_terminal_size().columns` to create full-width visual separators.
- Uses `[bold cyan]🚀 PRESS ENTER FOR NEXT RESPONSE 🚀` centered message.

---

### ✅ How to Use

1. Replace `API_KEY = "Grok_API"` with your actual Groq key.
2. Run the script:
   ```bash
   python speech_to_ai_response.py
   ```
3. Speak into the microphone.
4. Press `Enter` to stop recording and process the response.
5. View the formatted AI response in your terminal.
6. Press `Enter` again to repeat the cycle.

---  
---

## 🎧 voice_typing_assistant.py

This script listens to your voice using **Google Speech Recognition**, transcribes the speech, and then **types it automatically** into the active input field. It uses `pynput` to listen for hotkeys and `Rich` to display status messages in a styled terminal.

---

### 🚀 Features:
- 🗣️ Press `Alt + K` to **start speech recognition**.
- 🛑 Press `Right Shift` to **stop listening**.
- ⌨️ Automatically types the transcribed text into the focused input.
- 🎛️ Uses Rich for colored panels and styled output.
- 🎤 Captures continuous chunks of audio until stopped.
- 🧠 Uses threading to allow background execution.

---

### 🛠️ Dependencies

```bash
pip install SpeechRecognition pynput rich
```

---

### 🧠 Function: `listen_and_type()`

```python
def listen_and_type():
```

- Starts capturing audio using your default microphone.
- Adjusts for ambient noise.
- Collects audio in small chunks.
- Once stopped, it:
  - Combines the chunks.
  - Transcribes speech using Google API.
  - Types the resulting text using `pynput.keyboard.Controller`.
  - Displays the transcribed text in a Rich panel.

📦 **Handles**:
- ✅ Noisy background
- ⚠️ Timeout errors
- ⚠️ Speech not recognized
- ⚠️ Google API request errors

---

### 🧩 Function: `type_text(text)`

```python
def type_text(text):
```

- Waits briefly to give focus to the input field.
- Types the transcribed text using `keyboard_controller.type()`.

---

### 🎛️ Keyboard Controls

#### 🔍 `on_press(key)`

```python
def on_press(key):
```

- `Alt + K`: Starts listening if not already listening.
- `Right Shift`: Stops the current speech capture session.

#### 🔄 `on_release(key)`

```python
def on_release(key):
```

- Tracks when `Alt` key is released to reset flag.

---

### 🏁 Entry Point

```python
if __name__ == "__main__":
```

- Starts the script and shows the message:
  ```
  ✅ Script is running! Press Alt+K to start listening. Press Right Shift to stop and type the text.
  ```
- Starts the `keyboard.Listener` in the background to monitor key events.

---

### ✅ How to Use

1. Ensure your mic is connected and working.
2. Run the script:
   ```bash
   python voice_typing_assistant.py
   ```
3. Focus on an input field (browser, editor, chat box, etc).
4. Press `Alt + K` to begin speech recognition.
5. Speak your sentence clearly.
6. Press `Right Shift` to stop and let the script transcribe + type your sentence.

---

### 🧼 Notes

- Works best in quiet environments.
- Slight delay added before typing to ensure input field is active.
- Ideal for hands-free typing, accessibility tools, or productivity.

---

