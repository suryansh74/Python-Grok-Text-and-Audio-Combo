import speech_recognition as sr
import threading
import requests
import asyncio
import subprocess
from pynput import keyboard
from rich.console import Console
from rich.panel import Panel
import tempfile
import os
import re

# ==================== CONFIG ====================
GROQ_API_KEY = "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"
MODEL = "qwen-qwq-32b"
VOICES = ['en-AU-NatashaNeural', 'en-IE-EmilyNeural', 'en-IN-NeerjaNeural', 'en-US-AndrewMultilingualNeural']
VOICE = VOICES[3]

# ==================== INIT ====================
console = Console()
recognizer = sr.Recognizer()

# State
is_listening = False
stop_listening_flag = False
is_alt_pressed = False
is_right_shift_pressed = False

# ==================== CLEAN GROQ TEXT ====================
def clean_text(text):
    # Keep only letters, numbers, and spaces (remove everything else, including full stops)
    cleaned = re.sub(r'[^\w\s]', '', text)

    # Replace underscores (from \w) with nothing
    cleaned = re.sub(r'_', '', cleaned)

    # Collapse multiple spaces into one
    cleaned = re.sub(r'\s+', ' ', cleaned)

    # Strip leading/trailing whitespace
    return cleaned.strip()

# ==================== GROQ REQUEST ====================
def send_to_groq(prompt):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    json_data = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt + ". Explain in easy word with breif short explanation only"}
        ]
    }
    response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=json_data)
    response.raise_for_status()
    return clean_text(re.sub(r'<think>.*?</think>', '', response.json()["choices"][0]["message"]["content"], flags=re.DOTALL))

# ==================== TEXT TO SPEECH ====================
async def speak_streaming(text, pause_duration=0.01):  # customize pause duration here
    sentences = re.split(r'(?<=\.)\s+', text.strip())  # split only on full stop + space

    for sentence in sentences:
        if sentence:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmpfile:
                temp_path = tmpfile.name

            command = [
                "edge-tts",
                "--text", sentence,
                "--voice", VOICE,
                "--rate", "+0%",
                "--write-media", temp_path
            ]
            process = await asyncio.create_subprocess_exec(*command)
            await process.wait()

            play_cmd = await asyncio.create_subprocess_exec(
                "ffplay", "-nodisp", "-autoexit", "-loglevel", "quiet", temp_path
            )
            await play_cmd.wait()

            os.remove(temp_path)

            # Check if sentence ends with a full stop
            if sentence.strip().endswith("."):
                await asyncio.sleep(pause_duration)

# ==================== LISTEN + RESPOND LOOP ====================
def listen_loop():
    global is_listening, stop_listening_flag
    is_listening = True
    stop_listening_flag = False

    collected_text = ""

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        console.print("[bold cyan]🎙 Listening... (Press Right Shift to stop)[/bold cyan]")

        while not stop_listening_flag:
            try:
                audio = recognizer.listen(source, timeout=3)
                text = recognizer.recognize_google(audio)
                console.print(f"[blue]➕ {text}[/blue]")
                collected_text += " " + text
            except sr.WaitTimeoutError:
                continue
            except sr.UnknownValueError:
                console.print("[yellow]⚠️ Didn't catch that...[/yellow]")
            except Exception as e:
                console.print(f"[red]❌ Error: {e}[/red]")

    is_listening = False

    if collected_text.strip():
        console.print(Panel(collected_text, title="📝 Full Transcription", style="green"))

        try:
            response = send_to_groq(collected_text)
            console.print(Panel(response, title="🤖 Groq Response", style="cyan"))
            asyncio.run(speak_streaming(response))
        except Exception as e:
            console.print(f"[bold red]❌ Error during response: {e}[/bold red]")

    console.print("[bold green]✅ Done! Press Alt + L to speak again.[/bold green]")


# ==================== KEYBOARD HANDLERS ====================
def on_press(key):
    global is_alt_pressed, is_listening, stop_listening_flag

    if key == keyboard.Key.alt_l or key == keyboard.Key.alt_r:
        is_alt_pressed = True

    elif key == keyboard.Key.shift_r:
        if is_listening:
            stop_listening_flag = True

    elif hasattr(key, 'char') and key.char == 'l' and is_alt_pressed:
        if not is_listening:
            threading.Thread(target=listen_loop, daemon=True).start()
        else:
            console.print("[bold yellow]Already listening. Press Right Shift to stop.[/bold yellow]")

def on_release(key):
    global is_alt_pressed

    if key == keyboard.Key.alt_l or key == keyboard.Key.alt_r:
        is_alt_pressed = False


# ==================== MAIN ====================
if __name__ == "__main__":
    console.print("[bold green]✅ Voice Assistant is running![/bold green]\n[bold magenta]🔊 Press Alt+L + Right Shift to start\n🔇 Press Right Shift to stop[/bold magenta]")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
