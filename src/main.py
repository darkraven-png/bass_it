# main.py

from config.config import CHORD_SEQUENCE, OUTPUT_FILE
from generation.bass_generator import generate_bass_midi


def main():
    output = generate_bass_midi(CHORD_SEQUENCE, OUTPUT_FILE)
    print(f"Bass MIDI generated: {output}")


if __name__ == "__main__":
    main()