
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from pathlib import Path
import pygame

# Initialize Pygame
pygame.mixer.init()


class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("JM KENNE Music Player")
        self.root.geometry("650x520")
        self.root.configure(bg="#171725")

        self.playlist = []
        self.current_song = 0
        self.paused = False
        self.playing = False

        self.create_widgets()

        # Default music folder
        self.load_music_folder(
            Path.home() / "Music"
        )

        # Check for song completion
        self.check_music()

    def create_widgets(self):
        title = tk.Label(
            self.root,
            text="JM KENNE MUSIC PLAYER",
            font=("Arial", 22, "bold"),
            bg="#171725",
            fg="white"
        )
        title.pack(pady=15)

        self.song_label = tk.Label(
            self.root,
            text="No song playing",
            font=("Arial", 12),
            bg="#171725",
            fg="#66D9EF",
            wraplength=580
        )
        self.song_label.pack(pady=10)

        # Playlist
        self.listbox = tk.Listbox(
            self.root,
            width=65,
            height=12,
            font=("Arial", 11),
            bg="#242438",
            fg="white",
            selectbackground="#6741D9",
            selectforeground="white"
        )
        self.listbox.pack(pady=10)

        self.listbox.bind(
            "<Double-Button-1>",
            self.select_song
        )

        # Control buttons
        controls = tk.Frame(
            self.root,
            bg="#171725"
        )
        controls.pack(pady=15)

        buttons = [
            ("Previous", self.previous_song),
            ("Play", self.play_song),
            ("Stop", self.stop_song),
            ("Next", self.next_song)
        ]

        # Create Pause / Resume button
        self.pause_button = tk.Button(
            controls,
            text="Pause",
            command=self.pause_song,
            width=10,
            bg="#6741D9",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            cursor="hand2"
        )

        self.pause_button.pack(side=tk.LEFT, padx=4)

        for text, command in buttons:
            tk.Button(
                controls,
                text=text,
                command=command,
                width=10,
                bg="#6741D9",
                fg="white",
                font=("Arial", 10, "bold"),
                relief="flat",
                cursor="hand2"
            ).pack(side=tk.LEFT, padx=4)

        # Volume control
        volume_frame = tk.Frame(
            self.root,
            bg="#171725"
        )
        volume_frame.pack(pady=10)

        tk.Label(
            volume_frame,
            text="Volume",
            bg="#171725",
            fg="white"
        ).pack(side=tk.LEFT, padx=10)

        self.volume_slider = ttk.Scale(
            volume_frame,
            from_=0,
            to=100,
            orient=tk.HORIZONTAL,
            command=self.change_volume,
            length=220
        )
        self.volume_slider.set(70)
        self.volume_slider.pack(side=tk.LEFT)

        pygame.mixer.music.set_volume(0.7)

        # Load folder button
        tk.Button(
            self.root,
            text="Load Music Folder",
            command=self.choose_folder,
            bg="#00A896",
            fg="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            padx=15,
            pady=8
        ).pack(pady=10)

        self.root.protocol(
            "WM_DELETE_WINDOW",
            self.close_player
        )

    def load_music_folder(self, folder):
        folder = Path(folder)

        if not folder.is_dir():
            messagebox.showwarning(
                "Folder not found",
                f"Cannot find: {folder}"
            )
            return

        songs = sorted(
            folder.glob("*.mp3")
        )

        if not songs:
            messagebox.showinfo(
                "No music",
                "No MP3 files found in this folder."
            )
            return

        pygame.mixer.music.stop()
        self.playlist = songs
        self.current_song = 0
        self.playing = False
        self.paused = False

        self.pause_button.config(
            text="Pause",
            bg="#6741D9"
        )

        self.listbox.delete(0, tk.END)

        for song in self.playlist:
            self.listbox.insert(
                tk.END,
                song.name
            )

        self.song_label.config(
            text=f"{len(songs)} songs loaded"
        )

    def choose_folder(self):
        folder = filedialog.askdirectory()

        if folder:
            self.load_music_folder(folder)

    def select_song(self, event):
        selection = self.listbox.curselection()

        if selection:
            self.current_song = selection[0]
            self.play_song()

    def play_song(self):
        if not self.playlist:
            messagebox.showinfo(
                "Playlist empty",
                "Please load a music folder."
            )
            return

        if self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
            self.playing = True
            return

        song = self.playlist[self.current_song]

        try:
            pygame.mixer.music.load(str(song))
            pygame.mixer.music.play()
        except pygame.error as error:
            messagebox.showerror(
                "Playback error",
                str(error)
            )
            self.playing = False
            return

        self.playing = True
        self.paused = False

        self.pause_button.config(
            text="Pause",
            bg="#6741D9"
        )

        self.song_label.config(
            text=f"Now Playing: {song.name}"
        )

        self.listbox.selection_clear(
            0, tk.END
        )
        self.listbox.selection_set(
            self.current_song
        )
        self.listbox.see(
            self.current_song
        )

    
    def pause_song(self):
        if not self.playing:
            return

        if self.paused:
            # Resume music
            pygame.mixer.music.unpause()
            self.paused = False

            # Change button back to Pause
            self.pause_button.config(
                text="Pause",
                bg="#6741D9"
            )

            self.song_label.config(
                text="Playing: " +
                self.playlist[self.current_song].name
            )

        else:
            # Pause music
            pygame.mixer.music.pause()
            self.paused = True

            # Change button to Resume
            self.pause_button.config(
                text="Resume",
                bg="#00A896"
            )

            self.song_label.config(
                text="Paused: " +
                self.playlist[self.current_song].name
            )


    def stop_song(self):
        pygame.mixer.music.stop()
        self.playing = False
        self.paused = False
        self.song_label.config(
            text="Playback stopped"
        )

        self.pause_button.config(
            text="Pause",
            bg="#6741D9"
        )

    def next_song(self):
        if not self.playlist:
            return

        self.current_song = (
            self.current_song + 1
        ) % len(self.playlist)

        self.paused = False
        self.play_song()

    def previous_song(self):
        if not self.playlist:
            return

        self.current_song = (
            self.current_song - 1
        ) % len(self.playlist)

        self.paused = False
        self.play_song()

    def change_volume(self, value):
        pygame.mixer.music.set_volume(
            float(value) / 100
        )

    def check_music(self):
        # Move to next song when playback ends
        if self.playing and not self.paused:
            if not pygame.mixer.music.get_busy():
                self.next_song()

        self.root.after(
            500,
            self.check_music
        )

    def close_player(self):
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        self.root.destroy()


# Start application
if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
