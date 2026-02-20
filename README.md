# bass_it

Small Python project for bass-line analysis and generation.

Quick start

- Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

- Install dependencies (if provided):

```bash
pip install -r requirements.txt
```

- Run the app:

```bash
python src/main.py
```

Layout

- `bass.mid` — example MIDI file
- `src/` — source code
  - `main.py` — entry point
  - `analysis/` — BPM/key detection
  - `generation/` — bass generation code
  - `config/`, `constants/` — configuration
- `test_audios/` — test audio files

Notes

- Add a `requirements.txt` listing project dependencies (e.g., `librosa`, `numpy`, `mido`) if you want reproducible installs.
- macOS users: `.DS_Store` is ignored by `.gitignore`.
