import numpy as np

# Krumhansl–Schmuckler Key Profiles
MAJOR_PROFILE = np.array([
    6.35, 2.23, 3.48, 2.33,
    4.38, 4.09, 2.52, 5.19,
    2.39, 3.66, 2.29, 2.88
])

MINOR_PROFILE = np.array([
    6.33, 2.68, 3.52, 5.38,
    2.60, 3.53, 2.54, 4.75,
    3.98, 2.69, 3.34, 3.17
])

PITCH_CLASSES = [
    'C', 'C#', 'D', 'D#',
    'E', 'F', 'F#', 'G',
    'G#', 'A', 'A#', 'B'
]

# MIDI note numbers for common bass roots (octave 2 range)
CHORD_ROOTS = {
    "C": 48,
    "C#": 49,
    "D": 50,
    "D#": 51,
    "E": 52,
    "F": 53,
    "F#": 54,
    "G": 55,
    "G#": 56,
    "A": 57,
    "A#": 58,
    "B": 59
}

DEFAULT_VELOCITY = 100
DEFAULT_OCTAVE_SHIFT = 0  # Can shift bass up/down later