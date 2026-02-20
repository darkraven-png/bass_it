
# bass_it

Minimal toolkit for bass-line analysis and generation (BPM/key detection and MIDI/bass generation).

Prerequisites

- Python 3.8+ recommended
- See `requirements.txt` for Python package dependencies

Quick install

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run

```bash
python src/main.py
```

Project layout

- `bass.mid` — example MIDI file
- `requirements.txt` — Python dependencies
- `src/` — application source
  - `main.py` — entry point
  - `analysis/` — BPM and key detection modules
  - `generation/` — bass generation logic
  - `config/`, `constants/` — configuration values
- `test_audios/` — example audio files used for testing

Usage notes

- To reproduce results install packages from `requirements.txt` into a virtual environment.
- If you work with audio files, ensure `libsndfile` is installed on your system (often required by `python-soundfile`).
- The project currently uses `librosa` and `mido` for audio analysis and MIDI handling.

I’ll explain **how these libraries work together in a typical music/audio pipeline** and why a project might use *all of them together*.

---

# 🎵 Typical Audio + MIDI Processing Pipeline

## 1️⃣ Load Audio File

**Libraries involved:** `librosa`, `python-soundfile`, `numpy`

### What happens:

* `librosa` loads the audio.
* `python-soundfile` handles the low-level file reading.
* The audio becomes a `numpy` array for processing.

### Flow:

```
audio.wav → soundfile → librosa → numpy array
```

Example:

```python
import librosa
y, sr = librosa.load("audio.wav")
```

Now:

* `y` = waveform (NumPy array)
* `sr` = sample rate

---

## 2️⃣ Audio Feature Extraction

**Libraries involved:** `librosa`, `scipy`, `numpy`

This is where signal processing happens.

You might compute:

* Spectrogram
* MFCCs
* Tempo
* Chroma features
* Onset detection

Example:

```python
mfcc = librosa.feature.mfcc(y=y, sr=sr)
```

Under the hood:

* `librosa` uses `numpy`
* `librosa` uses `scipy.signal` for filtering & FFT

---

## 3️⃣ Work With MIDI Files

There are **two MIDI libraries** because they serve different purposes.

---

## 🎹 `mido` → Low-Level MIDI Control

Best for:

* Reading raw MIDI messages
* Sending MIDI to hardware
* Editing MIDI messages manually

Example:

```python
import mido
mid = mido.MidiFile("song.mid")
for msg in mid:
    print(msg)
```

Think of `mido` as:

> “Raw MIDI message access”

---

## 🎼 `pretty_midi` → High-Level Music Processing

Best for:

* Musical structure
* Notes, instruments
* Piano rolls
* Tempo analysis

Example:

```python
import pretty_midi
midi = pretty_midi.PrettyMIDI("song.mid")
piano_roll = midi.get_piano_roll()
```

Think of `pretty_midi` as:

> “Music-aware MIDI manipulation”

---

# 🎯 Why Use BOTH `mido` and `pretty_midi`?

Because they solve different problems:

| Library     | Level      | Best For                           |
| ----------- | ---------- | ---------------------------------- |
| mido        | Low-level  | MIDI message editing, hardware I/O |
| pretty_midi | High-level | Musical analysis, ML features      |

A project might:

* Use `pretty_midi` for analysis
* Use `mido` to export custom MIDI messages

---

# 🧠 Full Example Pipeline (Music AI Project)

Here’s how everything could connect:

```
1. Load audio → librosa
2. Extract features → librosa + scipy
3. Convert MIDI → pretty_midi
4. Edit/export MIDI → mido
5. All data stored in numpy arrays
```

---

# 🎼 What Type of Projects Use This Stack?

This exact dependency list is common in:

* 🎵 Music transcription (audio → MIDI)
* 🤖 AI music generation
* 🎹 Piano roll modeling
* 🎼 MIR (Music Information Retrieval)
* 🎧 Beat detection systems
* 🎚 Audio feature extraction for ML

---

# 🏗 Simple Mental Model

Think of it like this:

* **NumPy** → Math engine
* **SciPy** → Advanced signal tools
* **SoundFile** → Audio file reader
* **Librosa** → Audio/music analysis
* **PrettyMIDI** → Music structure layer
* **Mido** → Raw MIDI control layer

---

If you'd like, I can also:

* Show a concrete real-world example (audio → MIDI converter structure)
* Explain common errors when installing these
* Draw a simplified diagram of data flow
* Or explain how this relates to machine learning 🎯


