# generation/bass_generator.py

import pretty_midi
from constants.constants import CHORD_ROOTS, DEFAULT_VELOCITY
from config.config import BPM, BEATS_PER_CHORD


def extract_root(chord_name: str) -> str:
    """
    Extract pitch class from chord string.
    Example:
        Am7 -> A
        D7  -> D
        C#m -> C#
    """
    if len(chord_name) > 1 and chord_name[1] == "#":
        return chord_name[:2]
    return chord_name[0]


def generate_bass_midi(chord_sequence, output_file):
    seconds_per_beat = 60 / BPM

    midi = pretty_midi.PrettyMIDI(initial_tempo=BPM)
    bass_program = pretty_midi.instrument_name_to_program("Electric Bass (finger)")
    bass = pretty_midi.Instrument(program=bass_program)

    current_time = 0.0

    for chord in chord_sequence:
        root_name = extract_root(chord)
        root_pitch = CHORD_ROOTS[root_name]

        note = pretty_midi.Note(
            velocity=DEFAULT_VELOCITY,
            pitch=root_pitch,
            start=current_time,
            end=current_time + BEATS_PER_CHORD * seconds_per_beat
        )

        bass.notes.append(note)
        current_time += BEATS_PER_CHORD * seconds_per_beat

    midi.instruments.append(bass)
    midi.write(output_file)

    return output_file