import librosa
import numpy as np

def detect_bpm(file_path):
    print("Loading audio...")
    y, sr = librosa.load(file_path)

    print("Analyzing tempo...")
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)

    # FIX: extract first value if array
    tempo = float(tempo[0])

    print(f"Raw Detected Tempo: {tempo:.2f}")
    print(f"Number of beats detected: {len(beats)}")

    # Auto-correct common half/double time mistakes
    if tempo < 70:
        tempo *= 2
        print("Adjusted (double-time correction applied)")

    if tempo > 180:
        tempo /= 2
        print("Adjusted (half-time correction applied)")

    return tempo


if __name__ == "__main__":
    file = "AUD-20251210-WA0002.mp3"
    bpm = detect_bpm(file)
    print(f"Final BPM: {bpm:.2f}")