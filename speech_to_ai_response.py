import speech_recognition as sr
from groq import Groq
import threading
import os
import warnings
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import shutil
terminal_width = shutil.get_terminal_size().columns


# Suppress ALSA warnings
os.environ["PYTHONWARNINGS"] = "ignore"
os.environ["SDL_AUDIODRIVER"] = "dummy"  # Prevents some JACK errors
os.environ["PULSE_LOG"] = "0"  # Suppresses PulseAudio logs

# Redirect ALSA errors to null (silent)
alsa_no_logs = "2>/dev/null"
os.system(f"export ALSA_LOG_LEVEL=0 {alsa_no_logs}")

warnings.filterwarnings("ignore")  # Ignore Python warnings

# Initialize rich console
console = Console()

# Groq API Key
API_KEY = "Grok_API"
model_name = "deepseek-r1-distill-qwen-32b"

recognizer = sr.Recognizer()
stop_listening = False  # Control flag

def recognize_speech():
    """Listens until Enter is pressed, then sends the recognized text to Groq."""
    global stop_listening
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        console.print("\n[bold cyan]🎤 Listening... (Press Enter to stop)[/bold cyan]")

        audio_frames = []
        while not stop_listening:
            try:
                audio = recognizer.listen(source, timeout=2)  # Capture small chunks
                audio_frames.append(audio)
            except sr.WaitTimeoutError:
                continue  # Ignore timeout and keep listening

        # Combine all audio chunks into one
        if audio_frames:
            combined_audio = sr.AudioData(
                b"".join([chunk.get_wav_data() for chunk in audio_frames]),
                source.SAMPLE_RATE,
                source.SAMPLE_WIDTH,
            )

            try:
                text = recognizer.recognize_google(combined_audio)
                console.print(Panel(f"📝 Recognized: {text}", title="[bold green]Speech Recognition[/bold green]", style="green"))
                send_to_groq(text)  # Send to Groq API
            except sr.UnknownValueError:
                console.print("\n[bold yellow]⚠️ Could not understand the audio.[/bold yellow]")
            except sr.RequestError as e:
                console.print(f"\n[bold red]⚠️ Google Speech API error: {e}[/bold red]")
        else:
            console.print("\n[bold yellow]⚠️ No valid speech detected.[/bold yellow]")

def listen_for_stop():
    """Waits for Enter key press to stop listening."""
    global stop_listening
    input()  # Blocks until Enter is pressed
    stop_listening = True

def send_to_groq(prompt):
    """Sends recognized text to Groq API and prints the response clearly."""
    console.print("\n[bold blue]🧠 Processing...[/bold blue]")
    client = Groq(api_key=API_KEY)

    response = client.chat.completions.create(
        messages=[{"role": "user", "content": f"{prompt}"}],
        model=model_name,
        stream=True,  # Streaming response
    )

    response_text = ""  # Collect response for clear output
    for chunk in response:
        if chunk.choices[0].delta.content:
            response_text += chunk.choices[0].delta.content

    console.print(Panel(response_text, title="[bold magenta]💬 Groq Response[/bold magenta]", style="magenta"))

if __name__ == "__main__":
    while True:
        stop_listening = False
        threading.Thread(target=listen_for_stop).start()
        recognize_speech()  # Start listening
        # Centered message
        console.print("[bold cyan]🚀 PRESS ENTER FOR NEXT RESPONSE 🚀[/bold cyan]", justify="center")

        # Another full-width separator
        console.print("[bold yellow]═[/bold yellow]" * terminal_width, style="yellow")

        input("\nPress Enter to continue...")

