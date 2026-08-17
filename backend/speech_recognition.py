import os
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
from dotenv import load_dotenv

load_dotenv()

SAMPLE_RATE = 44100

recording = None
audio_data = []


def audio_callback(indata, frames, time, status):

    if status:
        print("Audio status:", status)

    audio_data.append(indata.copy())


def start_recording():

    global recording
    global audio_data

    audio_data = []

    print("Recording started...")

    recording = sd.InputStream(
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="int16",
        callback=audio_callback
    )

    recording.start()


def stop_recording():

    global recording
    global audio_data

    if recording is None:
        return ""

    print("Recording stopped.")

    recording.stop()
    recording.close()
    recording = None

    if not audio_data:
        print("No audio recorded.")
        return ""

    audio = np.concatenate(
        audio_data,
        axis=0
    )

    os.makedirs(
        "recordings",
        exist_ok=True
    )

    filename = "recordings/audio.wav"

    write(
        filename,
        SAMPLE_RATE,
        audio
    )

    print("Audio saved:", filename)
    print("Audio size:", len(audio), "samples")
    print("Uploading audio to AssemblyAI...")

    try:

        import assemblyai as aai

        api_key = os.getenv("ASSEMBLYAI_API_KEY")

        if not api_key:

            print("ERROR: AssemblyAI API key not found.")

            return "AssemblyAI API key is missing."

        aai.settings.api_key = api_key

        transcriber = aai.Transcriber()

        transcript = transcriber.transcribe(
            filename
        )

        if transcript.status == aai.TranscriptStatus.error:

            print(
                "AssemblyAI error:",
                transcript.error
            )

            return "Transcription failed."

        print("Transcription complete.")

        return transcript.text or "No speech detected."

    except Exception as error:

        print(
            "AssemblyAI ERROR:",
            repr(error)
        )

        return "Unable to transcribe audio."