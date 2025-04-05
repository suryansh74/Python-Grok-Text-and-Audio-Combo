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
