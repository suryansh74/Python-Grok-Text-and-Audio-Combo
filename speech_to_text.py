import speech_recognition as sr
import threading
from pynput import keyboard
from pynput.keyboard import Controller as KeyboardController
from rich.console import Console
from rich.panel import Panel
import time

console = Console()
recognizer = sr.Recognizer()
keyboard_controller = KeyboardController()

# State flags
is_listening = False
stop_listening_flag = False
is_alt_pressed = False

def type_text(text):
    time.sleep(0.5)  # Give time to focus input field
    keyboard_controller.type(text)

def listen_and_type():
    global is_listening, stop_listening_flag
    is_listening = True
    stop_listening_flag = False

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        console.print("[bold cyan]🎙 Listening... Press Right Shift to stop[/bold cyan]")

        audio_chunks = []

        while not stop_listening_flag:
            try:
                audio = recognizer.listen(source, timeout=2)
                audio_chunks.append(audio)
            except sr.WaitTimeoutError:
                continue

        if audio_chunks:
            combined_audio = sr.AudioData(
                b''.join([chunk.get_wav_data() for chunk in audio_chunks]),
                source.SAMPLE_RATE,
                source.SAMPLE_WIDTH
            )

            try:
                text = recognizer.recognize_google(combined_audio)
                console.print(Panel(f"{text}", title="📝 Transcribed Text", style="green"))
                type_text(text)
            except sr.UnknownValueError:
                console.print("[bold yellow]⚠️ Could not understand the audio.[/bold yellow]")
            except sr.RequestError as e:
                console.print(f"[bold red]❌ Google Speech API error: {e}[/bold red]")
        else:
            console.print("[bold yellow]⚠️ No speech captured.[/bold yellow]")

    is_listening = False
    console.print("[bold blue]Ready again! Press Alt+K to listen...[/bold blue]")

def on_press(key):
    global is_alt_pressed, is_listening, stop_listening_flag

    if key == keyboard.Key.alt_l or key == keyboard.Key.alt_r:
        is_alt_pressed = True

    elif is_alt_pressed and hasattr(key, 'char') and key.char == 'k':
        if not is_listening:
            threading.Thread(target=listen_and_type, daemon=True).start()
        else:
            console.print("[bold yellow]Already listening. Press Right Shift to stop first.[/bold yellow]")

    elif key == keyboard.Key.shift_r:  # 🛑 Only right shift stops listening
        if is_listening:
            stop_listening_flag = True

def on_release(key):
    global is_alt_pressed
    if key == keyboard.Key.alt_l or key == keyboard.Key.alt_r:
        is_alt_pressed = False

if __name__ == "__main__":
    console.print("[bold green]✅ Script is running! Press Alt+K to start listening. Press Right Shift to stop and type the text.[/bold green]\n")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()



