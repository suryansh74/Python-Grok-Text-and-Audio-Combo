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

