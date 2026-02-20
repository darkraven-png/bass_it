import librosa
import numpy as np
from src.constants.constants import MAJOR_PROFILE, MINOR_PROFILE, PITCH_CLASSES


def detect_key(file_path):
    print("Loading audio...")
    y, sr = librosa.load(file_path)

    print("Extracting chroma features...")
    chroma = librosa.feature.chroma_cqt(y=y, sr=sr)

    chroma_avg = np.mean(chroma, axis=1)

    best_score = -1
    best_key = None

    for i in range(12):
        rotated_major = np.roll(MAJOR_PROFILE, i)
        rotated_minor = np.roll(MINOR_PROFILE, i)

        major_score = np.corrcoef(chroma_avg, rotated_major)[0, 1]
        minor_score = np.corrcoef(chroma_avg, rotated_minor)[0, 1]

        if major_score > best_score:
            best_score = major_score
            best_key = f"{PITCH_CLASSES[i]} Major"

        if minor_score > best_score:
            best_score = minor_score
            best_key = f"{PITCH_CLASSES[i]} Minor"

    return best_key


if __name__ == "__main__":
    key = detect_key("test_audios/AUD-20251210-WA0002.mp3")
    print("Detected Key:", key)