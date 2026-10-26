# Python Graphical Music Player 🎵

A desktop MP3 music player built with **Python**, **Tkinter**, and **Pygame**. It provides a simple graphical interface for browsing and playing songs stored on your computer.

## Features

- **Graphical playlist:** Displays MP3 files from a selected folder.
- **Play:** Plays the selected track (or the first track when none is selected).
- **Pause / Resume:** A single button changes from **Pause** to **Resume** when playback is paused, then back to **Pause** when playback continues.
- **Stop:** Stops playback.
- **Previous / Next:** Navigates through the playlist.
- **Automatic next track:** Plays the next song when the current song finishes.
- **Volume control:** Adjusts playback volume with a slider.
- **Folder selection:** Loads MP3 files from a folder chosen using a file dialog.
- **Double-click playback:** Starts a song by double-clicking it in the playlist.

## Technologies

- **Python 3.11** (version used during development)
- **Tkinter** — desktop graphical user interface
- **Pygame Mixer** — audio playback
- **pathlib** — file and folder handling

## Requirements

- Python 3 installed on your computer
- Pygame 2.6.1 (version tested)
- Tkinter (usually included with Python on Windows)
- Local `.mp3` files

## Installation

1. Clone the repository (replace the placeholder with your repository URL):

   ```bash
   git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
   cd YOUR-REPOSITORY
   ```

2. Install Pygame:

   ```bash
   python -m pip install pygame
   ```

   On Windows, if you encounter a permissions error, try:

   ```bash
   python -m pip install --user pygame
   ```

3. Check that Tkinter is available:

   ```bash
   python -m tkinter
   ```

## Run the Application

Save the application code as `graphical_music_player.py` and run:

```bash
python graphical_music_player.py
```

The original application uses this default music folder:

```python
Path("C:/Users/JEAN MARIE/Music")
```

**Before publishing the code**, consider changing it to a portable path:

```python
Path.home() / "Music"
```

You can also use **Load Music Folder** in the application to select another folder. The application currently searches for `.mp3` files directly inside the chosen folder (not its subfolders).

## How to Use

1. Launch the application.
2. Load a folder containing MP3 files if needed.
3. Double-click a song in the playlist or click **Play**.
4. Click **Pause** to pause playback; the button changes to **Resume**.
5. Click **Resume** to continue playback; the button changes back to **Pause**.
6. Use **Previous**, **Next**, **Stop**, and the volume slider as needed.

## Project Structure

```text
python-graphical-music-player/
├── graphical_music_player.py
├── README.md
└── .gitignore                  # Optional
```

**Note:** Music files are not included in the repository. Use your own locally stored MP3 files.

## Possible Future Improvements

- Playback progress bar and track duration
- Shuffle and repeat modes
- Album artwork and track metadata
- Keyboard shortcuts
- Support for additional audio formats and playlist files
- More advanced interface styling

## What I Learned

This project demonstrates practical experience with Python GUI development, event-driven programming, audio playback, filesystem operations, and application state management. In particular, the **Pause / Resume** control shows how the interface can update dynamically based on playback state.

## Author

**Jean Marie Kenne**  
Python | Data Analytics | Software Development

---

*Built as a hands-on Python learning project.*
